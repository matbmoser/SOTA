# coding=UTF-8
import sys
import traceback
import threading
from operators.op import op
import json
import fileinput
from datetime import datetime, timezone


from camera.BaseCameraManager import BaseCameraManager


class CameraManager(BaseCameraManager):
    '''

    # Socket Cameras Manager

    inherits form ```BaseCamerasManager```

    Description ::
    ---------- 

    Allows to manage all socket cameras with one class.

    Input ::
    -----

    :attr str cameraprotocolClass: Socket Cameras default class

    :attr list Cameras: List of cameras (inherits from BaseCamerasManager) 

    '''

    def __init__(self, cameraprotocolClass="camera.TCPSJMPSocketCamera.TCPSJMPSocketCamera"):
        super().__init__(cameraprotocolClass=cameraprotocolClass)
        # General stadistics
        self.cameraWithAllMessagesSent = 0

        # Test Vars
        self.objectiveType = None
        self.objectiveNC = None
        self.objectiveNM = None
        self.expectedMessages = 0

        # STATS VARS
        self.totalMessagesRecieved = 0
        self.totalRecieveDuration = None
        self.maxRecieveDuration = None
        self.minRecieveDuration = None
        self.totalCameras = 0
        self.totalMessagesSent = 0
        self.statsThread = None
        self.ncameras = 0
        self.totalSendTime = None
        self.maxSentDuration = None
        self.minSentDuration = None
        self.startMsgs = None
        self.finishMsgs = None
        self.processedDuration = None

    # ================================================================
    # GET METHODS

    # Creates one or more Socket Cameras
    # (Returns new Camera)
    def createCameras(self, cameraClass, serverip, serverport, baseCameraid, numCameras=1):

        # Check if the number of cameras is correct
        try:
            numCameras = int(numCameras)
            numCameras = 1 if(numCameras < 1 or numCameras ==
                              None) else numCameras
        except Exception as e:  # If it fails
            numCameras = 1

        try:

            # Set Camera id from arguments
            for i in range(0, numCameras):

                # Create Camera ID
                if(i == 0):
                    tmpCameraid = baseCameraid
                else:
                    tmpCameraid = baseCameraid+str(i)

                op.printLog(
                    logType="DEBUG", messageStr=f"Trying to start Camera [{tmpCameraid}]...")
                # Create the Camera
                tmpCamera = self.newAndConnect(
                    protocolClass=cameraClass, cameraid=tmpCameraid, serverip=serverip, serverport=serverport)

                # If was not posible to create
                if(tmpCamera == None):
                    op.printLog(
                        logType="ERROR", messageStr="Was not posible to connect with server [ip=("+serverip+"), port=("+str(serverport)+")]")
                    op.printLog(logType="DEBUG",
                                messageStr=f"Closing Camera [{tmpCameraid}]...")
                    return None

            # Calculate the number of cameras
            lenCameras = len(self.Cameras)
            op.printLog(logType="INFO",
                        messageStr=f"NEW cameras created=[{str(lenCameras)}]!")

            return self.Cameras

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="in SocketCamerasManager(). On createCameras()")
            traceback.print_exc()

    # Creates a test Camera
    def createTestCameras(self, cameraClass, serverip, serverport, baseCameraid, objectiveType, objectiveNC, objectiveNM, numCameras=1):

        try:
            numCameras = int(numCameras)
            numCameras = 1 if(numCameras < 1 or numCameras ==
                              None) else numCameras
        except:  # If it fails
            numCameras = 1

        try:
            # DEFINE OBJECTIVES
            self.objectiveType = objectiveType
            self.objectiveNC = objectiveNC
            self.objectiveNM = objectiveNM
            self.startMsgs = datetime.now(timezone.utc)

            # Set up the expected results to stop calculate statistics later.
            if(objectiveType == "RECEIVE"):
                self.messagesPerCamera = self.objectiveNM+1
                self.expectedMessages = (objectiveNM*objectiveNC)+objectiveNC
            else:
                self.messagesPerCamera = self.objectiveNM+1
                self.expectedMessages = (objectiveNM*objectiveNC)

            startPoint = int(int(self.objectiveNC)/5)
            self.controlPoints = list(
                range(startPoint, int(self.objectiveNC), startPoint))

            op.printLog(logType="INFO", messageStr="Test Camera Started Objective:["+str(objectiveType)+"];expectedMessages:["+str(self.expectedMessages)+"];expectedCameras:["+str(
                self.objectiveNC)+"];expectedMessagesPerCamera:["+str(self.messagesPerCamera)+"]; Control Points: ["+str(self.controlPoints)+"].")

            # Set Camera id from arguments
            for i in range(0, numCameras):

                # Create Camera ID
                if(i == 0):
                    tmpCameraid = baseCameraid
                else:
                    tmpCameraid = baseCameraid+str(i)

                op.printLog(
                    logType="DEBUG", messageStr=f"Trying to start Camera [{tmpCameraid}]...")
                # Create the Camera
                tmpCamera = self.newAndConnect(
                    protocolClass=cameraClass, cameraid=tmpCameraid, serverip=serverip, serverport=serverport)

                # If was not posible to create
                if(tmpCamera == None):
                    op.printLog(
                        logType="ERROR", messageStr="Was not posible to connect with server [ip=("+serverip+"), port=("+str(serverport)+")]")
                    op.printLog(logType="DEBUG",
                                messageStr=f"Closing Camera [{tmpCameraid}]...")
                    return None

            # Calculate the number of cameras
            lenCameras = len(self.Cameras)
            op.printLog(logType="INFO",
                        messageStr=f"NEW cameras created=[{str(lenCameras)}]!")

            return self.Cameras
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="in SocketCamerasManager(). On createCameras()")
            traceback.print_exc()

    # ================================================================
    # CREATE, ADD AND UPDATE METHODS

    def addCamera(self, camera):
        # Check if Camera already exists
        self.Cameras[camera.cameraid] = camera

    # Method responsible to create new Camera
    # (Returns new Camera)
    def new(self, protocolClass=None, cameraid="", serverip='127.0.0.1', serverport=8080, ip="", port="", token=None):
        if protocolClass == None:
            protocolClass = self.cameraprotocolClass

        tmpCamera = op.createClass(newClass=protocolClass, serverip=serverip,
                                   serverport=serverport, ip=ip, port=port, cameraid=cameraid, token=token)
        self.addCamera(camera=tmpCamera)
        op.printLog(logType="DEBUG", messageStr="SocketCamerasManager.new(protocolClass="+protocolClass +
                    ", cameraid=["+tmpCamera.cameraid+"], serverip=[" + serverip + "], serverport=[" + str(serverport) + "].")
        return tmpCamera

    # Method responsible to connect a Camera to server
    # (Returns the Camera if connected and None if not)
    def newAndConnect(self, protocolClass=None, cameraid=None, serverip='127.0.0.1', serverport=8080, token=None):

        tmpCamera = self.new(protocolClass=protocolClass, cameraid=cameraid,
                             serverip=serverip, serverport=serverport, token=token)
        res = tmpCamera.connect()
        if(res):
            op.printLog(logType="DEBUG", messageStr=tmpCamera.toString())
            tmpCamera.open()
            return tmpCamera
        elif(res == None):
            op.printLog(
                logType="ERROR", messageStr="Was not possible to connect, Camera is not configured")
        elif(not res):
            op.printLog(
                logType="ERROR", messageStr="Was not possible to connect, server does not exists!")
        return None

    # ================================================================
    # START MESSAGE SENDING METHODS

    # Start the message sending threads in the cameras depending in the parameters
    def startCameras(self, file=None, message=None, nMessages=None, cameras=None, baseDestName=None):
        try:
            for i, cameraid in enumerate(self.Cameras):

                # Get Camera by Camera id
                camera = self.getByCameraId(cameraid)

                # Check if Camera needs to send something and configure the thread
                if(file != None):
                    camera.sendingThread = threading.Thread(name=str(str(type(
                        camera))+"-"+camera.cameraid+"-"+camera.serverkey+"-"+str(file)), target=self.startFileCamera, args=[camera, file])
                elif(cameras != None):
                    camera.sendingThread = threading.Thread(name=str(str(type(camera))+"-"+camera.cameraid+"-"+camera.serverkey+"-"+str(
                        cameras)), target=self.startTestCamera, args=[camera, cameras, message, nMessages])
                elif(baseDestName != None):
                    # Sets the destination ids
                    if (i == 0):
                        cameraid = baseDestName
                    else:
                        cameraid = baseDestName+str(i)

                    camera.sendingThread = threading.Thread(name=str(str(type(camera))+"-"+camera.cameraid+"-"+camera.serverkey+"-"+str(
                        cameraid)), target=self.startTestCamera, args=[camera, [cameraid], message, nMessages])
                else:
                    camera.sendingThread = threading.Thread(name=str(str(type(
                        camera))+"-"+camera.cameraid+"-"+camera.serverkey+"-stdin"+str(i)), target=self.startCamera, args=[camera])

                # Start Sending
                if(camera.sendingThread != None):
                    op.printLog(
                        logType="DEBUG", messageStr=f"Camera [{camera.cameraid}] started sending messages in thread [{camera.sendingThread._name}]")
                    camera.sendingThread.setDaemon = True
                    camera.sendingThread.start()
                    continue

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="in SocketCamerasManager(). On startCameras()")
            traceback.print_exc()

    # ================================================================
    # CAMERAS MANAGER CONNECTION HANDLERS METHODS
    # START AND STOP METHODS

    # Starts a Camera and reads from STDIN
    def startCamera(self, camera):

        # Wait for the Camera to be online
        while camera.status != "ONLINE":
            continue

        # Read file content
        keepAlive = True
        # Calculate initial time
        self.startMessages(camera=camera)

        # Go line per line sending the messages
        while keepAlive and (camera.status == "CONNECTED" or camera.status == "ONLINE"):

            # Get message from STDIN
            message = sys.stdin.readline()

            if(message.rstrip().upper() == "EXIT"):
                camera.forceClose()
                keepAlive = False
                break

            # If we arrive at the end of the file or is empty.
            if message.rstrip().upper() == "":
                # Check next line if its empty close Camera.
                nextLine = sys.stdin.readline()
                if nextLine.rstrip().upper() != "":
                    camera.addOutputMessage(value=nextLine.rstrip())
                    continue
                camera.forceClose()
                keepAlive = False
                break

            camera.addOutputMessage(value=message.rstrip())

        # Calculate final results
        self.finishMessages(camera=camera)

        op.printLog(logType="DEBUG", messageStr="Camera Closed!")

    def startFileCamera(self, camera, file):
        # Read file content
        lines = fileinput.input(files=(file), encoding="utf-8")
        # Calculate initial time
        self.startMessages(camera=camera)
        # Go line per line sending the messages
        for line in lines:
            try:
                if(line.rstrip() == ""):
                    continue
                # Try to parse JSON
                parsedLine = json.loads(line.rstrip())
                cameraid = parsedLine["cameraid"]
                message = parsedLine["message"]
                camera.sendMessageToCamera(message=message, cameraid=cameraid)
            except Exception as e:
                op.printLog(
                    logType="DEBUG", e=e, messageStr=f"SocketCamerasManager.startFileCamera(): Was not possible to parse [{line}].")
                camera.sendMessageToServer(message=message)
                continue

        # Calculate final results
        self.finishMessages(camera=camera)

    def startTestCamera(self, camera, cameras=None, message=None, nMessages=None):
        # Wait for the Camera to be online
        while camera.status != "ONLINE":
            continue
        # Calculate initial time
        self.startMessages(camera=camera)
        try:
            # Check vars
            if(cameras == None):
                return
            if(nMessages == None):
                nMessages = 1
            try:
                nMessages = int(nMessages)
            except:
                repnMessageseat = 1

            # If we want to send messages form a batch file
            if(message == None):
                message = "This is a test message 1234"

            # Send message from Camera to cameras
            for tmpCamera in cameras:
                for i in range(0, nMessages):
                    camera.sendMessageToCamera(
                        message=message+str(i), cameraid=tmpCamera)
                self.ncameras += 1

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="in SocketCamerasManager().startTestCamera()")
            traceback.print_exc()

        # Calculate final results
        self.finishMessages(camera=camera)

    # ================================================================
    # STATISTICS/TEST METHODS
    # (Can be removed in production)

    # Initializes the camera of time
    def startMessages(self, camera):
        camera.startMessageTime = datetime.now(timezone.utc)

    # Calculates the statistics of the time of all messages and prints a result
    def finishMessages(self, camera):
        try:
            # Call messages were sent
            camera.allMessagesSent = True
            self.cameraWithAllMessagesSent += 1
            self.totalMessagesSent += camera.messagesSent

            camera.finishMessageTime = datetime.now(timezone.utc)
            camera.durationMessageTime = camera.finishMessageTime - camera.startMessageTime
            tmpDuration = camera.durationMessageTime
            if(self.totalSendTime == None):
                self.totalSendTime = tmpDuration
                self.maxSentDuration = tmpDuration
                self.minSentDuration = tmpDuration

            self.totalSendTime += tmpDuration
            if(tmpDuration > self.maxSentDuration):
                self.maxSentDuration = tmpDuration
            if(tmpDuration < self.minSentDuration):
                self.minSentDuration = tmpDuration

            lenCameras = len(self.Cameras)
            if(self.cameraWithAllMessagesSent >= lenCameras):
                self.averageMessageTime = self.totalSendTime / self.cameraWithAllMessagesSent
                op.printLog(
                    logType="STATS", messageStr=f"Messages Sent: ncameras=[{str(self.ncameras)}];messagesSent=[{str(self.totalMessagesSent)}];totalTime=[{str(self.totalSendTime)}];minSendDuration=[{str(self.minSentDuration)}];avgSendDuration=[{str(self.averageMessageTime)}];maxSendDuration=[{str(self.maxSentDuration)}]")
        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="in SocketCamerasManager(). On finishMessages()")
            traceback.print_exc()

    # Stores the results of test in server
    def storeResults(self, totalmessagesProcessed, totalduration, mintime, maxtime):
        # Add one more Camera to the ones processed
        self.totalCameras += 1
        # Store the number of messages processed
        self.totalMessagesRecieved += totalmessagesProcessed
        # If the attributes where not initialized
        if(self.totalRecieveDuration == None):
            self.totalRecieveDuration = totalduration
            self.minRecieveDuration = totalduration
            self.maxRecieveDuration = totalduration
        else:
            # Add time to the existing time
            self.totalRecieveDuration += totalduration

        # Check if the time is the minumum
        if(self.minRecieveDuration > mintime):
            self.minRecieveDuration = mintime

        # Check if time is the maximum
        if(self.maxRecieveDuration < maxtime):
            self.maxRecieveDuration = maxtime

        # If the number of cameras is in the control points.
        if(self.totalCameras in self.controlPoints):
            # Calculate the porcentage of completed process
            completedPorcentage = (self.totalCameras/self.objectiveNC)*100
            actualTime = datetime.now(timezone.utc)
            # Calculate enlapsed time until now
            enlapsedTime = actualTime - self.startMsgs
            op.printLog(logType="INFO", messageStr="Test ["+str(completedPorcentage)+" %%] completed! ["+str(
                self.totalMessagesRecieved)+"] from ["+str(self.expectedMessages)+"] Messages Received, Enlapsed Time: ["+str(enlapsedTime)+"]")

        # Check if the objective has been fullfilled
        if(self.totalCameras >= self.objectiveNC):
            # Calculate average time
            avgTime = self.totalRecieveDuration/self.totalCameras
            self.finishMsgs = datetime.now(timezone.utc)
            # Calculate total duration time
            self.processedDuration = self.finishMsgs - self.startMsgs
            op.printLog(logType="STATS", messageStr="Total Messages Processed: nmessages=["+str(self.totalMessagesRecieved)+"];mintime=["+str(self.minRecieveDuration)+"];avgtime=["+str(
                avgTime)+"];maxtime=["+str(self.maxRecieveDuration)+"];duration=["+str(self.processedDuration)+"];totaladdedtime=["+str(self.totalRecieveDuration)+"]")

    # ================================================================
    # PRINT METHODS

    # Prints a menu for cmd Camera

    def printMenu(self):
        print("\n-------------------------------------")
        print(" 1 -> Start new Camera")
        print(" 2 -> Start Default Camera")
        print(" 3 -> Disconnect Camera")
        print(" 4 -> Send Message")
        print(" 5 -> List all cameras")
        print(" 6 -> Exit")
        print("-------------------------------------\n")
        print("Choose option:\n")
        return input("[Admin\cameras\cmd] > ")

    # Prints Camera classes the options to select
    def selectCameraClass(self):

        print("\n------------[Protocols]--------------")
        print(" 1 -> TCP Camera")
        print(" 2 -> TCP SJMP Camera")
        print(" 3 -> Return")
        print("-------------------------------------\n")
        print("Choose a protocol:\n")
        opt = input("[Admin\cameras\protocols] > ")

        if(opt == "1"):
            return "camera.socket.TCPSocketCamera.TCPSocketCamera"
        elif(opt == "2"):
            return "camera.socket.TCPSJMPSocketCamera.TCPSJMPSocketCamera"
        else:
            return None

    # ================================================================
    # COMMAND LINE METHODS

    # Selects a Camera from a list of cameras
    def selectCamera(self, route=""):
        num = len(self.Cameras)
        if num < 1:
            op.printLog(
                logType="WARNING", messageStr="SocketCamerasManager.selectCamera(). None Camera was found!")
            return None

        print("\n------------[Cameras]--------------")
        tmpCameraList = list(self.Cameras)
        for i, cameraid in enumerate(tmpCameraList):
            print("[" + str(i) + "] -> " + self.Cameras[cameraid].toString())

        print("-----------------------------------\n")
        print("Choose number of Camera:\n")
        tmpCameraPos = input("[Admin\cameras"+route+"\select] > ")
        try:
            # try to parse num
            cameraPos = int(tmpCameraPos)
            if(cameraPos+1 > num):
                op.printLog(
                    logType="WARNING", messageStr="Selected Camera position not valid, try to send message again!")
                return None

            if self.Cameras[tmpCameraList[cameraPos]].status == "ONLINE":
                return self.Cameras[tmpCameraList[cameraPos]]

        except Exception as e:
            op.printLog(logType="EXCEPTION", e=e,
                        messageStr="SocketCamerasManager.selectCamera() Camera Already Selected, or does not exist")
            traceback.print_exc()

        return None

    # Opens the command line to create the cameras
    def commandLine(self, defaultip, defaultport):
        while True:
            opt = self.printMenu()
            try:
                numopt = int(opt)

                # Create new Camera
                if (numopt == 1):
                    cameraid = input("Please insert Camera id: ")

                    if(cameraid == ""):
                        print("\n[ERROR] A Camera id needs to be specified!\n")
                        continue
                    # Server Socket Values

                    # Get server ip
                    ip = input(
                        "Please insert the Server IP [Default localhost]: ")
                    ip = ip if not ip == "" else "localhost"

                    # Get server port
                    port = input(
                        "Please insert the Server PORT [Default ("+str(defaultport)+") auto]: ")
                    try:
                        port = int(port) if not port == "" else defaultport
                        # Get port or set default if empty or invalid
                    except:
                        print("\n[ERROR] The port needs to be a int\n")
                        continue

                    # If invalid
                    if(port < 0 or port > 65535):
                        print(
                            "\n[ERROR] The port needs to be between 1 and 65534\n")
                        continue

                    # Get Camera class
                    print(
                        "Please select the Camera protocol [Default TCPCamera]: ")
                    protocolClass = self.selectCameraClass()
                    if(protocolClass == None):
                        protocolClass = "camera.socket.TCPSJMPSocketCamera.TCPSJMPSocketCamera"

                    try:
                        # Create and Start Server
                        tmpCamera = self.newAndConnect(
                            protocolClass=protocolClass, cameraid=cameraid, serverip=ip, serverport=port)
                        if not tmpCamera:
                            op.printLog(
                                logType="ERROR", messageStr="Was not possible to add a new Camera, invalid configuration!\n")
                    except Exception as e:
                        op.printLog(
                            logType="EXCEPTION", e=e, messageStr="in SocketCamerasManager(). On newAndStart()")
                        traceback.print_exc()
                    continue

                # Start Default Camera
                elif (numopt == 2):
                    # SET DEFAULT Camera CONFIGURATIONS:

                    cameraid = "DEFAULT"

                    # If Camera exists
                    if(self.getByCameraId(cameraid=cameraid) != None):
                        op.printLog(
                            logType="ERROR", messageStr="Camera already registed in the server! Create a new Camera...")
                        continue

                    protocolClass = "camera.socket.TCPSJMPSocketCamera.TCPSJMPSocketCamera"

                    try:
                        # Start new Camera
                        tmpCamera = self.newAndConnect(
                            protocolClass=protocolClass, cameraid=cameraid, serverip=defaultip, serverport=defaultport)
                        if not tmpCamera:
                            op.printLog(
                                logType="ERROR", messageStr="Was not possible to add a new Camera, invalid configuration!\n")

                    except Exception as e:
                        op.printLog(
                            logType="EXCEPTION", e=e, messageStr="in SocketCamerasManager(). On newAndStart()")
                        traceback.print_exc()

                    continue
                # Disconnect the Camera
                elif (numopt == 3):
                    tmpCamera = self.selectCamera(route="\\disconnect")

                    if (tmpCamera == None):
                        continue

                    tmpCamera.forceClose()

                # Send messages to Camera
                elif (numopt == 4):

                    print("Select a Camera to send message FROM:")
                    tmpFromCamera = self.selectCamera(
                        route="\\sendmessage\\from")
                    if (tmpFromCamera == None):
                        continue

                    print("Insert Camera ID to send message TO:")
                    tmpCameraid = input(
                        "[Admin\cameras\sendmessage\\to] > Destination cameraid: ")
                    while(tmpCameraid == ""):
                        print("Please introduce a valid cameraid!\n")
                        tmpCameraid = input(
                            "[Admin\cameras\sendmessage\\to] > Destination cameraid: ")
                    tmpMsg = input(
                        "[Admin\cameras\sendmessage\message] > Message to send: ")
                    tmpFromCamera.sendMessageToCamera(
                        cameraid=tmpCameraid, message=str(tmpMsg))
                    continue

                # Print all cameras
                elif (numopt == 5):
                    self.listCameras()

                # Exit the manager
                elif (numopt == 6):
                    self.closeCameras()
                    break

                else:
                    op.printLog(logType="ERROR",
                                messageStr="Option not found!\n")
            except Exception as e:
                op.printLog(logType="EXCEPTION", e=e,
                            messageStr="[ERROR] Option not found!\n")
                traceback.print_exc()

