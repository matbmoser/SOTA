# coding=UTF-8
import traceback
from operators.op import op
import copy
from datetime import datetime, timezone

from protocols.SJMPHandler import handler, packet
from protocols.TCPProtocol import TCPProtocol


class TCPSJMPProtocol(TCPProtocol):
    def __init__(self, buffer=2048):
        super().__init__(buffer=buffer)

    # ================================================================
    # MESSAGE HANDLE METHODS

    # Prepares and returns a connection message
    def getConnectionMessage(self, camera):
        token=camera.publicKey.decode("utf-8")
        print(token)
        print(type(token))
        return self.newMessage(content=packet().dumpPacket(flag="SYN", cameraid=camera.cameraid, clt_time=datetime.timestamp(datetime.now(timezone.utc)), token=token, type=camera.type).messageToJSONString())

    # Prepares and returns a close message
    def getCloseMessage(self):
        return self.newMessage(content=packet().dumpPacket(flag="FIN", response="Connection Closed! Server shutdown").messageToJSONString())

    # ================================================================
    # INPUT MESSAGE

    def processInputMessage(self):
        try:

            # [HINT]: [Implement here your logic if you need to treat the incoming information]
            #
            # #
            # Count the number of messages to send
            tmpInputMessageLen = self.camera.getLenInputMessages()

            # If there are messages to send
            if (tmpInputMessageLen > 0):
                # To parse and process the packets we use a SJMPHandler
                packetHandler = handler(handler=self.handler)
                try:
                    # Try to copy the message received
                    tmpInputMessages = copy.deepcopy(self.camera.inputMessages)
                    self.camera.clearInputMessages()
                except Exception:  # In case is imposible to copy the class
                    # Add the original value
                    tmpInputMessages = self.camera.inputMessages

                for inputMessage in tmpInputMessages:

                    # Generate a output or not depending in the flag
                    tmpOutputMessage = packetHandler.processPacket(
                        rawPacket=inputMessage)

                    # If we not need to return information to the Camera
                    if (tmpOutputMessage == None):
                        continue

                    res = self.camera.addOutputMessage(value=tmpOutputMessage)
                    if (not res):
                        return False

                # Clear output messages
                self.camera.clearInputMessages()

            # If there was messages they will be sent, if not we make nothing
            return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="TCPSJMPProtocol.processInputMessage()")
            traceback.print_exc()
            return False
