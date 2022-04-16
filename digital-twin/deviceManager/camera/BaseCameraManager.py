# coding=UTF-8
import traceback
from operators.op import op
import copy


class BaseCameraManager():

    '''

    # Base Camera Manager

    ```CAN BE OVERRIDED```

    Description ::
    ---------- 

    Allows to manage all cameras with one class.

    Input ::
    -----

    :attr str cameraprotocolClass: Cameras default class

    :attr list Cameras: List of cameras 

    '''

    def __init__(self, cameraprotocolClass="Camera.Camera"):
        # Cameras stored in the manager
        self.Cameras = {}
        # Camera default type (May be overrided)
        self.cameraprotocolClass = cameraprotocolClass

    # ================================================================
    # GET METHODS

    # Method responsible to get Camera by session id
    # (Returns Camera and None if does not exists)
    def getBySessionId(self, sessionid):
        for cameraid in self.Cameras:
            try:
                # Get Camera
                camera = self.Cameras[cameraid]
                # Check if cameraid is the same
                if camera.sessionid == sessionid:
                    return camera  # Return Camera if not
            except Exception:
                continue  # If the object has no session id

        return None

    # Method responsible to get Camera by Camera id
    # (Returns Camera and None if does not exists)
    def getByCameraId(self, cameraid):
        # If no cameraid is passed
        if cameraid == None:
            return None

        # If the Camera is in cameras
        if cameraid in self.Cameras:
            return self.Cameras[cameraid]

        return None

    # Creates or gets Camera if already exists
    # (Returns new Camera)
    def createOrGetCamera(self, protocolClass=None, ip='localhost', port=0, cameraid=None, sessionid=None):

        # Mark tmp var as none
        oldCamera = None

        try:
            # Check if Camera already exists
            if not cameraid == None:
                oldCamera = self.getByCameraId(cameraid=cameraid)

            # Camera that is connecting [Can use another protocol than the old Camera]
            newCamera = self.new(protocolClass=protocolClass,
                                 ip=ip, port=port, cameraid=cameraid, sessionid=sessionid)

            # If Camera does not exists we continue and wait for new messages
            if(oldCamera == None):
                self.addCamera(camera=newCamera)
                # Return the new Camera that was created
                return newCamera

            # Implement the cameras reconnection

            # We close the oldCamera connection if its open
            if(oldCamera.status == "ONLINE" or oldCamera.status == "CONNECTED"):
                oldCamera.forceClose()

            # Update Camera information
            reconnectedCamera = self.updateCamera(
                newCamera=newCamera, oldCamera=oldCamera)

            # If was not possible to reconnect, start the new Camera
            if reconnectedCamera == None:
                return newCamera

            # Add the new Camera
            self.addCamera(camera=reconnectedCamera)

            return reconnectedCamera

        except Exception as e:
            op.printLog(logType="CRITICAL", e=e, messageStr="\nBaseCamerasManager.createOrGetCamera(ip=" + ip + ", port=" + str(port) +
                        ", cameraid=[" + (cameraid if cameraid != None else "None") + "], sessionid=[" + (sessionid if sessionid != None else "None") + "])")
            traceback.print_exc()

        return newCamera

    # ================================================================
    # CREATE, ADD AND UPDATE METHODS

    # Method responsible to create new Camera
    # (Returns new Camera)
    def new(self, protocolClass=None, ip='localhost', port=0, cameraid=None, sessionid=None):
        # If no class type is defined use default
        if protocolClass == None:
            protocolClass = self.cameraprotocolClass
        # Create the Camera dynamicaly
        tmpCamera = op.createClass(
            newClass=protocolClass, ip=ip, port=port, cameraid=cameraid, sessionid=sessionid)
        # Add Camera to the list
        self.addCamera(camera=tmpCamera)
        # Set online
        tmpCamera.status = "ONLINE"

        return tmpCamera

    # Adds Camera in list of cameras
    def addCamera(self, camera):
        # Check if Camera already exists
        self.Cameras[camera.cameraid] = camera

    # Responsible to copy the information from a already existing Camera to a new one
    # (Returns newCamera object)
    def updateCamera(self, newCamera, oldCamera):

        # Copy values that we want to maintain
        newCamera.cameraid = copy.deepcopy(oldCamera.cameraid)
        newCamera.created = copy.deepcopy(oldCamera.created)
        newCamera.last_message = copy.deepcopy(oldCamera.last_message)

        tmpLenOutputMessages = oldCamera.getLenOutputMessages()

        # If Camera exists we check if there was messages for him
        if(tmpLenOutputMessages > 0):
            # Messages will be sent through the new connection.
            newCamera.outputMessages = copy.deepcopy(oldCamera.outputMessages)
            oldCamera.clearOutputMessages()

        # Invalidate Older Camera Session
        if(not self.deleteCameraByCameraId(cameraid=oldCamera.cameraid)):
            return None

        return newCamera

    # ================================================================
    # DELETE METHODS

    # Deletes Camera by session id
    # (RETURN TRUE IF SUCESSFULL, NONE IF NOT)
    def deleteCameraBySessionId(self, sessionid):
        for cameraid in self.Cameras:
            # TO REVIEW
            try:
                # Get Camera
                camera = self.Cameras[cameraid]
                # Check if cameraid is the same
                if camera.sessionid == sessionid:
                    # Delete Camera
                    del self.Cameras[cameraid]
                    return True
            except Exception:
                continue  # If the object has no session id

        return None

    # Deletes Camera by Camera id
    # (RETURN TRUE IF SUCESSFULL, NONE IF NOT)
    def deleteCameraByCameraId(self, cameraid):

        # Get Camera
        camera = self.getByCameraId(cameraid=cameraid)
        # If Camera exists
        if camera != None:
            # Delete Camera
            del self.Cameras[cameraid]
            return True

        return None

    # ================================================================
    # CONNECTION METHODS

    # Close all cameras in the list
    # (Returns False in Error, and True if not)
    def closeCameras(self):
        res = True
        for cameraid in self.Cameras:
            # If the Camera is already dead
            if self.Cameras[cameraid].status != "CONNECTED" and self.Cameras[cameraid].status != "ONLINE":
                continue
            res = self.Cameras[cameraid].forceClose()
            op.printLog(
                logType="DEBUG", messageStr="Camera ["+self.Cameras[cameraid].cameraid+"] KILLED!")
            # If there is a problem in closing all cameras
            if not res:
                break

        return res

    # ================================================================
    # PRINTING METHODS

    # List all cameras in the Manager Cameras List
    # (Returns the number of cameras)

    def listCameras(self):
        print("\t[Cameras] ----------------------------------------\n\t|")
        # Get the number of cameras
        num = len(self.Cameras)
        if num < 1:
            # If its empty
            op.printLog(logType="WARNING",
                        messageStr="\t| None Camera was found!")
            print("\t|\n\t--------------------------------------------------")
            return 0

        # If we have cameras
        for cameraid in self.Cameras:
            # Print cameras information
            tmpCamera = self.Cameras[cameraid]
            print("\t| " + tmpCamera.toString())

        print("\t|\n\t--------------------------------------------------")

        return num
