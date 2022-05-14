# coding=UTF-8
import traceback
from operators.op import op
from datetime import datetime, timezone
import copy


class Protocol():
    """
    # Base Protocol

    ```Abstract Class```

    Description ::
    -----------

    Defines the work flow and treatment of the information.
    This class can be overrided.

    Input ::
    -----

    :attr int buffer: Defines the amount of data that is received by the socket.

    Attributes ::
    ----------

    :attr object handler: Contains the logic to handle the connection flow.

    :attr object server: Contains the server object (if is available).

    :attr object Camera: Contains the Camera object .

    :attr socket.socket request: Contains the connection socket object.

    :attr bytes rawdata: Contains the rawdata incoming from the socket flow.

    :attr bytes list preProcessedData: List of bytes received and separated if they are concatenated

    :attr bool keepAlive: Connection status variable

    :attr bool processStatus: Processing status variable (If true the process has worked)

    """

    def __init__(self, buffer=2048):
        # Definition of the arguments used by the protocol.
        self.handler = None

        ## Server and Camera
        self.server = None
        self.camera = None

        # Request socket
        self.request = None
        self.buffer = buffer

        # Received data
        self.rawdata = None
        self.preProcessedData = None

        # Keep Alive
        self.keepAlive = False
        self.processStatus = False

    # ================================================================
    # MESSAGE HANDLE METHODS

    # Returns the message type and configures the request
    def getMessage(self, input=None):
        """MAY BE OVERRIDED WITH DESIRED MESSAGE"""

        return Message(rawdata=input)

    # Prepares and returns a connection message
    def getConnectionMessage(self):
        """MAY BE OVERRIDED WITH DESIRED MESSAGE STRUCTURE TO CONNECT"""

        return self.newMessage(content="Hallo Server! Connection Requested.")

    # Prepares and returns a close message
    def getCloseMessage(self):
        """MAY BE OVERRIDED WITH DESIRED MESSAGE STRUCTURE TO SHUTDOWN"""

        return self.newMessage(content="Server is Shutdown")

    # Prepares the a new message with a desired structure of the protocol including the data passed as params
    # (Return None if fails and the message object configured if not)
    def newMessage(self, content=""):
        """MAY BE OVERRIDED WITH DESIRED MESSAGE CREATION STRUCTURE"""
        try:
            # Create a tempory message in the protocol structure
            tmpMessage = Message()

            # HINT: Do here what you need to do to create the message

            # Pass as parameters here the arguments that contains your message
            tmpMessage.prepareMessage(message=content)

            return tmpMessage
        except Exception as e:  # Capture exception
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\nBaseProtocol.newMessage()")
            traceback.print_exc()
            # Close workflow
            self.keepAlive = False

            return None

    # ================================================================
    # REQUEST AND RESPONSE PROCESSING METHODS

    # Processes the rawdata and sepatates it in a list if messages are fragmented or concatenated
    def processRawData(self, rawdata):
        """OVERRIDE THIS METHOD WITH DESIRED RAWDATA FRAGMENTATION STRUCTURE"""
        return [rawdata]

    # Loads a request received from handler
    def loadRequest(self, handler):
        """DON'T OVERRIDE THIS METHOD"""

        # Store handler
        self.handler = handler
        # Declare the status not finished
        self.processStatus = False
        try:
            # Check if server exists and store it
            if (self.handler.server != None):
                self.server = self.handler.server

            # Store Camera and the connection socket
            self.camera = self.handler.camera

            if(self.camera == None):
                op.printLog(
                    logType="CRITICAL", messageStr="No Camera is being used in the connection!")
                self.handler.keepAlive = False
                # Close request
                return self.closeRequest()

            self.request = self.handler.request

            # If the handler has already identified the connection type we must process it.
            if self.handler.connectionData == None:
                # Store the socket incoming data
                self.rawdata = self.request.recv(self.buffer)
            else:
                self.rawdata = self.handler.connectionData  # Store the connection data

            # If we receive no message we shall wait
            if (self.rawdata == "" or self.rawdata == b''):
                return self.closeRequest()  # Close request because rawdata is empty

            # -----------------------------------------
            # MESSAGE RECEIVED, RAWDATA IS NOT EMPTY

            # Store the current timestamp
            self.handler.messageRecievedTimestamp = datetime.now(timezone.utc)

            # Pre processes the rawdata with protocol structure passing byteinput to a list of bytes
            self.preProcessedMessages = self.processRawData(
                rawdata=self.rawdata)

            # Get each message and add it to the Camera inputBuffer
            for rawdata in self.preProcessedMessages:
                # Set that the message received has been processed (control)
                self.handler.messagesProcessed += 1

                # Generate a message object containing the information in bytes
                tmpMessage = self.getMessage(input=rawdata)

                # ADD MESSAGE TO INPUT BUFFER
                # Message will be processed
                self.processStatus = self.camera.addInputBuffer(
                    value=tmpMessage)
                # If was not posible to process the Message
                if (not self.processStatus):
                    # If there was a error in the process
                    self.handler.keepAlive = False
                    op.printLog(
                        logType="CRITICAL", messageStr="Was not posible to process rawdata. BaseProtocol.loadRequest()")
                    traceback.print_exc()

            # Close request
            return self.closeRequest()
        except Exception as e:
            op.printLog(logType="DEBUG", e=e,
                        messageStr="BaseProtocol.loadRequest(request)")
            self.handler.keepAlive = False  # Close connection

        # Close request
        return self.closeRequest()

    # Closes the connection and clears the variables
    def closeRequest(self):
        """DON'T OVERRIDE THIS METHOD"""
        try:
            # Clear the entrance variables
            self.rawdata = None
            self.handler.connectionData = None
            # Return updated handler
            return self.handler
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="BaseProtocol.closeRequest()")
            traceback.print_exc()
            self.handler.keepAlive = False  # Close connection
            # Return updated handler
            return self.handler

    # If the connection is open in handler, and we have no acces to it we can use finish to close and stop processing
    def finish(self):
        # Close handler
        self.handler.keepAlive = False
        return True

    # ================================================================
    # INPUT BUFFER

    def processInputBuffer(self):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL INPUT/REQUEST BYTES HANDLING PROCESS"""

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
                    res = self.camera.addInputMessage(value=rawMessage.content)
                    # If there is a error
                    if (not res):
                        return res

                # Clear input buffer
                self.camera.clearInputBuffer()

            # If everything is allright return true
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\nBaseProtocol.processInputBuffer()")
            traceback.print_exc()

            return False

    # ================================================================
    # INPUT MESSAGE

    def processInputMessage(self):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL INPUT/REQUEST MESSAGE HANDLING PROCESS"""

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

                    # [HINT]: [Add Here you can process the messages you received and create a response]
                    #

                    # [DEFAULT] If there is no response logic send the same payload as we received.
                    message = inputMessage

                    #
                    # #

                    # Create a response [HINT] : [You can personalize how you want]
                    outputMessage = message

                    # If we not want to return messages
                    if (outputMessage == None):
                        continue

                    # ADD TO OUTPUT MESSAGE
                    res = self.camera.addOutputMessage(value=outputMessage)
                    if (not res):
                        return res

                # Clear output messages
                self.camera.clearInputMessages()

            # If there was messages they will be sent, if not we make nothing
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\nBaseProtocol.processInputMessage()")
            traceback.print_exc()

            return False

    # ================================================================
    # OUTPUT MESSAGE

    def processOutputMessage(self):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL OUTPUT/RESPONSE MESSAGE HANDLING PROCESS"""

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

                    # Go message per message
                    for outputMessage in tmpOutputMessages:

                        # Build a new message with desired content
                        rawOutputMessage = self.newMessage(
                            message=outputMessage)

                        # ADD TO OUTPUT BUFFER
                        res = self.camera.addOutputBuffer(
                            value=rawOutputMessage)
                        if (not res):
                            # If there is an error
                            return res

                self.camera.clearOutputMessages()

            # If everything is allright return true
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\nBaseProtocol.processOutputMessage()")
            traceback.print_exc()

            return False

    # ================================================================
    # OUTPUT BUFFER

    def processOutputBuffer(self):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL OUTPUT/RESPONSE BYTES HANDLING PROCESS"""
        try:

            # [HINT]: [Implement here your logic if you need to send the output information]
            #
            # #
            # [EXAMPLE OF GENERIC SEND USING OUTPUTBUFFER]
            while self.camera.getLenOutputBuffer() > 0:
                tmpResponse = self.camera.outputBuffer.pop(0)
                tmpResponseBytes = tmpResponse.messageToBytes()
                self.request.send(tmpResponseBytes)
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\nBaseProtocol.processOutputBuffer()")
            traceback.print_exc()

            return False