###### MAIN PROGRAM ######################################################################################################################################################
# Main program help


def showHelp():
    print(
        "\n***************************************\n"
        + "\nMultiple Protocol Python Camera Manager"
        + "\nby: David Graciani and Mathias Moser"
        + "\nCopyright CGI, All rights reserved"
        + "\n\n***************************************"
        + "\n\nDEFAULT PROTOCOL = ["+defaultprotocol+"]"
        + '\n\n-> IF YOU NEED HELP: '
        + '\n\n\tpy SocketCamerasManager.py -h'
        + '\n\n-> IF YOU WANT TO USE CMD: '
        + '\n\n\tpy SocketCamerasManager.py -cmd\n'
        + '\n\n-> ARGUMENTS DESCRIPTION: '
        + '\n\n\t-n [cameraid] [MANDATORY]: Camera unique identificator, can be alfanumeric.'
        + '\n\n\t-ip [ip]: IP from server to connect to.'
        + '\n\n\t-port [port]: PORT from server to connect to.'
        + '\n\n\t-f [filepath]: Messages file path. If no other params are set messages will be sent to server.'
        + '\n\t\tFile messages can use JSON format to specify the destination cameras and message: Ex: {"cameraid": "Clark", "message": "fraud tight cheese"} '
        + '\n\n\t-m [message]: If a specific messages must be sent to different cameras'
        + '\n\n\t-c [destination cameras]: Camerasid to send divided by "|". Ex: CL1|CL2|CL3.'
        + '\n\n\t-nM [Number of messages to send]: Number of messages to send'
        + '\n\n\t-dC [destination cameras base name]: If the cameras need to send to other cameras with a base destination cameraid.'
        + '\n\n\t-nC [number of cameras to create]: If we need to create multiple cameras. Will be created using the -n [cameraid] as "baseCameraid + number"'
        + '\n\n-> TEST ARGUMENTS DESCRIPTION: '
        + '\n\n\t-t [test objective can be ["SEND" or "RECEIVE"]]: When test mode with objectives is use this option.'
        + '\n\n\t-oC [nº cameras]: Number of cameras that will send information. '
        + '\n\n\t-oM [nº messages per Camera]: Number of messages sent by each Camera. '
        + '\n\n-> REQUIREMENTS: '
        + '\n\n\t[cameraid] Must be filled to open Camera.'
        + '\n\n\tIf TEST Objective is [RECEIVE]: -oC AND -oM need to be set.'
        + '\n\n\tIf TEST Objective is [SEND]: -nC AND -nM need to be set.'
        + '\n\n\tDefault Values if empty:'
        + '\n\n\t-----------------------------------------'
        + '\n\t| [-ip] = '+defaultip+'\t\t\t|'
        + '\n\t| [-port] = '+str(defaultport)+'\t\t\t|'
        + '\n\t| [-nM] = '+str(1)+'\t\t\t\t|'
        + '\n\t| [-nC] = '+str(1)+'\t\t\t\t|'
        + '\n\t| [-c] = None\t\t\t\t|'
        + '\n\t| Other Arguments = None\t\t|'
        + '\n\t-----------------------------------------\n'
    )


