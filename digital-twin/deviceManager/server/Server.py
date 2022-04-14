# coding=UTF-8
import traceback
import threading
import socketserver
from operators.op import op
from datetime import datetime, timezone
import hashlib

from camera.BaseCameraManager import BaseCameraManager


class RequestHandler(socketserver.BaseRequestHandler):
    """
    # Base Request Handler

    inherits from ```socketserver.BaseRequestHandler```

    ```Abstract Class```

    Description ::
    -----------

    Defines the connection flow handler.
    This class can be overrided.

    Attributes ::
    ----------

    :attr dict parsedConnectionData: Contains the parsed data of the connection which is used when identifing the Camera.

    :attr bytes connectionData: Contains the initial connection data.

    :attr object Camera: Contains the Camera object .

    :attr socket.socket request: Contains the connection socket object.

    :attr socketserver server: Contains the server object.

    [More attributes are used and inherited from socketserver.BaseRequestHandler]

    Connection Flow ::
    ---------------
    [More details in the code python docs]

        SETUP [IdentifyConnectionProtocol -> SetupCameraType] 
            -> HANDLE [Listen -> Received(Start) -> Process Camera Request -> Processed(Finish)?If test server store results?If not print results -> Received(Start) -> Process...] (Connection is open until server or Camera closes)
                -> FINISH [Close Camera]

    """

    # ================================================================
    # CONNECTION START/SETUP METHODS

    # Sets up the connection data.
    def setup(self):
        # If data is HTTP, SJMP or WebSocket the parsed data will be stored here
        self.parsedConnectionData = {}
        # Get the connection data
        self.connectionData = self.request.recv(2048)
        if (self.connectionData != ""):
            op.printLog(
                logType="DEBUG", messageStr=f"[NEW] RAW Connection Data Received: [{self.connectionData.decode('utf-8')}]")

        # Identify the protocol class of the connection
        protocolClass = self.identifyConnectionProtocol()

        op.printLog(
            logType="DEBUG", messageStr="Incoming ["+protocolClass+"] Protocol Connection...")

        # Setup Camera, reconnection or creating a new one.
        self.camera = self.setupCamera(protocolClass=protocolClass)

        # Print Camera information
        op.printLog(logType="DEBUG", messageStr=self.camera.toString())

        op.printLog(logType="DEBUG", messageStr="["+self.server.serverid +
                    "]-["+self.server.socketkey+"] BaseRequestHandler.setup().")

        # Connection keep alive
        self.keepAlive = True

        # STATS variables
        # Timestamps
        self.messageRecievedTimestamp = None
        self.messageProcessedTimestamp = None
        self.mintime = None
        self.maxtime = None

        # Numeric stats variables
        # Duration of one message processing after receiving
        self.duration = 0
        # Number of messages received and processed
        self.messagesProcessed = 0

        # Total duration of messages (Sum of duration)
        self.totalduration = None
        # Total duration of messages processed (Sum of messagesProcessed)
        self.totalmessagesProcessed = 0

        return socketserver.BaseRequestHandler.setup(self)

    # Identify the protocol connection message type.

    def identifyConnectionProtocol(self):
        """OVERRIDE THIS METHOD WITH DESIRED Camera PROTOCOL CONNECTION CLASS AND MESSAGE PROTOCOL DETECTION LOGIC"""

        return "camera.Camera.Camera"

    # Setups the Camera using the protocol
    def setupCamera(self, protocolClass):
        """OVERRIDE THIS METHOD WITH DESIRED Camera PROTOCOL token SETUP"""

        # Set session id
        tmpSessionId = str(hashlib.md5((self.client_address[0] + ":" + str(
            self.client_address[1]) + ":" + str(datetime.now(timezone.utc))).encode()).hexdigest())
        # Create or Reconnect Camera
        tmpCamera = self.server.camerasManager.createOrGetCamera(
            protocolClass=protocolClass, ip=self.client_address[0], port=self.client_address[1], cameraid=None, token=tmpSessionId)

        return tmpCamera

    # ================================================================
    # REQUEST HANDLING METHODS

    # Handles the connection
    def handle(self):
        op.printLog(logType="DEBUG", messageStr="[{0}]-[{1}] > Received one request from {2}".format(
            self.server.serverid, self.server.socketkey, self.camera.cameraid))
        self.listen()

        return

    # Listen to the Camera
    def listen(self):
        # Listen until the connection is closed by the server or by the Camera.
        while(self.keepAlive and self.server.keepAlive):
            self.received()
            # Process the request with Camera structure
            self = self.camera.processRequest(handler=self)
            self.processed()

        return

    # ================================================================
    # STATS HANDLING METHODS

    # Initializes the variables to calculate performance before request processing.

    def received(self):
        # Store when the message was received
        self.messageRecievedTimestamp = datetime.now(timezone.utc)
        # Clean all the variables for this interaction
        self.keepAlive = True
        self.messageProcessedTimestamp = None
        self.duration = 0
        self.messagesProcessed = 0

    # Calculates the performances after procesing the request.
    def processed(self):
        # Store when the message was processed
        self.messageProcessedTimestamp = datetime.now(timezone.utc)
        # Calculate the duration from processed message
        self.duration = self.messageProcessedTimestamp - self.messageRecievedTimestamp
        # If the variables are not initialized
        if(self.totalduration == None):
            self.totalduration = self.duration
            self.mintime = self.duration
            self.maxtime = self.duration

        # If there were messages processed
        if self.messagesProcessed > 0:

            # Check if this time is the minumum
            if(self.mintime > self.duration):
                self.mintime = self.duration

            # Check if this time is the maximum
            if(self.maxtime < self.duration):
                self.maxtime = self.duration

            # Sum the number of messages and the duration to total
            self.totalmessagesProcessed += self.messagesProcessed
            self.totalduration += self.duration

     
            # Print statistics after processing request (Messages Arrived and Time Duration of Processing)
            op.printLog(logType="STATS", messageStr="Messages Processed: nmessages=["+str(
                self.messagesProcessed)+"];duration=["+str(self.duration)+"]")

    # ================================================================
    # CLOSE CONNECTION METHODS

    # At the end of the processing we need to close the Camera.
    def finish(self):
        # Close Camera
        self.camera.close()
        return socketserver.BaseRequestHandler.finish(self)


