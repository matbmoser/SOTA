# coding=UTF-8
from operators.op import op
from camera.Camera import Camera

class TCPCamera(Camera):
    '''
    # TCP Camera

    inherits from ```Camera```

    Description ::
    ---------- 
    
    Class that contains a TCP Camera information, status and op.
         
    Input ::
    -----
    
    :attr str ip: Contains the ip from Camera.
    
    :attr int port: Contains the port from Camera.
    
    :attr str socketkey: Contains the socket key (ip:port)
    
    :attr str cameraid: Contains the Camera identification unique key
    
    :attr str token: Contains the Camera session identification unique key
        
    [More Attributes can be added]
    '''
    def __init__(self, ip, port, cameraid=None, token=None):
        super().__init__(ip=ip, port=port, cameraid=cameraid, token=token)

    ## Sets the protocol from Camera
    def getProtocol(self):
        return op.createClass("protocols.TCPProtocol.TCPProtocol")

    ### ================================================================
    ### BUFFER AND MESSAGE METHODS
    
    ## -------------------------------------------------
    ## INPUT BUFFER
    ## ------------------------------------------------- 
    
    ## GET
    def getInputBuffer(self,sep=""):
        
        tmpBuffer = ""

        # Concat data data from inputbuffer TCPMessages
        for tcpMessage in self.inputBuffer:
            tmpBuffer += tcpMessage.content

        self.clearInputBuffer()
        return tmpBuffer
    
