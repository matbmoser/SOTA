# coding=UTF-8
import traceback
from operators.op import op
from protocols.Protocol import Protocol, Message
from protocols.HTTPProtocol import HTTPMessage
import hashlib
import base64
import struct
import copy


"""
EXAMPLE OF WEBSOCKET FRAME STRUCTURE:

 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-------+-+-------------+-------------------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
| |1|2|3|       |K|             |                               |
+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                               |Masking-key, if MASK set to 1  |
+-------------------------------+-------------------------------+
| Masking-key (continued)       |          Payload Data         |
+-------------------------------- - - - - - - - - - - - - - - - +
:                     Payload Data continued ...                :
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|                     Payload Data continued ...                |
+---------------------------------------------------------------+
"""


class WebSocketProtocol(Protocol):
    """
    # Web Socket Protocol

    inherits from ```BaseProtocol```

    Description ::
    -----------

    Defines the work flow and treatment of the information in Web Socket.

    Input ::
    -----

    :attr int buffer: Defines the amount of data that is received by the socket.

    Attributes ::
    ----------

    :attr str|bytes acceptKey: Contains the WebSocket response acceptkey

    :attr bool fragmented: Indicates if processed message is fragmented

    :attr bytes fragmentedMessage: Contains the fragmented content

    :attr bool handshakeCompleted: Indicates if the handshakes has been completed

    """

    def __init__(self, buffer=2048):
        super().__init__(buffer=buffer)
        self.acceptKey = None
        self.keepAlive = True  # The server must stay connected
        self.fragmented = False
        self.fragmentedMessage = None
        self.handshakeCompleted = False

    # ================================================================
    # MESSAGE HANDLE METHODS

    # Returns the message type and configures the request
    def getMessage(self, input=None):
        if self.acceptKey == None:
            res = WebSocketHTTPRequest(rawdata=input)
        elif not self.handshakeCompleted:
            res = WebSocketHTTPResponse(rawdata=input)
        else:
            res = WebSocketMessage(rawdata=input)
        return res

    # Prepares and returns a close message
    def getCloseMessage(self):
        return self.newMessage(FIN=0b1, OPCODE=0x8, PAYLOAD="Connection Closed! Server shutdown")

    # Prepares the a new message with a desired structure of the protocol including the data passed as params
    # (Return None if fails and the message object configured if not)
    def newMessage(self, FIN=0b1, OPCODE=None, PAYLOAD="", RSV=[]):
        try:
            # Create a new message
            tmpMessage = WebSocketMessage()

            # If the opcode is defined
            if(OPCODE != None and OPCODE != ""):
                # Prepare the message to send
                tmpMessage.prepareMessage(
                    FIN=FIN, OPCODE=OPCODE, PAYLOAD=PAYLOAD, RSV=RSV)
                return tmpMessage

            # Set Default opcode as text
            OPCODE = tmpMessage.OPCODEtypes["text"]

            # Configure OPCODE according to the message data type
            b = {'0', '1'}
            t = set(PAYLOAD)
            # Check if the message is binary
            if(b == t or t == {'0'} or t == {'1'}):
                OPCODE = tmpMessage.OPCODEtypes["binary"]

            # Prepare the message to send
            tmpMessage.prepareMessage(
                FIN=FIN, OPCODE=OPCODE, PAYLOAD=PAYLOAD, RSV=RSV)

            return tmpMessage
        except Exception as e:  # Capture exception
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketProtocol.newMessage()")
            traceback.print_exc()
            # Close workflow
            self.keepAlive = False

            return None

    # ================================================================
    # REQUEST AND RESPONSE PROCESSING METHODS

    # Processes the rawdata and sepatates it in a list if messages are fragmented or concatenated
    def processRawData(self, rawdata):
        # Rawdata will be stored here
        parsedRawData = list()

        # Is fragmented
        if(self.fragmented):
            # Append it to the begining of the rawdata
            rawdata = self.fragmentedMessage.rawdata + rawdata
            self.fragmented = False
            self.fragmentedMessage = None

        # Parse websocket headers
        tmpWSMessage = WebSocketMessage().getHeaders(message=rawdata)

        # If is not posible to get the headers
        if (tmpWSMessage == None):
            return [rawdata]

        # If is not valid
        if(tmpWSMessage.frameLen < 1):
            return [rawdata]

        # Concat the first rawdata needed without the fragmented piece
        parsedRawData.append(rawdata[:tmpWSMessage.frameLen])
        rawdata = rawdata[tmpWSMessage.frameLen:]

        # Go rawdata per rawdata until is empty leaving the rest of rawdata to the next connection
        while(rawdata != b''):
            tmpWSMessage = WebSocketMessage().getHeaders(message=rawdata)
            # If there is no message anymore we stop
            if(tmpWSMessage == None):
                break
            parsedRawData.append(rawdata[:tmpWSMessage.frameLen])
            rawdata = rawdata[tmpWSMessage.frameLen:]

        # Return the clean rawdata messages
        return parsedRawData

    # ================================================================
    # INPUT BUFFER

    def processInputBuffer(self):

        try:
            # Check as complete, until is checked incomplete by FIN = 0b0
            incomplete = False
            lenInputBuffer = self.camera.getLenInputBuffer()

            if(lenInputBuffer > 0):

                # Get inputBuffer
                tmpInputBuffer = self.camera.inputBuffer

                for message in tmpInputBuffer:

                    rawMessage = message.parseMessage()

                    # [HTTP] If the handshake is not completed there is no message to process
                    if (self.acceptKey == None) or (not self.handshakeCompleted):

                        # Save Accept Key
                        self.acceptKey = rawMessage.acceptKey
                        # Create response
                        tmpResponse = self.getMessage()
                        # Send the same version of the protocol in response
                        tmpResponse.requestVersion = rawMessage.version
                        # If a subprotocol exists
                        tmpResponse.generateSubprotocolResponse(
                            subprotocol=self.handler.subprotocol, sessionid=self.camera.sessionid)
                        # Generate Handshake
                        tmpResponse.generateHandshake(acceptKey=self.acceptKey)
                        # Clean the Input Buffer
                        self.camera.clearInputBuffer()
                        # Add the handshake response directly to outputbuffer
                        self.camera.addOutputBuffer(
                            value=tmpResponse)  # CONNECTION IS OPENED

                        # Mark handshake as Completed
                        self.handshakeCompleted = True

                        return self.processOutputMessage()

                    # [WebSocket] All the messages from now on will be WebSocketProtocol type

                    # IF OPCODE IS CLOSE, there is no payload to receive
                    if(rawMessage.OPCODE == rawMessage.OPCODEtypes["close"]):
                        op.printLog(
                            logType="INFO", messageStr="Connection with ["+self.camera.cameraid+"] is Closed")
                        self.keepAlive = False
                        return False

                    # IF OPCODE IS PONG, there is no payload to receive
                    if(rawMessage.OPCODE == rawMessage.OPCODEtypes["pong"]):
                        op.printLog(
                            logType="INFO", messageStr="Received Answer from Camera ["+self.camera.cameraid+"]")
                        return True

                    # IF OPCODE IS PING, there is no payload to receive
                    if(rawMessage.OPCODE == rawMessage.OPCODEtypes["ping"]):
                        op.printLog(
                            logType="INFO", messageStr="Received Ping from Camera ["+self.camera.cameraid+"]. Sending pong")
                        tmpMessage = self.newMessage(
                            FIN=1, OPCODE=rawMessage.OPCODEtypes["pong"], PAYLOAD="PONG")
                        # Add the pong response directly to outputbuffer
                        # CONNECTION IS STILL OPENED
                        self.camera.addOutputBuffer(value=tmpMessage)
                        return True

                    # If the message is fragmented
                    if(rawMessage.FIN != 0b1):
                        incomplete = True
                        continue

                    # Check if message is fragmented
                    realPayloadLen = len(rawMessage.PAYLOAD)
                    if(rawMessage.PAYLOAD_LEN != realPayloadLen):
                        op.printLog(logType="DEBUG", messageStr="Message is fragmented! ["+str(
                            realPayloadLen)+"] Bytes Arrived, ["+str(rawMessage.PAYLOAD_LEN-realPayloadLen)+"] Bytes Remaining")
                        self.fragmented = True
                        self.fragmentedMessage = rawMessage
                        self.camera.clearInputBuffer()
                        return True

                    # Get the buffer and add to inputmessage
                    tmpMessage = self.camera.getInputBuffer()
                    # Adds the full message to the list
                    res = self.camera.addInputMessage(value=tmpMessage)
                    if (not res):
                        return res

                # If the message has ended (is not fragmented)
                if(not incomplete):
                    self.camera.clearInputBuffer()

            # If there is no message to send
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketProtocol.processInputBuffer()")
            traceback.print_exc()

            return False

    # ================================================================
    # INPUT MESSAGE

    def processInputMessage(self):
        try:
            # Count the number of messages to send
            tmpInputMessageLen = self.camera.getLenInputMessages()

            # If there are messages to send
            if (tmpInputMessageLen > 0):

                try:
                    # Try to copy the message received
                    tmpInputMessages = copy.deepcopy(self.camera.inputMessages)
                    self.camera.clearInputMessages()
                except Exception:  # In case is imposible to copy the class
                    # Add the original value
                    tmpInputMessages = self.camera.inputMessages

                for inputMessage in tmpInputMessages:

                    # [HINT]: [Add Here you can process the messages you received and create a response]
                    #

                    # [DEFAULT] If there is no response logic send the same payload as we received.
                    PAYLOAD = inputMessage

                    #
                    # #

                    # Create a response [HINT] : [You can personalize how you want]
                    outputMessage = PAYLOAD

                    # Add to the outputMessage list that will be sent
                    res = self.camera.addOutputMessage(value=outputMessage)
                    if (not res):
                        return False

                # Clear output messages
                self.camera.clearInputMessages()

            # If there was messages they will be sent, if not we make nothing
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketProtocol.processInputMessage()")
            traceback.print_exc()

            return False

    # ================================================================
    # OUTPUT MESSAGE

    def processOutputMessage(self):
        try:
            # If the Camera is offline we dont add the messages to the OutputBuffer
            if (self.camera.status == "ONLINE"):
                # Count the number of messages to send
                tmpOutputMessagesLen = self.camera.getLenOutputMessages()

                if (tmpOutputMessagesLen > 0):

                    try:
                        # In case is imposible to copy the class
                        tmpOutputMessages = copy.deepcopy(
                            self.camera.outputMessages)
                        self.camera.clearOutputMessages()
                    except Exception:
                        # Add the original value
                        tmpOutputMessages = self.camera.outputMessages

                    for outputMessage in tmpOutputMessages:

                        # If the output Message is a String we add it into a payload.
                        # In case the output message is binary, the OPCODE will be modified
                        rawOutputMessage = self.newMessage(
                            FIN=0b1, PAYLOAD=outputMessage)

                        res = self.camera.addOutputBuffer(
                            value=rawOutputMessage)
                        if (not res):
                            # If there is an error
                            return False

                self.camera.clearOutputMessages()

            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketProtocol.processOutputMessage()")
            traceback.print_exc()
            return False

