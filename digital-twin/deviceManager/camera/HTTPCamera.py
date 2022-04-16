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

    Uses HTTP Protocol.

    '''

    def __init__(self, ip, port, cameraid=None, sessionid=None):
        super().__init__(ip=ip, port=port, cameraid=cameraid, sessionid=sessionid)

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
