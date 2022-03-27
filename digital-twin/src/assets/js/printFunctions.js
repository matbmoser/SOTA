
async function cleanOutput(){
  document.getElementById("output").innerHTML = "";
}
async function setOnline(){
  document.getElementById("status").innerHTML = '<span class="alert-online">ONLINE</span>';
  // Dispatch the event.
  document.dispatchEvent(online);
}
async function setConnected(){
  document.getElementById("status").innerHTML = '<span class="alert-connected">CONNECTED</span>';
}
async function setConnecting(){
  document.getElementById("status").innerHTML = '<span class="alert-fail">CONNECTING</span>';
}
async function setOffline(){
  document.getElementById("status").innerHTML = '<span class="alert-danger">DISCONNECTED</span>';
}

async function unlockConfig(){
  document.getElementById("name").removeAttribute("disabled");
  document.getElementById("ip").removeAttribute("disabled");
  document.getElementById("port").removeAttribute("disabled");
}
async function lockConfig(){
  document.getElementById("name").disabled = true;
  document.getElementById("ip").disabled = true;
  document.getElementById("port").disabled = true;
}

async function stopMessage(){
  document.getElementById("response").classList.add("hidden"); //Hide response fields
  submitconf.classList.remove("hidden"); //Remove Hidden from connect buttom
  sendmessage.classList.add("hidden"); //Hide sendmessage buttom
}

async function startMessage(){
  document.getElementById("response").classList.remove("hidden"); //Unlock response fields 
  submitconf.classList.add("hidden"); //Hide submit buttom
  sendmessage.classList.remove("hidden"); //Unlock send button
}

async function writeToScreen(message) {
  var pre = document.createElement("p"); 
  pre.style.wordWrap = "break-word"; 
  pre.innerHTML = message; 
  output.appendChild(pre);
}

async function writeToScreenSpan(message) {
  var pre = document.createElement("span"); 
  pre.style.wordWrap = "break-word"; 
  pre.innerHTML = message; 
  output.appendChild(pre);
}