class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """
    # Base Server

    inherits from ```socketserver.ThreadingMixIn``` and ```socketserver.TCPServer```

    ```Abstract Class```

    Description ::
    -----------

    Defines the multithread server structure and workflow. Overrides methods of TCPServer
    This class can be overrided with desired protocol logic.

    Attributes ::
    ----------

    :attr type RequestHandlerClass: Contains the request handler class type. [BaseRequestHandler] in this case. (Can be overrided)

    :attr object camerasManager: Contains the cameras manager that contains all the logic to manage the cameras. [BaseCamerasManager] in this case (Can be overrided)

    :attr str serverid: serverid of the server. (Server socket key by default (ip:port))

    :attr float poll_interval: Timeout check if server needs to shutdown

    :attr str ip: Server socket ip address.

    :attr int port: Server socket opened port.

    :attr str socketkey: Server socket key (ip:port)

    :attr threading.thread thread: Main Thread used by server to handle connections and start new threads. 

    :attr str status: Server current status. Can be SHUTDOWN, RUNNING.

    :attr bool keepAlive: Defines if server shall stay alive or shall shutdown.

    [More attributes can be added]

    """

    def __init__(self, ip='localhost', port=0, poll_interval=0.5, bind_and_activate: bool = ...) -> None:
        # Mandatory Socket Server attributes
        self.RequestHandlerClass = self.getServerRequestHandler()
        self.ip = ip
        self.port = port
        self.poll_interval = poll_interval
        super().__init__(server_address=(self.ip, self.port),
                         RequestHandlerClass=self.RequestHandlerClass, bind_and_activate=bind_and_activate)

        # Server connection Atributtes
        self.camerasManager = self.getCamerasManager()
        self.keepAlive = True
        self.ip, self.port = self.server_address  # find out what port we were given
        self.status = "SHUTDOWN"

        # Server identification Attributes
        self.socketkey = self.ip+":"+str(self.port)
        self.serverid = self.socketkey

        # Thread Attributes
        self.thread = None

        # Statistics Attributes
        self.totalMessagesRecieved = 0
        self.totalRecieveDuration = None
        self.maxRecieveDuration = None
        self.minRecieveDuration = None
        self.totalCameras = 0
        self.startMsgs = None
        self.finishMsgs = None
        self.processedDuration = None

        # Test Permance Measure Attributes (Can be removed in production)
        self.isTestServer = False
        self.objectiveType = None
        self.objectiveNC = None
        self.objectiveNM = None
        self.expectedMessages = 0

    # ================================================================
    # SETUP METHODS

    # Defines server cameras manager
    def getCamerasManager(self):
        """OVERRIDE THIS METHOD WITH DESIRED DEFAULT PROTOCOL Camera OR CLIENTSMANAGER"""

        return BaseCameraManager(cameraprotocolClass="BaseCamera")

    # Defines the server request handler type
    def getServerRequestHandler(self):
        """OVERRIDE THIS METHOD WITH DESIRED DEFAULT PROTOCOL HANDLER"""

        return RequestHandler

    # Sets the server serverid
    def setServerId(self, serverid):
        """OVERRIDE THIS METHOD IF YOU NEED TO INCLUDE A SPECIAL SERVERID STRUCTURE TO SERVER"""
        self.serverid = serverid

    # ================================================================
    # CONNECTION AND KEEPALIVE METHODS

    # Starts the server and wait for shutdown in every poll interval time
    def serve_forever(self, poll_interval: float = ...) -> None:
        val = None
        try:
            # Set running status
            self.status = "RUNNING"
            # Start server
            val = super().serve_forever(poll_interval=poll_interval)
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="in serve_forever().")
            traceback.print_exc()

        return val

    # Shutsdown the server
    def shutdown(self) -> None:
        val = None
        try:
            # Update status
            self.status = "SHUTDOWN"
            # Change keepAlive
            self.keepAlive = False
            # Close server
            val = super().shutdown()
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e, messageStr="in shutdown().")
            traceback.print_exc()

        return val

    # Check if server is alive (RETURNS TRUE IF Alive)
    def isAlive(self):
        return (self.status == "RUNNING")

    # ================================================================
    # WORKFLOW METHODS (START AND STOP)

    # Start the main thread of the server and open connection
    def start(self):
        # Server started reciving messages time
        self.startMsgs = datetime.now(timezone.utc)
        # Start server main thread and open connection
        self.thread = threading.Thread(
            name=self.serverid, target=self.serve_forever, args=[self.poll_interval], daemon=False)
        self.thread.setDaemon = True  # don't hang on exit
        self.thread.start()
        if(self.thread == None):
            return None

        return True

    # Stop the main thread of the server
    def stop(self):
        # Server finished reciving messages time
        self.finishMsgs = datetime.now(timezone.utc)
        # Close server connection
        self.shutdown()
        # Close cameras connection
        self.camerasManager.closeCameras()
        # Stop server main thread
        self.thread.join()
        self.thread = None

    # ================================================================
    # PRINT METHODS

    def toString(self):
        # Capture server main information
        tmpString = "Server ["+self.serverid+"] in socket ["+self.socketkey+"] status ["+str(
            self.status)+"] in thread: [" + ((str(self.thread._name)) if self.thread != None else "None") + "]"

        return tmpString

    # ================================================================
    # TEST METHODS (Can be removed in production)

    def startTest(self, objectiveType=None, objectiveNC=None, objectiveNM=None):
        # Store test vars
        self.isTestServer = True
        self.objectiveType = objectiveType
        self.objectiveNC = objectiveNC
        self.objectiveNM = objectiveNM
        self.messagesPerCamera = self.objectiveNM+1
        self.expectedMessages = (objectiveNM*objectiveNC)+objectiveNC
        startPoint = int(int(self.objectiveNC)/5)
        self.controlPoints = list(
            range(startPoint, int(self.objectiveNC), startPoint))
        op.printLog(logType="INFO", messageStr="["+self.serverid+"]-["+self.socketkey+"] Test Server Started Objective:["+str(self.objectiveType)+"];expectedMessages:["+str(
            self.expectedMessages)+"];expectedCameras:["+str(self.objectiveNC)+"];expectedMessagesPerCamera:["+str(self.messagesPerCamera)+"]; Control Points: ["+str(self.controlPoints)+"].")
        # Start Server
        self.start()

    # Stores the results of test in server
    def storeResults(self, totalmessagesProcessed, totalduration, mintime, maxtime):
        # Add one more Camera to the ones processed
        self.totalCameras += 1
        # Store the number of messages processed
        self.totalMessagesRecieved += totalmessagesProcessed
        # If the attributes where not initialized
        if(self.totalRecieveDuration == None):
            self.totalRecieveDuration = totalduration
            self.minRecieveDuration = totalduration
            self.maxRecieveDuration = totalduration
        else:
            # Add time to the existing time
            self.totalRecieveDuration += totalduration

        # Check if the time is the minumum
        if(self.minRecieveDuration > mintime):
            self.minRecieveDuration = mintime

        # Check if time is the maximum
        if(self.maxRecieveDuration < maxtime):
            self.maxRecieveDuration = maxtime

        # If the number of cameras is in the control points.
        if(self.totalCameras in self.controlPoints):
            # Calculate the porcentage of completed process
            completedPorcentage = (self.totalCameras/self.objectiveNC)*100
            actualTime = datetime.now(timezone.utc)
            # Calculate enlapsed time until now
            enlapsedTime = actualTime - self.startMsgs
            op.printLog(logType="INFO", messageStr="Test ["+str(completedPorcentage)+" %%] completed! ["+str(
                self.totalMessagesRecieved)+"] from ["+str(self.expectedMessages)+"] Messages Received, Enlapsed Time: ["+str(enlapsedTime)+"]")

        # Check if the objective has been fullfilled
        if(self.totalCameras >= self.objectiveNC):
            # Calculate average time
            avgTime = self.totalRecieveDuration/self.totalCameras
            self.finishMsgs = datetime.now(timezone.utc)
            # Calculate total duration time
            self.processedDuration = self.finishMsgs - self.startMsgs
            op.printLog(logType="STATS", messageStr="Total Messages Processed: nmessages=["+str(self.totalMessagesRecieved)+"];mintime=["+str(self.minRecieveDuration)+"];avgtime=["+str(
                avgTime)+"];maxtime=["+str(self.maxRecieveDuration)+"];duration=["+str(self.processedDuration)+"];totaladdedtime=["+str(self.totalRecieveDuration)+"]")
