# coding=UTF-8
from operators.op import op

from camera.BaseCameraManager import BaseCameraManager
from server.HTTPServer import HTTPRequestHandler, HTTPServer
from protocols.HTTPProtocol import HTTPMessage

class WebSocketRequestHandler(HTTPRequestHandler):
    """
    # Web Socket Request Handler
    
    inherits from ```HTTPRequestHandler```
    

    Description ::
    -----------
    
    Defines the connection flow of a Web Socket Request handler.
        
    """
    ### ================================================================
    ### CONNECTION START/SETUP METHODS
    
    ## Sets up the connection data.
    def setup(self):
        self.extensions = None
        return super().setup()
    
    ## Identify the protocol connection message type.
    def identifyConnectionProtocol(self):
        # Get last protocol
        tmpCamera = super().identifyConnectionProtocol()
        
        # If Camera is TCP there is no HTTP headers
        if tmpCamera != "camera.HTTPCamera.HTTPCamera":
            return tmpCamera

        # Check if HTTP headers has WebSocket Protocol Handshake
        self.parsedConnectionData = {}
        tmpParsedMessage = HTTPMessage().loadData(data=self.connectionData)
        
        if tmpParsedMessage == None:
            return tmpCamera
        
        ## Store the parsed data
        self.parsedConnectionData = tmpParsedMessage
        
        ## If the upgrade is not in the headers
        if not ("Upgrade" in self.parsedConnectionData.headers):
            return tmpCamera
        
        ## If the upgrade field is not websocket is HTTP
        if self.parsedConnectionData.headers["Upgrade"] != "websocket":
            return tmpCamera
        
        ## If it includes extensions
        if ("Sec-WebSocket-Extensions" in self.parsedConnectionData.headers):
            self.extensions = self.parsedConnectionData.headers["Sec-WebSocket-Extensions"]
        
        return "camera.WebSocketCamera.WebSocketCamera"
    
    def setupCamera(self,protocolClass):
        return super().setupCamera(protocolClass=protocolClass)
    
    

class WebSocketServer(HTTPServer):
    """
    # Web Socket Server
    
    inherits from ```HTTPServer``` 
    

    Description ::
    -----------
    
    Defines the multithread server structure and workflow using  Web Socket.
    """
    ## Defines server cameras manager 
    def getCamerasManager(self):
        return BaseCameraManager(cameraprotocolClass="camera.WebSocketCamera.WebSocketCamera")

    ## Defines the server request handler type
    def getServerRequestHandler(self):
        return WebSocketRequestHandler