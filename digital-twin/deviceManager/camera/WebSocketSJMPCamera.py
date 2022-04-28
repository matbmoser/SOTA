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

    :attr str sessionid: Contains the Camera session identification unique key

    :attr str type: Contains the type of camara/the function designated (add cars of delete cars, or both) ["ENTRY", "EXIT", "BOTH"] default: BOTH

    [More Attributes can be added]
    '''

    def __init__(self, ip, port, cameraid=None, sessionid=None, type="BOTH"):
        super().__init__(ip, port, cameraid=cameraid, sessionid=sessionid, type=type)

    # Sets the protocol from Camera
    def getProtocol(self):
        return op.createClass("protocols.WebSocketSJMPProtocol.WebSocketSJMPProtocol")
