# coding=UTF-8
import traceback
from operators.op import op
from datetime import datetime, timezone


class Camera():
    '''
    # Base Camera

    ```Abstract Class```

    Description ::
    ---------- 

    Class that contains a Camera information, status and op.

    Input ::
    -----

    :attr str ip: Contains the ip from Camera.

    :attr int port: Contains the port from Camera.

    :attr str socketkey: Contains the socket key (ip:port)

    :attr str cameraid: Contains the Camera identification unique key

    :attr str sessionid: Contains the Camera session identification unique key

    [More Attributes can be added]

    BUFFER LOGIC ::
    -------------
    Go to class for more information

        Camera BUFFER LOGIC:

        | INPUT BUFFER   | -> Message Type Object 
        | INPUT MESSAGE  | -> Clear Message
        | OUTPUT BUFFER  | -> Clear Reponse Message
        | OUTPUT MESSAGE | -> Message Type Object Reponse


        DATATYPE       Camera                        PROTOCOL

        (Bytes)   ###################        ########################         
        > REQUEST     ADD INPUT BUFFER    =>     PROCESS INPUT BUFFER    >
                    ###################        ########################
                        #####################        #########################         
        (String)  >     ADD INPUT MESSAGE    =>      PROCESS INPUT MESSAGE    >
                        #####################        #########################
                            #####################        ##########################         
        (String)      >     ADD OUTPUT MESSAGE    =>     PROCESS OUTPUT MESSAGE    >
                            #####################        ##########################
                                #####################        #########################         
        (Bytes)           >     ADD OUTPUT BUFFER    =>      PROCESS OUTPUT BUFFER    > REPONSE
                                #####################        #########################                                                                                 

    '''

    def __init__(self, ip, port, cameraid=None, sessionid=None, type="BOTH"):
        
        self.types = ["ENTRY", "EXIT", "BOTH"]
        # Atributes from Camera
        self.ip = ip
        self.port = port
        # The socket key can identify the Camera
        if(self.ip != "" and port != None):
            self.socketkey = self.ip + ":" + str(self.port)

        # Attributes for handshake
        self.cameraid = self.setCameraId(value=cameraid)
        self.sessionid = self.setSessionId(value=sessionid)
        self.publicKey, self.privateKey =  None, None
        self.type = type 
        
        # Datetime elements
        self.created = datetime.now(timezone.utc)
        self.last_message = self.created

        # Set input and output buffer
        self.inputBuffer = list()
        self.inputMessages = list()

        self.outputBuffer = list()
        self.outputMessages = list()

        # Set protocol spoken by the Camera
        self.protocol = self.getProtocol()

        self.status = "OFFLINE"

        # Initialize the variables that contain the counter of messages
        self.messagesRecieved = 0
        self.messagesSent = 0
        self.encrypted = False
    
    
    # Sets the protocol from Camera
    def getProtocol(self):
        """MAY BE OVERRIDED WITH DESIRED PROTOCOL"""

        return op.createClass("BaseProtocol")

    # Loads handler and loads the request using the protocol spoken by Camera
    def processRequest(self, handler):
        try:
            # Load the request from handler using the protocol flow
            return self.protocol.loadRequest(handler=handler)
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="\n BaseCamera.loadRequest(request)")
            traceback.print_exc()
            # Close Camera handler when a ERROR happened
            handler.keepAlive = False

        return handler

    # ================================================================
    # Camera CONNECTION METHODS

    def close(self):
        # Stop protocol processing
        self.protocol.finish()
        self.status = "OFFLINE"

    def forceClose(self):
        res = False
        # If Camera is online we can force close
        if self.status == "ONLINE":
            res = self.addOutputBuffer(value=self.protocol.getCloseMessage())
            self.close()

        return res

    # ================================================================
    # Camera IDENTIFICATION METHODS

    # Set Camera id using IP
    def setCameraId(self, value=None):
        """CAN BE OVERRIDED WITH DESIRED PROTOCOL"""

        # If there is no value
        if value == None:
            # The Camera id is the socket
            value = self.socketkey
        # Store value
        self.cameraid = value

        return value

    def setSessionId(self, value):
        """CAN BE OVERRIDED WITH DESIRED PROTOCOL"""

        self.sessionid = value

        return self.sessionid

    # ================================================================
    # BUFFER AND MESSAGE METHODS

    # -------------------------------------------------
    # INPUT BUFFER
    # -------------------------------------------------

    # CLEAR
    def clearInputBuffer(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.inputBuffer = []

    # ADD
    def addInputBuffer(self, value):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.inputBuffer.append(value)
        # Count the message received
        self.messagesRecieved += 1
        res = self.protocol.processInputBuffer()
        if (not res):
            op.printLog(
                logType="WARNING", messageStr="Something went wrong! BaseCamera.addInputBuffer()")

        return res

    # GET
    def getInputBuffer(self, sep=""):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        tmpBuffer = ""

        # Concat payload data from inputbuffer frames
        for baseMessage in self.inputBuffer:
            tmpBuffer += baseMessage.message

        self.clearInputBuffer()

        return tmpBuffer

    # GET LENGTH
    def getLenInputBuffer(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        return len(self.inputBuffer)

    # -------------------------------------------------
    # INPUT MESSAGES
    # -------------------------------------------------

    # CLEAR
    def clearInputMessages(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.inputMessages = []

    # ADD
    def addInputMessage(self, value):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.inputMessages.append(value)
        # Store the last message time
        self.last_message = datetime.now(timezone.utc)
        res = self.protocol.processInputMessage()
        if (not res):
            op.printLog(
                logType="WARNING", messageStr="Something went wrong! BaseCamera.addInputMessage()")

        return res

    # GET
    def getInputMessages(self, sep=""):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        return self.inputMessages

    # GET LENGTH
    def getLenInputMessages(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        return len(self.inputMessages)

    # -------------------------------------------------
    # OUTPUT MESSAGES
    # -------------------------------------------------

    # CLEAR

    def clearOutputMessages(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.outputMessages = []

    # ADD
    def addOutputMessage(self, value):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.outputMessages.append(value)
        res = self.protocol.processOutputMessage()
        if (not res):
            op.printLog(
                logType="WARNING", messageStr="Something went wrong! BaseCamera.addOutputMessage()")

        return res

    # GET
    def getOutputMessages(self, sep=""):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        res = sep.join(self.outputMessages)
        self.clearOutputMessages()

        return res

    # GET LENGTH
    def getLenOutputMessages(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        return len(self.outputMessages)

    # -------------------------------------------------
    # OUTPUT BUFFER
    # -------------------------------------------------

    # CLEAR
    def clearOutputBuffer(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.outputBuffer = []

    # ADD
    def addOutputBuffer(self, value):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        self.outputBuffer.append(value)
        res = self.protocol.processOutputBuffer()
        if (not res):
            op.printLog(
                logType="WARNING", messageStr="Something went wrong! BaseCamera.addOutputBuffer()")
            return res
        self.messagesSent += 1

        return res

    # GET
    def getOutputBuffer(self, sep=b""):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        return sep.join(self.outputBuffer)

    # GET LENGTH
    def getLenOutputBuffer(self):
        """CAN BE OVERRIDED WITH DESIRED LOGIC"""

        return len(self.outputBuffer)

    # ================================================================
    # PRINTING METHODS

    def toString(self):
        """CAN BE OVERRIDED WITH DESIRED FORMAT"""

        tmpString = "Camera ["+self.cameraid+"], "
        tmpString += "status ["+str(self.status)+"] "
        if(self.socketkey != None):
            tmpString += "on ["+self.socketkey+"] "
        if(self.sessionid != None):
            tmpString += "logged in with sessionid = ["+self.sessionid+"] "
        tmpString += "type ["+str(type(self.protocol))+"] "
        return tmpString
