# coding=UTF-8
from camera.BaseCameraManager import BaseCameraManager
from server.TCPSJMPServer import TCPSJMPRequestHandler, TCPSJMPServer


class HTTPRequestHandler(TCPSJMPRequestHandler):
    """
    # HTTP Request Handler
    
    inherits from ```TCPSJMPRequestHandler```

    Description ::
    -----------
    
    Defines the connection flow of a HTTP Request handler.
        
    """
    ### ================================================================
    ### CONNECTION START/SETUP METHODS
    
    ## Identify the protocol connection message type.
    def identifyConnectionProtocol(self):
        # Get last protocol
        tmpCamera = super().identifyConnectionProtocol()
        
        ## If is not TCPCamera
        if(tmpCamera != "camera.TCPCamera.TCPCamera"):
            return tmpCamera

        tmpLenRequest=len(self.connectionData)
        # Check minumum HTTP message len 
        if(tmpLenRequest < 3):
            return tmpCamera
        try:
            # Check if method is in the valid methods list
            method = str(self.connectionData[0:3],'utf-8').upper()
            
            if method in ["GET","POST"]:
                return "camera.HTTPCamera.HTTPCamera"
        except:
            pass

        return tmpCamera
    
    ## Setups the Camera using the protocol
    def setupCamera(self,protocolClass):
        return super().setupCamera(protocolClass=protocolClass)
    


class HTTPServer(TCPSJMPServer):
    """
    # HTTP Server
    
    inherits from ```TCPSJMPServer``` 

    Description ::
    -----------
    
    Defines the multithread server structure and workflow using HTTP.
    """
    
    ### ================================================================
    ### SETUP METHODS
    
    ## Defines server cameras manager 
    def getCamerasManager(self):
        return BaseCameraManager(cameraprotocolClass="camera.HTTPCamera.HTTPCamera")
    
    ## Defines the server request handler type
    def getServerRequestHandler(self):
        return HTTPRequestHandler