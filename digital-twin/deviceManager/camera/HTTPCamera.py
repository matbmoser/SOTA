# coding=UTF-8
from operators.op import op, op

from camera.TCPCamera import TCPCamera


class HTTPCamera(TCPCamera):
    '''
    # HTTP Camera

    inherits from ```TCPCamera``` 


    Description ::
    ---------- 

    Class that contains the Camera HTTP logic.
    
   
    Input ::
    -----

    :attr str ip: Contains the ip from Camera.

    :attr int port: Contains the port from Camera.

    :attr str socketkey: Contains the socket key (ip:port)

    :attr str cameraid: Contains the Camera identification unique key

    :attr str sessionid: Contains the Camera session identification unique key
    
    :attr str type: Contains the type of camera/the function designated (add cars of delete cars, or both) ["ENTRY", "EXIT", "BOTH"] default: BOTH

    Uses HTTP Protocol.

    '''

    def __init__(self, ip, port, cameraid=None, sessionid=None, type="BOTH"):
        super().__init__(ip=ip, port=port, cameraid=cameraid, sessionid=sessionid, type=type)

    # Sets the protocol from Camera
    def getProtocol(self):
        return op.createClass("protocols.HTTPProtocol.HTTPProtocol")

    # ================================================================
    # BUFFER AND MESSAGE METHODS

    # -------------------------------------------------
    # INPUT BUFFER
    # -------------------------------------------------

    # GET
    def getInputBuffer(self, sep=""):

        tmpBuffer = ""

        # Extract information from HTTP body and create string
        for httpMessage in self.inputBuffer:
            tmpBuffer += httpMessage.body

        # Clear the buffer
        self.clearInputBuffer()
        return tmpBuffer
