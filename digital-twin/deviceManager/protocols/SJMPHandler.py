# coding=UTF-8
import traceback
from operators.op import op
from datetime import datetime, timezone
import json


class handler():
    """
    # SJMP Handler

    Description ::
    -----------

    Defines the protocol handler and logic from SJMP.

    Intput ::
    ----------

    :attr object handler: Contains the connection handler.    

    Attributes ::
    ----------

    :attr object Camera: Contains the Camera object.

    :attr SJMPPacket packet: Contains the SJMP Packet

    :attr socketserver server: Contains the server object. (In this case none)

    Handler Flow ::
    ---------------
    [More details in the code python docs]

    REQUEST (rawPacket) -> processPacket(packet) -> Process FLAG -> RESPONSE (responsePacket)

    The RESPONSE can be None.    
    """

    def __init__(self, handler):
        self.handler = handler
        self.camera = handler.camera
        self.server = handler.server
        self.packet = None

    # ================================================================
    # SETUP METHODS

    def processPacket(self, rawPacket):
        """ 
            Processes a rawPacket that can be SJMP.
                @returns:
                    -> IF not SJMP -> Nothing (None)
                    -> IF error -> RJTP Error packet
                    -> IF success -> SJMP Success Ack packet
        """
        # If the packet is empty we can not process
        if (rawPacket == None):
            return None

        # Create new packet to parse
        tmpSJMPPacket = packet()
        res = tmpSJMPPacket.parse(rawdata=rawPacket)

        # If we were not able to parse
        if(not res):
            print("[MESSAGE ARRIVED]")
            print(rawPacket)
            # Return nothing if we were not able to parse.
            return None

        # Store server time, when the message has arrived
        tmpSJMPPacket.srv_time = self.handler.messageRecievedTimestamp.timestamp()

        # If there is no output message we will return None
        tmpOutputMessage = None

        # If is SJMP Store Packet
        self.packet = tmpSJMPPacket

        # Check for flag and call the designated handler

        if(self.packet.flag == "MSG"):
            tmpOutputMessage = self.processMSGFlag()

        elif(self.packet.flag == "SYN"):
            tmpOutputMessage = self.processSYNFlag()

        elif(self.packet.flag == "OK"):
            tmpOutputMessage = self.processOKFlag()

        elif(self.packet.flag == "FIN"):
            tmpOutputMessage = self.processFINFlag()

        # Return nothing or something depending in the result from the flag processing
        return tmpOutputMessage

    # ================================================================
    # FLAG METHODS

    # Process FIN flag
    def processFINFlag(self):

        # Camera Must be active
        if(self.camera == None or self.packet == None):
            return None

        # If we are in the server
        if(self.server != None):
            # Close connection
            self.handler.keepAlive = False
            return None

        # If we are in the Camera
        self.camera.status = "DISCONNECTED"
        self.handler.keepAlive = False

        op.printLog(
            logType="INFO", messageStr="["+self.camera.cameraid+"] status changed to ["+self.camera.status+"]!")
        self.camera.close()
        # Store session id

        return None

    # Process OK flag
    def processOKFlag(self):

        # Camera Must be active
        if(self.camera == None or self.packet == None):
            return None
        # If token is not in ok packet
        if(self.packet.token == None):
            return None

        # Store session id
        self.camera.token = self.packet.token
        self.camera.status = "ONLINE"
        op.printLog(logType="DEBUG", messageStr="Camera ["+self.camera.cameraid+"] status [" +
                    self.camera.status+"] logged in with token = ["+self.camera.token+"] in ["+self.camera.serverkey+"].")

        return None

    # Process SYN flag
    def processSYNFlag(self):

        # Camera Must be active
        if(self.camera == None or self.packet == None):
            return None

        self.camera.cameraid = self.packet.cameraid
        tmpOutputMessage = packet().dumpPacket(flag="OK", device_time=str(
            datetime.timestamp(datetime.now(timezone.utc))), token=self.camera.token)

        return tmpOutputMessage.messageToJSONString()

    # Process MSG flag
    def processMSGFlag(self):

        # Server Must be active
        if(self.server == None):
            op.printLog(
                logType="DEBUG", messageStr=f"[{self.camera.cameraid}] > SJMP MSG RECEIVED FROM [{self.packet.cameraid}]")
            return None
        # Check if origin Camera is authenticated
        originCamera = self.server.camerasManager.getBySessionId(
            token=self.packet.token)
        # We must return an error if not

        tmpOutputPacket = packet()

        # Return to Camera a ERROR if the sending Camera does not exists
        if (originCamera == None):
            tmpOutputMessage = tmpOutputPacket.dumpPacket(
                flag="ERR", message="Origin Camera with token ["+self.packet.token+"] does not exists!")

            return tmpOutputMessage.messageToJSONString()

        # Check if destination Camera exists
        destinationCamera = self.server.camerasManager.getByCameraId(
            cameraid=self.packet.cameraid)
        # We must return an error if not
        if (destinationCamera == None):
            op.printLog(
                logType="ERROR", messageStr="SJMPHandler.processMSGFlag(cameraid=["+self.packet.cameraid+"]). The cameraid [" + self.packet.cameraid + "] don't exist!")
            tmpOutputMessage = tmpOutputPacket.dumpPacket(
                flag="ERR", message="Destination cameraid ["+self.packet.cameraid+"] does not exists!")

            return tmpOutputMessage.messageToJSONString()

        # SENDING MESSAGE TO ANOTHER Camera ---------------------------------
        # Create response with message sent by the Camera
        tmpSJMPResponse = packet().dumpPacket(flag="MSG", message=self.packet.message, srv_time=self.packet.srv_time,
                                              cameraid=originCamera.cameraid, device_time=str(self.packet.device_time))
        # Add new packet to the destination Camera's OutputMessages list
        destinationCamera.addOutputMessage(
            value=tmpSJMPResponse.messageToJSONString())
        op.printLog(
            logType="DEBUG", messageStr=f"[{originCamera.cameraid}] > SENT SJMP MSG TO [{self.packet.cameraid}]")
        # ------------------------------------

        # SENDING MESSAGE BACK TO Camera ---------------------------------
        # Send a message to the Camera saying that the message was sent
        if(destinationCamera.status == "ONLINE" or destinationCamera.status == "CONNECTED"):
            tmpOutputMessage = tmpOutputPacket.dumpPacket(
                flag="ACK", message="Message was sent to Camera ["+destinationCamera.cameraid+"]")

            return tmpOutputMessage.messageToJSONString()

        # Prepare response
        tmpOutputMessage = tmpOutputPacket.dumpPacket(
            flag="ACK", message="Camera ["+destinationCamera.cameraid+"] is ["+destinationCamera.status+"]. Message stored in OutputMessages")

        return tmpOutputMessage.messageToJSONString()


