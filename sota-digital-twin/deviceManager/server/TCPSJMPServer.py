# coding=UTF-8
import hashlib
from datetime import datetime, timezone
from operators.op import op

from camera.BaseCameraManager import BaseCameraManager
from server.TCPServer import TCPRequestHandler, TCPServer
from protocols.SJMPHandler import packet


class TCPSJMPRequestHandler(TCPRequestHandler):
    """
    # TCP SJMP Request Handler

    inherits from ```TCPRequestHandler```


    Description ::
    -----------

    Defines the connection flow of a TCP SJMP Request handler.

    """
    # ================================================================
    # CONNECTION START/SETUP METHODS

    # Identify the protocol connection message type.
    def identifyConnectionProtocol(self):
        # Get last protocol
        tmpCamera = super().identifyConnectionProtocol()

        # Identify if the data is not empty
        tmpLenRequest = len(self.connectionData)
        if(tmpLenRequest < 0):
            return tmpCamera

        # If the first char is a "{" is a JSON
        if(self.connectionData[0:1] != b'{'):
            return tmpCamera

        # Parse the data as a SJMP
        self.parsedConnectionData = packet().loadPacketFromBytes(data=self.connectionData)
        # If is not a SJMP
        if (self.parsedConnectionData == None):
            return "camera.TCPCamera.TCPCamera"

        return "camera.TCPSJMPCamera.TCPSJMPCamera"

    # Setups the Camera using the protocol
    def setupCamera(self, protocolClass):

        if(protocolClass != "camera.TCPSJMPCamera.TCPSJMPCamera"):
            return super().setupCamera(protocolClass=protocolClass)

        #
        # # Include here the protocol logic to reconnect or start Camera
        tmpCameraId = self.parsedConnectionData.cameraid

        tmpSessionId = str(hashlib.md5((self.client_address[0] + ":" + str(self.client_address[1]) + ":" + str(
            datetime.now(timezone.utc)) + "cameraid=["+tmpCameraId+"]").encode()).hexdigest())

        tmpCamera = self.server.camerasManager.createOrGetCamera(
            protocolClass=protocolClass, ip=self.client_address[0], port=self.client_address[1], cameraid=tmpCameraId, token=tmpSessionId)

        return tmpCamera


class TCPSJMPServer(TCPServer):
    """
    # TCP SJMP Server

    inherits from ```TCPServer``` 

    Description ::
    -----------

    Defines the multithread server structure and workflow using TCP SJMP.
    """

    # Defines server cameras manager
    def getCamerasManager(self):
        return BaseCameraManager(cameraprotocolClass="camera.TCPSJMPCamera.TCPSJMPCamera")

    # Defines the server request handler type
    def getServerRequestHandler(self):
        return TCPSJMPRequestHandler
