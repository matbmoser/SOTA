
async function cleanOutput(){
  document.getElementById("output").innerHTML = "";
}

async function setOnline(){
  document.getElementById("status").innerHTML = '<span class="alert-online">ONLINE</span>';
  // Dispatch the event.
  document.dispatchEvent(online);
}

async function setConnected(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-connected">CONNECTED</span>';
}

async function setConnecting(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-fail">CONNECTING</span>';
}

async function setOffline(){
  document.getElementById("statusCamera").innerHTML = '<span class="alert-danger">DISCONNECTED</span>';
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
  document.getElementById("output").appendChild(pre);
}

async function overwriteScreen(message) {
  var pre = document.createElement("p"); 
  pre.style.wordWrap = "break-word"; 
  pre.innerHTML = message; 
  document.getElementById("output").replaceChildren(pre)
}


async function writeToScreenSpan(message) {
  var pre = document.createElement("span"); 
  pre.style.wordWrap = "break-word"; 
  pre.innerHTML = message; 
  document.getElementById("output").appendChild(pre);
}