class packet():
    """
    # SJMP packet

    Description ::
    -----------

    This class marks the data structure of a SJMPPacket and includes logic.


    Attributes ::
    ----------

    :attr bytes|str data: Contains bytes or string of the data introduced in packet.

    :attr str flag: Contains the flag from a packet.

    :attr list flags: Contains the authorized flags.

    :attr str|datetime.timpestamp srv_time: Contains the server timestamp.

    :attr str|datetime.timpestamp device_time: Contains the device timestamp.

    :attr str cameraid: Contains the Camera identification unique key

    :attr str token: Contains the Camera session identification unique key

    :attr str message: Contains the packet messages.


    Functionalities ::
    ---------------

    -> Parse rawdata and store it into the structure (@function parse)

    -> Store data in structure using params (@function dumpPacket) 

    -> Load packet into structure from:
        - @type bytes (@function loadPacketFromBytes)
        - @type str (@function loadPacket)  

    -> Dump packet into: 
        - JSON Object (@function messageToJSONString)
        - @type dict (@function buildPacket)

    """

    def __init__(self):
        # Data recieved
        self.data = None

        # Attributes from RTJM packet

        # Flag variables
        self.flag = ""
        self.flags = ["OK", "ERR", "ACK", "SYN", "MSG", "RCN", "FIN"]

        # Time variables
        self.srv_time = ""
        self.device_time = ""

        # Camera identification variables
        self.cameraid = ""
        self.token = ""

        # Content of packet
        self.message = ""

    # ================================================================
    # LOAD METHODS

    # Load rawdata and prepare to loadpacket into structure
    def loadPacketFromBytes(self, data):
        # If data is not string we convert it to string
        if type(data) != str:
            data = str(data, "utf-8")

        # If JSON is using (') as field separator we convert it to (")
        data = data.replace("'", "\"")
        parsedPacket = None
        try:
            # Parse JSON and load Packet in structrure
            parsedPacket = self.loadPacket(data=json.loads(data))
        except Exception as e:
            op.printLog(logType="DEBUG", e=e,
                        messageStr=f"NOT JSON:[{str(data.encode('utf-8'))}]")

        return parsedPacket

    # Load packet from data
    def loadPacket(self, data):
        # If the flag is not valid
        if data["flag"] not in self.flags:
            return None

        # Store Flag
        self.flag = data["flag"]

        # Store Server Time
        if "srv-time" in data:
            self.srv_time = op.valueEmpty(data["srv-time"])
        else:
            self.srv_time = str(datetime.timestamp(datetime.now(timezone.utc)))

        # Get Camera Time
        if "device-time" in data:
            self.device_time = op.valueEmpty(data["device-time"])

        # Store rest of attribute if not empty
        if "cameraid" in data:
            self.cameraid = op.valueEmpty(data["cameraid"])

        if "token" in data:
            self.token = op.valueEmpty(data["token"])

        # Get the message
        if "message" in data:
            self.message = op.valueEmpty(data["message"])

        return self

    # ================================================================
    # DUMP PACKET METHODS

    # Store packet params in the structure
    def dumpPacket(self, flag=None, cameraid=None, token=None, srv_time=None, device_time=None, message="Hay, Camera!"):

        # Store Flag
        if flag != None:
            self.flag = flag

        # If flag is not valid we return None
        if self.flag == "" or self.flag == None or self.flag not in self.flags:
            return False

        # Store cameraid and token
        if cameraid != None:
            self.cameraid = cameraid

        if token != None:
            self.token = token

        # Store server time if is not specified
        if (srv_time != None and srv_time != False):
            self.srv_time = srv_time
        elif srv_time == None:
            self.srv_time = str(datetime.timestamp(datetime.now(timezone.utc)))
        else:
            self.srv_time = None

        # Store device time
        if device_time != None:
            self.device_time = device_time

        # Store packet message
        if message != None:
            self.message = message

        # return packet object
        return self

    # Builds the packet as a dictionary and returns a JSON object
    def messageToJSONString(self):
        tmpBuildedPacket = self.buildPacket()

        return json.dumps(tmpBuildedPacket)

    # ================================================================
    # BUILD PACKET METHODS

    # Convert packet in a dictionary object
    def buildPacket(self):
        try:
            packet = {}

            # Standard fields
            packet["flag"] = self.flag

            # Depending on the flag we must store some fields or not
            if(self.flag == "MSG"):
                packet["device-time"] = self.device_time
                if(self.token != "" and self.token != None):
                    packet["token"] = self.token
                # If the message is not from the server the message will have the srv-time when it arrived
                if(self.srv_time != "" and self.srv_time != None):
                    packet["srv-time"] = self.srv_time
                # Camera to send and Message
                packet["cameraid"] = self.cameraid
                packet["message"] = self.message
                return packet

            if(self.flag == "OK"):
                # If the message is not from the server the message will have the srv-time when it arrived
                if(self.srv_time != None):
                    packet["srv-time"] = self.srv_time
                # Camera to send
                packet["token"] = self.token

                return packet

            if(self.flag == "SYN"):
                packet["device-time"] = self.device_time
                # Camera to send
                packet["cameraid"] = self.cameraid
                return packet

            # =======
            # ACK, FIN AND ERR FLAGS JUST CONTAIN MESSAGE, FLAG AND SERVER TIME
            # =======
            # If the server is sending a message as Server
            packet["srv-time"] = self.srv_time
            packet["message"] = self.message

            # return the packet dic object
            return packet

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="SJMPPacket.buildPacket()")
            traceback.print_exc()

            return False

    # ================================================================
    # PARSE PACKET METHODS

    # Parse a buffer of bytes into a SJMPPacket structure
    def parse(self, rawdata):
        try:
            # Parse the data that is received in the incoming rawdata
            res = self.loadPacketFromBytes(data=rawdata)
            # If there was a fail we return False
            if(res == None):
                return False

            # If worked we return True
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="SJMPPacket.parse()")
            traceback.print_exc()

            return False