# coding=UTF-8
from operators.op import op, op
from camera.Camera import Camera


class WebSocketCamera(Camera):
    '''
    # Web Socket Camera

    inherits from ```BaseCamera```

    Description ::
    ---------- 

    Class that contains a Web Socket Camera information, status and op.

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
        super().__init__(ip=ip, port=port, cameraid=cameraid, sessionid=sessionid, type=type)

    # Sets the protocol from Camera
    def getProtocol(self):
        return op.createClass("protocols.WebSocketProtocol.WebSocketProtocol")

    # ================================================================
    # BUFFER AND MESSAGE METHODS

    # -------------------------------------------------
    # INPUT BUFFER
    # -------------------------------------------------

    # GET
    def getInputBuffer(self, sep=""):
        tmpBuffer = ""

        # Concat payload data from inputbuffer frames
        for frame in self.inputBuffer:
            tmpBuffer += frame.PAYLOAD

        self.clearInputBuffer()
        return tmpBuffer
