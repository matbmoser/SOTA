# coding=UTF-8
import json
from urllib.parse import unquote
from operators.op import op
import hashlib
from datetime import datetime, timezone

from camera.BaseCameraManager import BaseCameraManager
from server.WebSocketServer import WebSocketRequestHandler, WebSocketServer


class WebSocketSJMPRequestHandler(WebSocketRequestHandler):
    """
    # Web Socket SJMP Request Handler

    inherits from ```WebSocketRequestHandler```


    Description ::
    -----------

    Defines the connection flow of a Web Socket SJMP Request handler.

    """
    # ================================================================
    # CONNECTION START/SETUP METHODS

    # Sets up the connection data
    def setup(self):
        self.parsedConnectionProtocol = None
        return super().setup()

    # Identify the protocol connection message type.
    def identifyConnectionProtocol(self):
        # Get last protocol
        tmpCamera = super().identifyConnectionProtocol()

        # Check if is not websocket
        if(tmpCamera != "camera.WebSocketCamera.WebSocketCamera"):
            return tmpCamera

        # If not contains the protocol header, it is has no SJMP protocol
        if not ("Sec-WebSocket-Protocol" in self.parsedConnectionData.headers):
            return tmpCamera

        # Get the header
        self.parsedConnectionProtocol = self.parsedConnectionData.headers["Sec-WebSocket-Protocol"].replace(
            ", ", ",").split(",")

        # Het the len of the protocol data
        tmpLenParsedConnectionData = len(self.parsedConnectionProtocol)

        # If is not specified the subprotocol name
        if tmpLenParsedConnectionData < 1:
            return tmpCamera

        # Check if the subprotocol is SJMP
        if self.parsedConnectionProtocol[0] != "SJMP":
            return tmpCamera

        return "camera.WebSocketSJMPCamera.WebSocketSJMPCamera"

    def setupCamera(self, protocolClass):

        # Check if the Camera is SJMP
        if(protocolClass != "camera.WebSocketSJMPCamera.WebSocketSJMPCamera"):
            return super().setupCamera(protocolClass=protocolClass)

        #
        # # Include here the protocol logic to reconnect or start Camera
        self.subprotocolList = self.parsedConnectionProtocol
        self.lenSubprotocolList = len(self.subprotocolList)
        # If the parsing fails the switch will be true
        tmpFailSwitch = False

        # If the header is empty
        if not (self.lenSubprotocolList > 0):
            tmpFailSwitch = True

        # Get subprotocol name
        self.subprotocol = self.subprotocolList[0].upper()

        # Check if the first element is SJMP (Subprotocol)
        if self.subprotocol != "SJMP":
            tmpFailSwitch = True

        # Check if the list has a second element
        if not (self.lenSubprotocolList > 1):
            tmpFailSwitch = True

        # Check if json is valid and get data from JSON
        self.rawPayload = unquote(self.subprotocolList[1])
        self.subprotocolPayload = json.loads(
            self.rawPayload.replace("'", "\""))

        if("flag" not in self.subprotocolPayload):
            tmpFailSwitch = True

        if(self.subprotocolPayload["flag"] != "SYN"):
            tmpFailSwitch = True

        # Check if Camera has a cameraid
        if("cameraid" not in self.subprotocolPayload):
            tmpFailSwitch = True

        # If there is a fail
        if (tmpFailSwitch):
            op.printLog(
                logType="ERROR", messageStr="On parsing SJMP Subprotocol Request, in WebSocketSJMPRequestHandler.setupCamera()")
            tmpSessionId = str(hashlib.md5((self.client_address[0] + ":" + str(
                self.client_address[1]) + ":" + str(datetime.now(timezone.utc))).encode()).hexdigest())
            tmpCamera = self.server.camerasManager.createOrGetCamera(
                protocolClass=protocolClass, ip=self.client_address[0], port=self.client_address[1], cameraid=None, sessionid=tmpSessionId)
            return tmpCamera

        cameraid = self.subprotocolPayload["cameraid"]

        tmpSessionId = str(hashlib.md5((self.client_address[0] + ":" + str(self.client_address[1]) + ":" + str(
            datetime.now(timezone.utc)) + "cameraid=["+cameraid+"]").encode()).hexdigest())

        tmpCamera = self.server.camerasManager.createOrGetCamera(
            protocolClass=protocolClass, ip=self.client_address[0], port=self.client_address[1], cameraid=cameraid, sessionid=tmpSessionId)

        return tmpCamera


class WebSocketSJMPServer(WebSocketServer):
    """
    # Web Socket SJMP Server

    inherits from ```WebSocketServer``` 


    Description ::
    -----------

    Defines the multithread server structure and workflow using Web Socket SJMP.
    """
    # Defines server cameras manager

    def getCamerasManager(self):
        return BaseCameraManager(cameraprotocolClass="camera.WebSocketSJMPCamera.WebSocketSJMPCamera")

    # Defines the server request handler type
    def getServerRequestHandler(self):
        return WebSocketSJMPRequestHandler
