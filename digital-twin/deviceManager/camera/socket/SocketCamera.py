# coding=UTF-8
from operators.op import op
import threading
import socket
from operators.cryptool import cryptool

from camera.socket.SocketCamerasHandler import SocketCamerasHandler
from protocols.Protocol import *
from camera.Camera import Camera


class SocketCamera(Camera):
    '''
    # Base Socket Camera 

    inherits from ```BaseCamera``` 

    ```Abstract Class```

    Description ::
    ---------- 

    Class that contains a socket Camera logic. This class can be overrided.

    Input ::
    -----

    :attr str serverip: Contains the ip from server that Camera is connected to.

    :attr int serverport: Contains the port from server that Camera is connected to.

    :attr str serverkey: Contains the server socket key (ip:port) that Camera is connected to.

    :attr str socket: Contains the socket object that handles the TCP connection.

    :attr str socketkey: Contains the Camera socket key (ip:port).

    :attr str handler: Contains the handler of the connection flow [SocketCameraHandler]

    :attr str thread: Contains the thread that listens and processes requests.

    :attr str sendingThread: Contains the thread that prepares and sends messages to the server.

    [More Attributes can be added]
    '''

    def __init__(self, serverip, serverport, ip=None, port=None, cameraid=None, sessionid=None, type="BOTH"):
        # Call super of BaseCamera
        super().__init__(ip=ip, port=port, cameraid=cameraid, sessionid=sessionid, type=type)

        # Server configurations
        self.serverip = serverip
        self.serverport = serverport
        self.serverkey = self.serverip+":"+str(self.serverport)
        self.serversecret = None
        
        # Socket configurations
        self.socket = None
        self.socketkey = None
        self.thread = None
        self.handler = None
        self.sendingThread = None

        # [TEST] VARS -> REMOVE IN PRODUCTION
        self.isTestCamera = False
        self.startMessageTime = None
        self.finishMessageTime = None
        self.durationMessageTime = None
        self.totalSentDuration = None
        self.maxSentDuration = None
        self.minSentDuration = None
        self.allMessagesSent = False
        self.messagesDuration = None

    # ================================================================
    # CONNECTION HANDLING METHODS

    def generateSecret(self):
        return cryptool.generateKeys(string=True)
    
    def deleteSecret(self):
        self.privateKey = None
        self.publicKey = None
        return True
    
    # Gets the handler of connection
    def getHandler(self):
        """OVERRIDE THIS METHOD WITH DESIRED HANDLER"""

        return SocketCamerasHandler(camera=self)

    # Connects to server though socket
    # (Returns True if was posible to connect, and False if not, None if connection data is not defined)
    def connect(self):
        
        self.publicKey, self.privateKey = self.generateSecret()
        
        # Check if server has connection information defined
        if(((self.serverip == "" or self.serverip == None) or (self.serverport == "" or self.serverport == None))):
            return None

        # Create socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server
        conn = self.socket.connect_ex((self.serverip, self.serverport))
        # Check if was posible to connect
        if(conn != 0):
            # Set connection status to fail
            self.status = "FAILED"
            return False

        # Store socket connection information
        self.ip = self.socket.getsockname()[0]
        self.port = self.socket.getsockname()[1]
        self.socketkey = self.ip+":"+str(self.port)

        # Set Status to connected
        self.status = "CONNECTED"
        op.printLog(
            logType="DEBUG", messageStr="Camera Socket Opened on ["+self.socketkey+"] ...")

        return True

    # ================================================================
    # OPEN/CLOSE METHODS

    # Opens the Camera connection and starts listening
    # (Returns True if we can open, and false if not)

    def open(self):
        # Configure handler
        self.handler = self.getHandler()
        # Set listening thread
        self.thread = threading.Thread(name=str(
            str(type(self))+"-"+self.cameraid+"-"+self.serverkey), target=self.handler.listen)
        if(self.thread == None):
            return False
        self.thread.setDaemon = True
        self.thread.start()

        op.printLog(
            logType="DEBUG", messageStr="Camera ["+self.cameraid+"] listening in ["+self.thread.getName()+"]")

        return True

    # Close the Camera connection and stop listening
    def close(self):
        self.deleteSecret()
        # If there is a socket connected
        if(self.socket != None):
            self.socket.close()
        # Clean all variables
        self.socket = None
        self.ip = ""
        self.port = ""
        self.cameraid = ""
        # Set status to disconnected
        self.status = "DISCONNECTED"

    # ================================================================
    # MESSAGE HANDLING METHODS

    # Sends messages adding to output buffer (TO SERVER)

    def sendMessage(self, message):
        # Set message logic
        self.addOutputMessage(message)

    # ================================================================
    # PRINT METHODS

    # Prints Camera information overriding the existing function with extra data

    def toString(self):
        tmpString = super().toString()
        # Add socket ket to Camera info
        if(self.serverkey != None):
            tmpString += "in ["+str(self.serverkey)+"] "

        return tmpString
