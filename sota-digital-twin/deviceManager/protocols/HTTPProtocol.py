# coding=UTF-8
import traceback
from operators.op import op
from protocols.Protocol import Message
from protocols.TCPProtocol import TCPProtocol
import copy


class HTTPProtocol(TCPProtocol):
    """
    # HTTP Protocol

    Input ::
    -----

    :attr int buffer: Defines the amount of data that is received by the socket.

    Description ::
    -----------

    Defines the work flow and treatment of the information using http.

    """

    def __init__(self, buffer=2048):
        super().__init__(buffer=buffer)

    # ================================================================
    # MESSAGE HANDLE METHODS

    # Returns the message type and configures the request
    def getMessage(self, input=None):
        # Gets the protocol message type
        return HTTPMessage(rawdata=input)

    # Prepares and returns a close message
    def getCloseMessage(self):

        return self.newMessage(code="1000", message="close", responseHeaders={"Connection": "keep-alive, close"})

    # Prepares the a new message with a desired structure of the protocol including the data passed as params
    # (Return None if fails and the message object configured if not)
    def newMessage(self, version="1.1", code="200", message="OK", responseBody="", responseHeaders={}):
        tmpHTTPResponse = HTTPMessage()
        tmpHTTPResponse.prepareMessage(version=version, code=code, message=message,
                                       responseBody=responseBody, responseHeaders=responseHeaders)

        return tmpHTTPResponse

    # ================================================================
    # REQUEST AND RESPONSE PROCESSING METHODS

    # Processes the rawdata and sepatates it in a list if messages are fragmented or concatenated
    def processRawData(self, rawdata):
        """OVERRIDE THIS METHOD WITH DESIRED HTTP FRAGMENTATION STRUCTURE"""

        return super().processRawData(rawdata=rawdata)

    # ================================================================
    # INPUT BUFFER

    def processInputBuffer(self):
        try:
            # Get the len of Buffer
            lenInputBuffer = self.camera.getLenInputBuffer()

            ## If is not empty
            if(lenInputBuffer > 0):

                # Get inputBuffer
                tmpInputBuffer = self.camera.inputBuffer

                # Go message per message
                for message in tmpInputBuffer:
                    # Parse message with message structure
                    rawMessage = message.parseMessage()

                    # [HINT]: [Implement here your logic if the message is fragmented]
                    #
                    # #

                    # ADD MESSAGE CONTENT TO INPUT MESSAGE
                    res = self.camera.addInputMessage(value=rawMessage.body)
                    # If there is a error
                    if (not res):
                        return res

                # Clear input buffer
                self.camera.clearInputBuffer()

            # If everything is allright return true
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\HTTPProtocol.processInputBuffer()")
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
                    outputMessage = ""
                    # [DEFAULT] If there is no response logic send the same payload as we received.

                    if(inputMessage != None and inputMessage != ""):
                        # Create a response [HINT] : [You can personalize how you want]
                        outputMessage = inputMessage

                    # If we not want to return messages
                    if (outputMessage == None):
                        continue

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
                        messageStr="BaseProtocol.processInputMessage()")
            traceback.print_exc()

            return False

    # ================================================================
    # OUTPUT MESSAGE

    def processOutputMessage(self):
        try:

            # [HINT]: [Implement here your logic if you need to encode the output information]
            #
            # #
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

                        # [HINT] Modify here the parameters to send a different response
                        #
                        tmpCode = "200"
                        tmpStatus = "OK"
                        tmpResponseBody = outputMessage  # Send the message back
                        # Here you can configure the parameters to send in the headerresponse
                        tmpResponseHeaders = {}
                        #
                        ##

                        rawOutputMessage = self.newMessage(
                            code=tmpCode, message=tmpStatus, responseBody=tmpResponseBody, responseHeaders=tmpResponseHeaders)

                        res = self.camera.addOutputBuffer(
                            value=rawOutputMessage)
                        if (not res):
                            # If there is an error
                            return False

                self.camera.clearOutputMessages()

            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="HTTPProtocol.processOutputMessage()")
            traceback.print_exc()

            return False