# ================================================================
# WEBSOCKET PROTOCOL MESSAGES
# ================================================================


class WebSocketMessage(Message):
    """
    # Web Socket Message

    inherits from ```Message```

    Description ::
    ---------- 

    Defines the structure of Web Socket protocol message frame.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    Attributes ::
    ----------

    :attr bytes firstByte: Stores frame first byte [8 Bits | 1 Byte]

    :attr bytes secondByte: Stores frame second byte [8 Bits | 1 Byte]

    :attr bin FIN: Stores first bit (indicates if is the end of the frame) [1 Bit]

    :attr list(bin) RSV: Stores next three bits (used for extentions) [3 Bits]

    :attr hex OPCODE: Indicates the type of frame [8 Bits | 1 Byte]

    :attr dict OPCODEtypes: Indicates the frame types

    :attr dict OPCODEnames: Indicates the frame names

    :attr bin MASK: Stores mask bit (indicates if frame is masked) [1 Bit]

    :attr int PAYLOAD_LEN: Indicates the LENGHT of a frame payload

    :attr bytes MASKING_KEY: If MASK is equal to 1 here we store the masking key

    :attr str PAYLOAD: Here we store the content/message from the WebSocket Frame

    :attr str masked_payload_data: Contains the masked data

    :attr str unmasked_payload_data: Contains the unmasked data without parsing the payload

    :attr str frameLen: Indicates the total frameLen

    :attr str tmppayload_len: Indicates the incoming payloadlen

    :attr str payload_len_size: Indicates the size of the payload (is not the bytes lenght)

    :attr str masking_key_len: Indicates the masking key len

    :attr str offset: # Indicates the actual location while reading the bytes array

    :attr str masking_key_offset: # Indicates where is the mask located by default 4

    :attr str payload_offset: # Indicates where is the payload located by default 6

    [More Attributes can be added]

    """

    def __init__(self, rawdata=None):
        super().__init__(rawdata=rawdata)
        # Buffer Bytes
        self.firstByte = b""
        self.secondByte = b""

        # --------------------
        # START OF WS FRAME STRUCTURE
        # --------------------

        # Structure of the Frame Header
        self.FIN = 0b1
        self.RSV = [0b0, 0b0, 0b0]  # Store RSV in a list
        self.OPCODE = 0x0
        self.OPCODEtypes = {"continuation": 0x0, "text": 0x1, "binary": 0x2,
                            "close": 0x8, "ping": 0x9, "pong": 0xA}  # Opcode types
        self.OPCODEnames = {y: x for x, y in self.OPCODEtypes.items()}
        self.MASK = 0b0
        self.PAYLOAD_LEN = -1

        # Structure of the Frame Extended
        self.MASKING_KEY = b""
        self.PAYLOAD = ""

        # --------------------
        # END OF WS FRAME STRUCTURE
        # --------------------

        # Un/Masked Payloads
        self.masked_payload_data = ""
        self.unmasked_payload_data = ""

        # Payload Lenght
        self.frameLen = 0
        self.tmppayload_len = 0
        self.payload_len_size = 0  # 0 bits, 16 bits, 64 bits

        # Masking key
        self.masking_key_len = 4  # The mask is always 4 bytes (32 bits)

        # Offsets
        self.offset = 0
        # 4 Bits of Masking Key from 2 -> Masking_key_Len by default
        self.masking_key_offset = 2
        self.payload_offset = 6  # Payload Len Bits of Payload from 6 -> Payload_Len by default

    # WebSocket Prepare Message Method
    def prepareMessage(self, FIN=0b1, OPCODE=0x1, PAYLOAD="Hay, Camera!", RSV=[]):
        try:
            # Calculate the number of reserved bits set
            rsvlen = len(RSV)
            # The esencial bits must be set to prepare the message
            if(OPCODE == 0b0 or rsvlen > 3 or OPCODE not in self.OPCODEtypes.values()):
                return None

            # Set FIN bit
            self.FIN = FIN

            # Add rsv bits
            for i, rsv in enumerate(RSV):
                self.RSV[i] = rsv

            # Set opcode
            self.OPCODE = OPCODE

            # Set mask to 0
            self.MASK = 0b0

            # Add payload data
            self.PAYLOAD = PAYLOAD

            # Calculate payload len
            self.PAYLOAD_LEN = len(self.PAYLOAD)
            return True

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketMessage.prepareMessage()")
            traceback.print_exc()
            return False

    # WebSocket Getting the headers
    def getHeaders(self, message=None):
        try:
            # If message is not available
            if message != None:
                self.rawdata = message

            # Get first byte
            self.firstByte = self.rawdata[0]
            ## If is not valid or empty
            if self.firstByte == b"" or self.firstByte == None or self.firstByte == "":  # If the first byte is empty
                return None

            # Get second byte
            self.secondByte = self.rawdata[1]  # Get Second Byte

            # Get the first bits
            self.FIN = (self.firstByte >> 7) & 0b1
            self.RSV[0] = (self.firstByte >> 6) & 0b1
            self.RSV[1] = (self.firstByte >> 5) & 0b1
            self.RSV[2] = (self.firstByte >> 4) & 0b1

            # Get the code from messages with total byte
            # Get 4 bits (fbyte>>0 & 0b1111) the rest of the information
            self.OPCODE = self.firstByte & 0b1111
            if (message == None):
                op.printLog(
                    logType="DEBUG", messageStr="WebSocketMessage.getHeaders(): Incomming WS Message type [" + self.OPCODEnames[int(self.OPCODE)] + "].")

            # Get Mask
            # Get first bit from 1 byte
            self.MASK = (self.secondByte >> 7) & 0b1
            if not self.MASK:  # As defined in the documentation the MASK bit must be set to 1: https://datatracker.ietf.org/doc/html/rfc6455#section-5.2
                return None

            # Get payload len
            # 7F == 127 bits In the second byte we verify the lenght can be (X<125,X==126,X==127)
            self.PAYLOAD_LEN = self.secondByte & 0x7F

            # Get position of payload
            self.payload_offset = self.getPayloadLen()
            if(self.payload_offset == None):
                return None

            # Get the total frame len
            self.frameLen = self.payload_offset + self.masking_key_len + self.PAYLOAD_LEN

            return self
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketMessage.getHeaders(rawdata)")
            traceback.print_exc()

            return None

    # Parse a buffer of bytes into a WebSocketFrame structure
    def parseMessage(self):
        try:
            # Get headers
            self.getHeaders()
            self.getMaskingKey()

            # Get the payload
            payload = self.getPayload()
            if payload == None:
                payload = ""

            # Get the payload
            self.PAYLOAD = payload
            op.printLog(
                logType="DEBUG", messageStr="WebSocketMessage.parseMessage(): WS Payload received LEN = ["+str(self.PAYLOAD_LEN)+"]")

            return self
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketMessage.parseMessage(rawdata)")
            traceback.print_exc()

            return None

    # Gets the payload from a buffer of bytes if the structure is defined

    def getPayload(self):

        # If the offset is invalid
        if(self.offset == 0 or self.PAYLOAD_LEN == -1):
            return None

        # Get payload data
        self.masked_payload_data = self.rawdata[self.offset:self.PAYLOAD_LEN+self.offset]

        # Un Mask the payload
        self.unmasked_payload_data = self.unMaskPayload(
            masked_payload_data=self.masked_payload_data)

        # Update offset
        self.offset = self.PAYLOAD_LEN+self.offset

        return self.unmasked_payload_data

    # Gets the masking key from a buffer of bytes if the structure is defined
    def getMaskingKey(self):

        # Calculate new offset [DEFAULT = 4]
        tmpOffset = self.payload_offset + self.masking_key_len

        # Get the Masking Key and store in the Structure [DEFAULT [2:4]]
        self.MASKING_KEY = self.rawdata[self.payload_offset:tmpOffset]

        # Move the offset to a new position
        self.offset = tmpOffset

    # Gets the payload lenght from a buffer of bytes if the structure is defined
    def getPayloadLen(self):

        # If a payload len is not defined or is INVALID
        if (self.PAYLOAD_LEN < 0 or self.PAYLOAD_LEN > 127):
            return None

        # If payload is less than 126, execute default settings
        if (self.PAYLOAD_LEN < 126):
            self.offset = self.masking_key_offset
            self.payload_len_size = 7
            return self.offset

        # If payload is equal to 126 set properties and get payload_len
        if (self.PAYLOAD_LEN == 126):
            self.offset = 4
            self.payload_len_size = 16
            self.PAYLOAD_LEN = struct.unpack('!H', self.rawdata[2:self.offset])[
                0]  # GET Unsigned short int EXTRA 16 bits
            return self.offset

        # If payload is igual to 127 set properties and get payload_len
        self.offset = 10
        self.payload_len_size = 64
        self.PAYLOAD_LEN = struct.unpack('!Q', self.rawdata[2:self.offset])[
            0]  # GET Unsigned long long EXTRA 64 bits

        return self.offset

        # Un mask the payload passed by parameter

    # Unmasks the payload that comes from Camera using the masking key
    def unMaskPayload(self, masked_payload_data):

        # As defined in the documentation the MASK bit must be set to 1: https://datatracker.ietf.org/doc/html/rfc6455#section-5.2
        if self.MASK == 0b0:
            return None

        message = b""
        for octet, original_octet_i in enumerate(masked_payload_data):
            # i mod 4
            j = octet % 4
            # XOR from original octet and mask as defined in protocol: https://datatracker.ietf.org/doc/html/rfc6455#section-5.3
            transformed_octet_i = chr(original_octet_i ^ self.MASKING_KEY[j])
            chrbytes = transformed_octet_i.encode("utf-8")
            message += chrbytes

        strmessage = str(message, 'utf-8')

        return strmessage

    # Compact the frame attributes into a byte stream
    def messageToBytes(self):

        self.extendedPayloadLen = b""

        # In case the payload is less than the reserved bits, we send the original len
        if(self.PAYLOAD_LEN < 126):

            tmpPayloadLen = "{:07b}".format(self.PAYLOAD_LEN)

        # In case the payload is more than the reserved bits but less than 16 bits, we send 126 (7bits) + 16 bits
        if(self.PAYLOAD_LEN >= 126 and self.PAYLOAD_LEN <= 65535):

            tmpPayloadLen = "{:07b}".format(126)
            self.extendedPayloadLen = struct.pack(
                "!H", self.PAYLOAD_LEN)  # Unsigned Short

        # In case the payload is more than the reserved bits but less than 16 bits, we send 127 (7bits) + 64 bits
        if(self.PAYLOAD_LEN > 65535):

            tmpPayloadLen = "{:07b}".format(127)
            self.extendedPayloadLen = struct.pack(
                "!Q", self.PAYLOAD_LEN)  # Unsigned Long Long

        # Concat the first bytes
        self.firstByte = str(
            self.FIN) + str(''.join(map(str, self.RSV))) + "{:04b}".format(self.OPCODE)
        self.secondByte = str(self.MASK) + str(tmpPayloadLen)

        # Concat the extra bytes
        self.otherBytes = b"".join([self.MASKING_KEY, self.extendedPayloadLen])

        self.content = b"".join([struct.pack("!B", int(self.firstByte, 2)), struct.pack(
            "!B", int(self.secondByte, 2)), self.otherBytes, bytes(self.PAYLOAD, "utf-8")])

        return super().messageToBytes()


