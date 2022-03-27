# coding=UTF-8
from operators.op import op
from camera.TCPCamera import TCPCamera
from camera.socket.SocketCamera import SocketCamera
from SocketCamerasHandler import SocketCamerasHandler


class TCPSocketCamera(SocketCamera, TCPCamera):
    '''
    # TCP Socket Camera 

    inherits from ```BaseSocketCamera``` and ```TCPCamera``` 

    ```Abstract Class```

    Description ::
    ---------- 

    Class that contains a TCP socket Camera logic.

    Input ::
    -----

    :attr str serverip: Contains the ip from server that Camera is connected to.

    :attr int serverport: Contains the port from server that Camera is connected to.

    :attr str serverkey: Contains the server socket key (ip:port) that Camera is connected to.

    :attr str socket: Contains the socket object that handles the TCP connection.

    :attr str socketkey: Contains the Camera socket key (ip:port).

    :attr str handler: Contains the handler of the connection flow [SocketCameraHandler]

    :attr str thread: Contains the thread that listens and processes requests.

    :attr str sendingThread: Contains the thread that prepares and sends messages to the server.

    [More Attributes can be added]
    '''

    def __init__(self, serverip, serverport, ip="", port="", cameraid=None, token=None):
        super().__init__(serverip=serverip, serverport=serverport,
                         ip=ip, port=port, cameraid=cameraid, token=token)

    # Gets the handler of connection
    def getHandler(self):
        return SocketCamerasHandler(camera=self)

    # Sends message to server
    def sendMessageToServer(self, message):
        self.addOutputMessage(message)
