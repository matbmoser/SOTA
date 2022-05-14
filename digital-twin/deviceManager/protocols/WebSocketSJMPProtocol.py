# coding=UTF-8
import os
import sys
import traceback

from datetime import datetime, timezone
from operators.op import op
from protocols.WebSocketProtocol import WebSocketHTTPRequest, WebSocketHTTPResponse, WebSocketProtocol, WebSocketMessage
from protocols.SJMPHandler import handler, packet

import copy


class WebSocketSJMPProtocol(WebSocketProtocol):
    """
    # Web Socket SJMP Protocol

    inherits from ```WebSocketProtocol```

    Description ::
    -----------

    Defines the work flow and treatment of the information in Web Socket SJMP.

    Input ::
    -----

    :attr int buffer: Defines the amount of data that is received by the socket.


    """

    def __init__(self, buffer=2048):
        super().__init__(buffer=buffer)

    # ================================================================
    # MESSAGE HANDLE METHODS

    # Returns the message type and configures the request
    def getMessage(self, input=None):
        if self.acceptKey == None:
            res = WebSocketHTTPRequest(rawdata=input)
        elif not self.handshakeCompleted:
            res = WebSocketSJMPHTTPResponse(rawdata=input)
        else:
            res = WebSocketMessage(rawdata=input)
        return res

    # Prepares and returns a close message
    def getCloseMessage(self):
        return self.newMessage(FIN=0b1, OPCODE=0x8, PAYLOAD=packet().dumpPacket(flag="FIN", message="Server is Shutdown").messageToJSONString())

    # ================================================================
    # INPUT MESSAGE

    def processInputMessage(self):
        try:
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

                    # Add raw infomation in his outputmessage
                    res = self.camera.addOutputMessage(value=tmpOutputMessage)
                    if (not res):
                        return False

                # Clear input messages
                self.camera.clearInputMessages()

                # If there was messages they will be sent, if not we make nothing
                return True
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="SJMPProtocol.processInputMessage()")
            traceback.print_exc()

            return False


class WebSocketSJMPHTTPResponse(WebSocketHTTPResponse):
    """
    # Web Socket SJMP HTTP Response Message

    inherits from ```WebSocketHTTPResponse```

    Description ::
    ---------- 

    Defines the structure of WebSocket SJMP HTTP protocol response message.

    Input ::
    -----

    :attr bytes rawdata: Contains the incoming data of the protocol socket connection.

    """

    def __init__(self, rawdata=None):
        super().__init__(rawdata=rawdata)

    # Generates the subprotocol using the SJMP Protocol
    def generateSubprotocolResponse(self, subprotocol=None, sessionid=""):
        # Sub protocol configuration

        # If in the handshake we include a subprotocol we must return it
        if(subprotocol != None):
            self.subprotocol = subprotocol

        # SJMP OK flag response
        if self.subprotocol == "SJMP":
            self.subprotocolResponse = packet().dumpPacket(flag="OK", srv_time=str(
                datetime.timestamp(datetime.now(timezone.utc))), sessionid=sessionid).messageToJSONString()

        return
