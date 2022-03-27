# coding=UTF-8
from operators.op import op
from datetime import datetime, timezone

from protocols.SJMPHandler import packet
from camera.socket.SocketCamerasHandler import SocketCamerasHandler
from camera.socket.SocketCamera import SocketCamera
from camera.TCPSJMPCamera import TCPSJMPCamera

class TCPSJMPSocketCamera(SocketCamera, TCPSJMPCamera):
    
    def __init__(self, serverip, serverport, ip="", port="", cameraid=None, token=None):
        super().__init__(serverip=serverip, serverport=serverport, ip=ip, port=port, cameraid=cameraid, token=token)
    
    def getHandler(self):
        return SocketCamerasHandler(camera=self)
    
    def connect(self):
        res = super().connect()
        # Send handshake connection
        if res:
            connectionPayload = packet().dumpPacket(flag="SYN", cameraid=self.cameraid, device_time=datetime.timestamp(datetime.now(timezone.utc)),message="Hallo, Server!").messageToJSONString()
            op.printLog(logType="DEBUG", messageStr="["+self.cameraid+"]->[SENT SJMP SYN MESSAGE]")
            self.socket.send(bytes(connectionPayload,'utf-8'))
            self.last_message = datetime.now(timezone.utc)
        return res
        
    def sendMessageToCamera(self, message, cameraid):
        message = packet().dumpPacket(srv_time=False,flag="MSG",token=self.token, cameraid=cameraid, device_time=datetime.timestamp(datetime.now(timezone.utc)),message=message).messageToJSONString()
        op.printLog(logType="DEBUG", messageStr="["+self.cameraid+"]->[SENT SJMP MSG MESSAGE]")
        self.addOutputMessage(message)
    

    def reconnect(self):
        if self.status != "OFFLINE" and self.status != "DISCONNECTED":
            op.printLog(logType="ERROR",messageStr="Was not possible to connect, Camera is online or not exists")
            return False 
        
        res = self.connect()
        if(res):
            op.printLog(logType="DEBUG", messageStr="Camera RECONNECTED:"+self.toString())
            self.open()
            return True
            
        elif(res == None):
            op.printLog(logType="ERROR",messageStr="Was not possible to connect, Camera is not configured")
        elif(not res):
            op.printLog(logType="ERROR",messageStr="Was not possible to connect, server does not exists!")
        
        return False
         
        
            