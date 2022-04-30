const online = new Event("isonline");

async function newCamera(cameraid, ip, port) {
    camera = new CameraClient(cameraid);
    camera.type = "BOTH";
    camera.start(ip, port);
}

async function createAndConnectCamera(cameraid, ip, port) {
  if (cameraid != "" && cameraid != "" && port >= 0 && port <= 65535) {
    lockConfig();
    await newCamera(cameraid, ip, port);
  } else {
    alert("[ERROR] Please insert all values!");
  }
}



