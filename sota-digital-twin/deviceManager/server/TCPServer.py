# coding=UTF-8
from camera.BaseCameraManager import BaseCameraManager

from server.Server import RequestHandler, Server
  

class TCPRequestHandler(RequestHandler):
    """
    # TCP Request Handler
    
    inherits from ```BaseRequestHandler```
    

    Description ::
    -----------
    
    Defines the connection flow of a TCP Request handler.
        
    """
    ### ================================================================
    ### CONNECTION START/SETUP METHODS
    
    ## Identify the protocol connection message type.   
    def identifyConnectionProtocol(self):
        return "camera.TCPCamera.TCPCamera"
    
    ## Setups the Camera using the protocol
    def setupCamera(self,protocolClass):
        return super().setupCamera(protocolClass=protocolClass)


class TCPServer(Server):
    """
    # TCP Server
    
    inherits from ```Server``` 
    

    Description ::
    -----------
    
    Defines the multithread server structure and workflow using TCP.
    """
    ## Defines server cameras manager    
    def getCamerasManager(self):
        return BaseCameraManager(cameraprotocolClass="camera.TCPCamera.TCPCamera")

    ## Defines the server request handler type
    def getServerRequestHandler(self):
        return TCPRequestHandler