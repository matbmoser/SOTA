# coding=UTF-8
import traceback
from operators.op import op
from datetime import datetime, timezone


class SocketCamerasHandler():
    """
    # Socket Camera Handler

    copies the workflow from ```BaseRequestHandler```

    Description ::
    -----------

    Defines the connection flow handler from a socket Camera.

    Input ::
    -----

    :attr object Camera: Contains the socket Camera object.


    Attributes ::
    ----------

    :attr dict parsedConnectionData: Contains the parsed data of the connection which is used when identifing the Camera.

    :attr bytes connectionData: Contains the initial connection data.

    :attr SocketCameraManager manager: Contains the Socket Camera Manager.

    :attr socket.socket request: Contains the connection socket object.

    :attr socketserver server: Contains the server object. (In this case none)

    [More attributes are used and inherited from socketserver.BaseRequestHandler]

    Connection Flow ::
    ---------------
    [More details in the code python docs]

        INIT
            -> HANDLE [Listen -> Received(Start) -> Process Camera Request -> Processed(Finish)?If test server store results?If not print results -> Received(Start) -> Process...] (Connection is open until server or Camera closes)
                -> FINISH [Close Camera]

    """

    def __init__(self, camera):
        # Handler variables
        self.parsedConnectionData = {}
        self.camera = camera
        self.server = None
        self.manager = None
        self.request = self.camera.socket

        # Init variables
        self.keepAlive = True
        self.connectionData = None

        # Performance STATS Variables
        self.messageRecievedTimestamp = None
        self.messageProcessedTimestamp = None

        # Stats variables
        self.duration = 0
        self.messagesProcessed = 0
        self.totalmessagesProcessed = 0
        self.totalduration = None
        self.mintime = None
        self.maxtime = None

        return

    # ================================================================
    # REQUEST HANDLING METHODS

    # Listen to the Camera
    def listen(self):
        # While Camera is alive he waits for messages and processes the request
        while(self.keepAlive):
            self.received()
            try:
                self = self.camera.processRequest(handler=self)
            except Exception as e:
                op.printLog(logType="EXCEPTION", e=e,
                            messageStr="in SocketCameraHandler.listen().")
                traceback.print_exc()
                self.keepAlive = False
            self.processed()
        self.finish()
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

            # If the Camera is in test mode we can store the results
            if(self.camera.isTestCamera):
                # If we processed the total messages defined
                if(self.totalmessagesProcessed >= self.manager.messagesPerCamera):
                    # Store results of the test performance in Camera
                    self.manager.storeResults(totalmessagesProcessed=self.totalmessagesProcessed,
                                              totalduration=self.totalduration, mintime=self.mintime, maxtime=self.maxtime)
            else:
                # Print statistics after processing request (Messages Arrived and Time Duration of Processing)
                op.printLog(logType="STATS", messageStr="Messages Processed: nmessages=["+str(
                    self.messagesProcessed)+"];duration=["+str(self.duration)+"]")

    # ================================================================
    # CLOSE CONNECTION METHODS

    def finish(self):
        #logTools.printLog(logType="STATS", messageStr="Total Messages Proccessed: nmessages=["+str(self.totalmessagesProcessed)+"];mintime=["+str(self.mintime)+"];maxtime=["+str(self.maxtime)+"];duration=["+str(self.totalduration)+"]")
        self.camera.close()
        return
