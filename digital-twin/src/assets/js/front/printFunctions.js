const online = new Event("isonline");
async function cleanOutput(){
  document.getElementById("cameraMonitor").innerHTML = "";
}


async function setOnline(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-online">ONLINE</span>';
  // Dispatch the event.
  document.dispatchEvent(online);
}

async function setConnected(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-connected">CONNECTED</span>';
  blockCameraAccess();
}

async function setConnecting(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-fail">CONNECTING</span>';
}

async function setOffline(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-danger">DISCONNECTED</span>';
  unblockCameraAccess();
}

// Block Access To Server Configurations
function blockCameraAccess() {

  var openButton = document.getElementById("openCamera");
  var closeButton = document.getElementById("closeCamera");
  var connectCamera = document.getElementById("connectCamera");

  connectCamera.innerHTML = "Disconnect Camera";
  openButton.classList.add("hidden");
  closeButton.classList.remove("hidden");
}


// Block Access To Server Configurations
function unblockCameraAccess() {
  var openButton = document.getElementById("openCamera");
  var closeButton = document.getElementById("closeCamera");
  var connectCamera = document.getElementById("connectCamera");

  connectCamera.innerHTML = "Connect Camera";
  openButton.classList.remove("hidden");
  closeButton.classList.add("hidden");
  cleanOutput();
}


async function stopMessage(){
// BLOCK ENVIO MATRICULAS
}

async function startMessage(){
 // UNBLOCK ENVIO MATRICULAS
}

async function writeToScreen(data) {
  var pre = document.createElement("p");
  pre.style.wordWrap = "break-word";
  pre.innerHTML = data;
  document.getElementById("cameraMonitor").appendChild(pre);
}

async function overwriteScreen(data) {
  let monitor = document.getElementById("cameraMonitor");
  monitor.innerHTML = data;
}


async function writeToScreenSpan(message) {
  var pre = document.createElement("span"); 
  pre.style.wordWrap = "break-word"; 
  pre.innerHTML = message; 
  document.getElementById("cameraMonitor").appendChild(pre);
}