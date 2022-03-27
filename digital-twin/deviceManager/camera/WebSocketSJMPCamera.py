# coding=UTF-8
from operators.op import op
from camera.WebSocketCamera import WebSocketCamera

class WebSocketSJMPCamera(WebSocketCamera):
    '''
    # Web Socket SJMP Camera

    inherits from ```WebSocketCamera```

    Description ::
    ---------- 
    
    Class that contains a Web Socket SJMP Camera information, status and op.
         
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
        super().__init__(ip, port, cameraid=cameraid, token=token)
        
    ## Sets the protocol from Camera
    def getProtocol(self):
        return op.createClass("protocols.WebSocketSJMPProtocol.WebSocketSJMPProtocol")




    
        