def main(cameraManager, arguments):

    lenArguments = len(arguments)

    # Pass all arguments to a dictionary
    args = {}
    for i in range(0, lenArguments, 2):
        try:
            args[arguments[i]] = arguments[i+1]
        except:
            args[arguments[i]] = None

    # If user want to see the help docs
    if '-h' in args:
        showHelp()
        # Print help
        return 2
    # If the user wants to open a comand line for the CameraManagers
    if "-cmd" in args:
        # To review, we define as default TCPSJMPSocketCamera
        cameraManager.commandLine(defaultip=defaultip, defaultport=defaultport)
        return 0

    # If user does not introduces the serverid
    if ("-n" not in args):
        # Show error message
        op.printLog(
            logType="ERROR", messageStr="Please introduce at least the cameraid argument to execute the Camera with default values.\n")
        # Print help
        showHelp()
        return 2

    # Get Arguments
    cameraid = args["-n"]
    # Get ip or set default if empty
    ip = args["-ip"] if("-ip" in args) else defaultip

    # Get port or set default if empty or invalid
    try:
        port = int(args["-port"]) if("-port" in args) else defaultport
    except:
        port = defaultport

    # If invalid
    if(port < 0 or port > 65535):
        port = defaultport

    # If the Camera will send messages form file
    file = args["-f"] if("-f" in args) else None

    # If there is a message to send
    message = args["-m"] if("-m" in args) else None
    # Number of times to send
    try:
        nMessages = int(args["-nM"]) if("-nM" in args) else 1
    except:
        nMessages = 1

    # If we have specific cameras to send
    cameras = None
    # Check if there are specific cameras to send
    if("-c" in args):
        tmpCameras = args["-c"]
        cameras = tmpCameras.split("|")
        nCameras = len(cameras)
        if(nCameras < 1):
            op.printLog(logType="ERROR", messageStr="If you indicate cameras to send with '-c' you must indicate at least one, if you would like to add more you can use '|', for example: -c 'camera1|camera2'")
            showHelp()
            return 2

    # Variables for creating multiple cameras and sending to multiple destination cameras
    baseDestName = args["-dC"] if("-dC" in args) else None

    # Get the number of cameras
    try:
        numCameras = int(args["-nC"]) if("-nC" in args) else 1
    except:
        numCameras = 1

    # If the user want to start the test Camera with objectives
    if ("-t" in args):
        # Test objectives
        objectiveTypes = ["RECEIVE", "SEND"]
        objectiveType = str(args["-t"]).upper()

        if(objectiveType not in objectiveTypes):
            op.printLog(
                logType="ERROR", messageStr="You must indicate a valid test type objective!\n")
            showHelp()
            return 2

        # If objetive is to recieve
        if(objectiveType == objectiveTypes[0]):
            # OBJECTIVE: NUMBER OF CAMERAS
            if("-oC" not in args):
                op.printLog(
                    logType="ERROR", messageStr="You must indicate a Camera objective number in the test Camera!\n")
                # Print help
                showHelp()
                return 2

            # Parse int
            try:
                objectiveNC = int(args["-oC"])
            except:
                op.printLog(
                    logType="ERROR", messageStr="You must indicate a valid Camera objective number in the test Camera!\n")
                # Print help
                showHelp()
                return 2

            # OBJECTIVE: MESSAGES PER Camera
            if ("-oM" not in args):
                op.printLog(
                    logType="ERROR", messageStr="You must indicate a valid objective message number!\n")
                # Print help
                showHelp()
                return 2

            # Parse int
            try:
                objectiveNM = int(args["-oM"])
            except:
                op.printLog(
                    logType="ERROR", messageStr="You must indicate a valid objective message per Camera in the test Camera!\n")
                # Print help
                showHelp()
                return 2

            # Create cameras
            cameraManager.createTestCameras(cameraClass=defaultprotocol, serverip=ip, serverport=port, baseCameraid=cameraid,
                                            numCameras=numCameras, objectiveType=objectiveType, objectiveNC=objectiveNC, objectiveNM=objectiveNM)
        # If objetive is to send
        else:
            # Set objectives
            objectiveNC = numCameras
            objectiveNM = nMessages

            # Create cameras
            cameraManager.createTestCameras(cameraClass=defaultprotocol, serverip=ip, serverport=port, baseCameraid=cameraid,
                                            numCameras=numCameras, objectiveType=objectiveType, objectiveNC=objectiveNC, objectiveNM=objectiveNM)
            # Start messages from all the cameras
            cameraManager.startCameras(
                file=file, message=message, nMessages=nMessages, cameras=cameras, baseDestName=baseDestName)
        return 0

    # Create all cameras that we need to create
    res = cameraManager.createCameras(
        cameraClass=defaultprotocol, serverip=ip, serverport=port, baseCameraid=cameraid, numCameras=numCameras)
    if(res == None):
        op.printLog(logType="CRITICAL",
                    messageStr="Was not possible to start the cameras!")
        showHelp()
        return 2

    # Start messages from all the cameras
    cameraManager.startCameras(
        file=file, message=message, nMessages=nMessages, cameras=cameras, baseDestName=baseDestName)

    return 0


if __name__ == '__main__':
    # SET DEFAULT Camera CONFIGURATIONS:
    # DEFAULT server configuration
    defaultip = "127.0.0.1"
    defaultport = 8888
    # DEFAULT Camera configurations
    defaultprotocol = "camera.socket.TCPSJMPSocketCamera.TCPSJMPSocketCamera"

    # ------
    cameraManager = CameraManager(cameraprotocolClass=defaultprotocol)

    # Start Camera
    exitCode = main(cameraManager=cameraManager, arguments=sys.argv[1:])
    sys.exit(exitCode)