# ================================================================
# HTTP PROTOCOL MESSAGES
# ================================================================


class HTTPMessage(Message):
    """
    # HTTP Message

    inherits from ```Message```

    ```Abstract Class```

    Description ::
    ---------- 

    Defines the structure of HTTP protocol message.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    Attributes ::
    ----------

    :attr str LINE_SEP: HTTP line separator

    :attr dict headers: HTTP headers

    :attr str body: HTTP body

    :attr str protocolName: HTTP is the name of the protocol

    :attr str version: The version of the protocol

    :attr int statusCode: HTTP status code of response.

    :attr str statusMessage: HTTP is the name of the protocol

    :attr str context: HTTP context

    :attr str methods: HTTP allowed methods

    :attr str method: HTTP message method

    [More Attributes can be added]

    """

    def __init__(self, rawdata=None):
        super().__init__(rawdata=rawdata)
        self.LINE_SEP = "\r\n"
        self.headers = dict()
        self.body = ""
        self.protocolName = "HTTP"
        self.version = "1.1"
        self.method = ""
        self.context = ""
        self.methods = ["GET", "POST"]
        self.statusCode = 200
        self.statusMessage = "OK"

    # Converts the headers in string
    def headersToString(self):
        tmpString = ""
        for tmpKey in self.headers:
            tmpString = tmpString+self.LINE_SEP + \
                tmpKey+": "+self.headers[tmpKey]
        return tmpString

    # HTTP Prepare Message Method
    def prepareMessage(self, version="1.1", code="200", message="OK", responseBody="", responseHeaders={}):
        self.statusCode = code
        self.version = version
        self.statusMessage = message
        self.headers = responseHeaders
        self.body = responseBody
        return True

    # Pass HTTPMessage to Bytes
    def messageToBytes(self):
        tmpMessage = self.protocolName+"/"+self.version + " " + \
            str(self.statusCode) + " " + self.statusMessage + \
            self.headersToString() + self.LINE_SEP*2
        if(type(self.body) == str):
            self.content = tmpMessage+self.body
        else:
            self.content = b''.join([bytes(tmpMessage, "utf-8"), self.body])

        return super().messageToBytes()

    # Parse from internal rawbytes in rawdata

    def parseMessage(self):
        try:
            # Loads the data in the structre
            return self.loadData(data=self.rawdata)
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="BaseHTTPMessage.parseMessage()")
            traceback.print_exc()
            return self

    # Loads data into the structure from rawdata or a external data.
    def loadData(self, data):
        # Parse to string
        if(type(data) != str):
            data = str(data, "utf-8")
        # Check if in the valid methods list
        method = data[0:3].upper()

        # Check if the method is in the list of valid methods
        if not method in self.methods:
            return None

        # Devide the request
        splited_request = data.split(self.LINE_SEP*2)

        # If there less than two blocks
        tmpRequestBlocks = len(splited_request)
        if(tmpRequestBlocks < 2):
            return None

        # Get headers
        headers_lines = splited_request[0].split(self.LINE_SEP)

        # Get fist line
        operationLine = headers_lines.pop(0)

        # Parse First line:
        definition = operationLine.split(" ")

        # Save header info
        self.method = definition[0]
        self.context = definition[1]
        self.protocolName, self.version = definition[2].split("/")

        # Parse all lines:
        tmpHeadersLen = len(headers_lines)
        count = 0
        while(tmpHeadersLen > count):
            tmpHeaderLineParts = headers_lines[count].split(": ")
            self.headers[tmpHeaderLineParts[0]] = tmpHeaderLineParts[1]
            count += 1

        # If the message has more than two elements, it comes with a body
        if(tmpRequestBlocks == 3):
            self.body = splited_request[1]

        return self