class WebSocketHTTPResponse(HTTPMessage):
    """
    # Web Socket HTTP Response Message

    inherits from ```HTTPMessage```

    Description ::
    ---------- 

    Defines the structure of WebSocket HTTP protocol response message.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    Attributes ::
    ----------

    :attr str|bytes acceptKey: Contains the WebSocket response acceptkey

    :attr str WebSocketAcceptKeyHeaderName: Accept key HTTP field name

    :attr dict WebSocketSubprotocolHeaderName: Sub protocol HTTP field name

    :attr str subprotocol: Subprotocol used (can be SJMP)

    :attr str subprotocolResponse: Subprotocol response

    :attr str requestVersion: Version Comming in the request

    """

    def __init__(self, rawdata=None):
        super().__init__(rawdata=rawdata)
        self.acceptKey = None
        # Standard Headers Names from WebSocket Response
        self.WebSocketAcceptKeyHeaderName = "Sec-WebSocket-Accept"
        self.WebSocketSubprotocolHeaderName = "Sec-WebSocket-Protocol"
        self.subprotocol = None
        self.subprotocolResponse = None
        self.requestVersion = ""

    # Generate the subprotocol response

    def generateSubprotocolResponse(self, subprotocol=None, sessionid=None):
        # Sub protocol configuration

        # If in the handshake we include a subprotocol we must return it
        if(subprotocol != None):
            self.subprotocol = subprotocol

        # [HINT] If you want to add the response logic for your subprotocol add it here.
        # --------------------------------
        #  Example of Response
        #  if self.subprotocol == "Chat":
        #      self.subprotocolResponse = "Welcome Camera!"
        #      return
        # --------------------------------
        return

    # Generate the handshake
    def generateHandshake(self, acceptKey=None):
        # Store acceptKey and protocolResponse
        self.acceptKey = acceptKey
        tmpHeaders = {}

        if(self.requestVersion == ""):
            self.requestVersion = "1.1"

        if(self.subprotocol != None):
            # Define Subprotocol Language
            tmpHeaders[self.WebSocketSubprotocolHeaderName] = self.subprotocol

        if(self.subprotocolResponse != None):
            # Send SubProtocol Response in body
            tmpBodyResponse = WebSocketMessage()
            tmpBodyResponse.prepareMessage(PAYLOAD=self.subprotocolResponse)

        # If the acceptKey was not created
        if self.acceptKey == None:
            self.prepareMessage(code=400, message="Bad Request")
            return False

        tmpHeaders["Connection"] = "Upgrade"
        # Return AcceptKey
        tmpHeaders[self.WebSocketAcceptKeyHeaderName] = self.acceptKey
        # Create the response headers
        tmpHeaders["Upgrade"] = "websocket"

        self.prepareMessage(version=self.requestVersion, code=101, message="Switching Protocols",
                            responseHeaders=tmpHeaders, responseBody=tmpBodyResponse.messageToBytes())


