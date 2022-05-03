
var camera = null;
async function newCamera(cameraid, ip, port) {
    camera = new CameraClient(cameraid);
    camera.type = "BOTH";
    camera.start(ip, port, camera);
}

async function createAndConnectCamera(cameraid, ip, port) {
  if (cameraid != "" && cameraid != "" && port >= 0 && port <= 65535) {
    await newCamera(cameraid, ip, port);
  } else {
    alert("[ERROR] Please insert all values!");
  }
}

async function reconnectCamara(server){
  let cameraid = localStorage.getItem("cameraid");
  if (cameraid == null || cameraid == undefined || cameraid == "") {
    return false;
  }
  createAndConnectCamera(cameraid, CONFIGS["defaultIP"], server["port"])
}