# ================================================================
# BASE PROTOCOL MESSAGES
# ================================================================


class Message():
    """
    # Base Message

    ```Abstract Class```

    Description ::
    ---------- 

    Defines the structure of protocol message.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    Attributes ::
    ----------

    :attr bytes|str message: Contains the treated content of a message
    [More Attributes can be added]

    """

    def __init__(self, rawdata=None):
        # Bytes array to parse
        self.rawdata = rawdata
        # Message content
        self.content = None

    # Standard Base Message to Bytes
    def messageToBytes(self):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL STRUCTURE TO BYTES PROCESS"""
        try:
            if(type(self.content) != bytes):
                return bytes(self.content, "utf-8")
            return self.content
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="Message.messageToBytes()")
            traceback.print_exc()
            return self.content

    # Base Prepare Message Method
    def prepareMessage(self, message):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL MESSAGES PREPARATION PROCESS"""
        try:
            # [HINT]: [Implement here your logic to prepare and create a message]
            #
            #   You can add the parameters you need for preparing your message
            #   You must add the information in the arguments from your message class
            #
            # #
            self.content = message
            op.printLog(logType="DEBUG",
                        messageStr="Message.prepareMessage() Not implemented!")
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="Message.prepareMessage()")
            traceback.print_exc()
            return False

    # Standad Base Parse Message Method
    def parseMessage(self):
        """OVERRIDE THIS METHOD WITH DESIRED PROTOCOL MESSAGE PARSING PROCESS"""
        try:
            # Store rawdata into message
            self.content = self.rawdata
            return self
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="Message.parseMessage()")
            traceback.print_exc()
            return None
