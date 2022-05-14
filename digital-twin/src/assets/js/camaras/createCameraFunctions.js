
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

function connectToServer() {
  let rawServer = localStorage.getItem("serverInfo");
  if (rawServer != null && rawServer != undefined && rawServer != "") {
    server = JSON.parse(rawServer);
    let ip = CONFIGS["defaultIP"];
    let port = server["port"];
    let cameraid = uuidv4();
    createAndConnectCamera(cameraid, ip, port);
    return;
  }
  let tmpCameraid = localStorage.getItem("cameraid");
  if (tmpCameraid == null || tmpCameraid == undefined || tmpCameraid == "") {
    tmpCameraid = uuidv4();
  }
  localStorage.setItem("cameraid", tmpCameraid);
  let cameraid = tmpCameraid
  let ip = CONFIGS["defaultIP"];
  let port = document.getElementById("cameraServerPort").value;
  createAndConnectCamera(cameraid, ip, port);
}

function disconnectFromServer() {
  camera.close()
  stopMessage();
  localStorage.removeItem("cameraid");
  localStorage.removeItem("cameraStatus");
}