class WebSocketHTTPRequest(HTTPMessage):
    """
    # Web Socket HTTP Request Message

    inherits from ```HTTPMessage```

    Description ::
    ---------- 

    Defines the structure of WebSocket HTTP protocol response message.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    Attributes ::
    ----------

    :attr str|bytes acceptKey: Contains the WebSocket response acceptkey

    :attr str WebSocketAcceptKeyHeaderName: Accept key HTTP field name

    :attr dict WebSocketSubprotocolHeaderName: Sub protocol HTTP field name

    :attr str subprotocol: Subprotocol used (can be SJMP)

    :attr str subprotocolList: Subprotocol content

    :attr int lenSubprotocolList: Subprotocol content len

    :attr bytes GUID: Indicates the control string of Web Socket to generate accept key

    [More attributes are used to store information of acceptKey]

    """

    def __init__(self, rawdata=None):
        super().__init__(rawdata=rawdata)
        self.WebSocketKeyHeaderName = "Sec-WebSocket-Key"
        self.WebSocketSubprotocolHeaderName = "Sec-WebSocket-Protocol"
        self.GUID = b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        self.acceptKey = None
        self.deviceTime = None
        self.key = None
        self.hash = None
        self.subprotocol = None
        self.clearAcceptKey = None
        self.subprotocolList = None
        self.lenSubprotocolList = 0

    # Parse from internal rawbytes in rawdata and generate acceptkey
    def parseMessage(self):
        super().parseMessage()
        self.generateProtocolList()
        self.generateAcceptKey()
        return self

    # Get the content included in websocket headers protocol field
    def generateProtocolList(self):
        try:
            if not (self.WebSocketSubprotocolHeaderName in self.headers):
                return

            self.subprotocolList = self.headers[self.WebSocketSubprotocolHeaderName].replace(
                ", ", ",").split(",")
            self.lenSubprotocolList = len(self.subprotocolList)

            # If the header is empty
            if not (self.lenSubprotocolList > 0):
                return

            self.subprotocol = self.subprotocolList[0].upper()
            return

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="WebSocketHTTPRequest.generateProtocolList()")
            traceback.print_exc()
            return

    # Generate the acceptkey
    def generateAcceptKey(self):
        self.key = self.headers.get(self.WebSocketKeyHeaderName, None)
        if self.key == None:
            return None
        # Concat with key in bytes
        self.clearAcceptKey = bytes(self.key, 'utf-8') + self.GUID
        # Digest in sha1hash
        self.hash = hashlib.sha1(self.clearAcceptKey).hexdigest()
        # Base64 encode
        self.acceptKey = base64.b64encode(
            bytes.fromhex(self.hash)).decode('utf-8')
        return self.acceptKey
