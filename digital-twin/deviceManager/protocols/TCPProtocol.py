# coding=UTF-8
import traceback
from operators.op import op
import copy
from datetime import datetime, timezone

from protocols.Protocol import Protocol, Message


class TCPProtocol(Protocol):
    """
    # TCP Protocol

    inherits from ```Protocol```

    Description ::
    -----------

    Defines the work flow and treatment of the information in TCP.

    Input ::
    -----

    :attr int buffer: Defines the amount of data that is received by the socket.

    Attributes ::
    ----------

    :attr str EOF: Message Separator for TCP

    :attr bool fragmented: Indicates if processed message is fragmented

    :attr bytes fragmentedMessage: Contains the fragmented content

    """

    def __init__(self, buffer=2048):
        super().__init__(buffer=buffer)
        self.EOF = b'\0n'  # End of the message character
        self.fragmented = False
        self.fragmentedMessage = None

    # ================================================================
    # MESSAGE HANDLE METHODS

    # Returns the message type and configures the request
    def getMessage(self, input=None):
        return TCPMessage(rawdata=input)

    # Prepares and returns a connection message
    def getConnectionMessage(self, cameraid):
        return self.newMessage(content="message=Hello, Server! Connection Requested.;cameraid="+str(cameraid)+";clt-time="+str(datetime.timestamp(datetime.now(timezone.utc))))

    # Prepares and returns a close message
    def getCloseMessage(self):
        return self.newMessage(content="Connection Closed! Server shutdown")

    # Prepares the a new message with a desired structure of the protocol including the data passed as params
    # (Return None if fails and the message object configured if not)
    def newMessage(self, content=""):
        try:
            tmpMessage = TCPMessage()
            tmpMessage.prepareMessage(data=content)

            return tmpMessage
        except Exception as e:  # Capture exception
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="TCPProtocol.newMessage()")
            traceback.print_exc()
            # Close workflow
            self.keepAlive = False

            return None

    # ================================================================
    # REQUEST AND RESPONSE PROCESSING METHODS

    # Processes the rawdata and sepatates it in a list if messages are fragmented or concatenated
    def processRawData(self, rawdata):
        # Is fragmented
        if(self.fragmented):
            # Append it to the begining of the rawdata
            rawdata = self.fragmentedMessage + rawdata
            self.fragmented = False
            self.fragmentedMessage = None

        # Split the rawdata using the end of message character
        parsedRawData = rawdata.split(self.EOF)
        lenParsedData = len(parsedRawData)
        if(lenParsedData < 2):
            return [rawdata]

        tmpLastElement = parsedRawData.pop()
        if(tmpLastElement != b''):
            self.fragmented = True
            self.fragmentedMessage = tmpLastElement

        return parsedRawData

    # ================================================================
    # INPUT MESSAGE

    def processInputMessage(self):
        try:

            # [HINT]: [Implement here your logic if you need to treat the incoming information]
            #
            # #
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

                    tmpOutputMessage = None

                    # Generate a output or not depending in message sent

                    # EXAMPLE ==========================================================
                    # Example of one posibility of structured message Format

                    tmpElements = inputMessage.split(";")
                    lenElements = len(tmpElements)
                    if (lenElements == 0):
                        continue

                    elements = {}
                    for element in tmpElements:
                        tmpKeyData = element.split("=")
                        lenKeyData = len(tmpKeyData)
                        if(lenKeyData == 2):
                            elements[tmpKeyData[0]] = tmpKeyData[1]

                    # Identify message type by default messages, message must exist
                    if("message" not in elements):
                        continue

                    if("cameraid" in elements):
                        self.camera.cameraid = elements["cameraid"]

                    # Just return handshake
                    if(elements["message"] == "Hello, Server!"):
                        tmpOutputMessage = "message=Welcome Camera!;sessionid=" + \
                            str(self.camera.sessionid)+";srv-time=" + \
                            str(datetime.timestamp(datetime.now(timezone.utc)))
                    elif(elements["message"] == "Welcome Camera!"):
                        self.camera.sessionid = elements["sessionid"]
                        self.camera.status = "ONLINE"
                        op.printLog(logType="DEBUG", messageStr="Camera ["+self.camera.cameraid+"] status [" +
                                    self.camera.status+"] logged in with sessionid = ["+self.camera.sessionid+"] in ["+self.camera.serverkey+"].")
                        tmpOutputMessage = None

                    # EXAMPLE ==========================================================

                    # If we not need to return information to the Camera
                    if (tmpOutputMessage == None):
                        continue

                    res = self.camera.addOutputMessage(value=tmpOutputMessage)
                    if (not res):
                        return False

                # Clear output messages
                self.camera.clearInputMessages()

            # If there was messages they will be sent, if not we make nothing
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="TCPProtocol.processInputMessage()")
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
            if (self.camera.status == "ONLINE" or self.camera.status == "CONNECTED"):
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

                        rawOutputMessage = self.newMessage(
                            content=outputMessage)

                        res = self.camera.addOutputBuffer(
                            value=rawOutputMessage)
                        if (not res):
                            # If there is an error
                            return False

                self.camera.clearOutputMessages()

            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="TCPProtocol.processOutputMessage()")
            traceback.print_exc()

            return False

    # ================================================================
    # OUTPUT BUFFER

    def processOutputBuffer(self):
        try:

            # [HINT]: [Implement here your logic if you need to send the output information]
            #
            # #
            # [EXAMPLE OF GENERIC SEND USING OUTPUTBUFFER]
            while self.camera.getLenOutputBuffer() > 0:
                tmpResponse = self.camera.outputBuffer.pop(0)
                tmpResponseBytes = tmpResponse.messageToBytes()
                self.request.send(tmpResponseBytes+self.EOF)

            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="TCPProtocol.processOutputBuffer()")
            traceback.print_exc()

            return False

# ================================================================
# TCP PROTOCOL MESSAGES
# ================================================================


class TCPMessage(Message):
    """
    # TCP Message

    inherits from ```Message```

    Description ::
    ---------- 

    Defines the structure of TCP protocol message.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.
    [More Attributes can be added]

    """

    def __init__(self, rawdata=None):
        super().__init__(rawdata=rawdata)

    # Base Prepare Message Method
    def prepareMessage(self, data="Hay, Camera!"):
        self.content = data
        return True

    # Standad TCP Parse Message Method
    def parseMessage(self):
        try:
            self.content = self.rawdata
            return self
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="TCPMessage.parseMessage()")
            traceback.print_exc()
            return None
