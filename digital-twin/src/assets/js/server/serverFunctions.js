function closeServer(port) {
    ServerConnectionManager.close(port);
}
function openServer(port) {
    ServerConnectionManager.open(port);
}
function getServer(port) {
    ServerConnectionManager.get(port);
}
function printServerStatus(data){
    let monitor = document.getElementById("monitor");
    monitor.innerHTML = `<span style="color:green">Servidor [`+data["name"].toString()+`] Abierto en IP=[`+data["ip"].toString()+`], PORT=[`+data["port"].toString()+`] y PID=[`+data["pid"].toString()+`]  </span>`
    printServerData(data)
}
function printServerData(data){
    let serverData = document.getElementById("serverData");
    serverData.classList.add("alert-online")
    serverData.innerHTML = `<span style="color:white">
    <strong>SERVERID</strong>: `+data["name"].toString()+` 
    <br>
    <strong>IP</strong>: `+data["ip"].toString()+`
    <br>
    <strong>PORT</strong>: `+data["port"].toString()+`
    <br>
    <strong>PID</strong>: `+data["pid"].toString()+`
    </span>`
}
function closeServerByPort(){
    let data = JSON.parse(localStorage.getItem("serverInfo"));
    let monitor = document.getElementById("monitor");
    monitor.innerHTML = `<span style="color:#dc3545"><div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div>Cerrando Servidor [`+data["name"].toString()+`] Abierto en IP=[`+data["ip"].toString()+`], PORT=[`+data["port"].toString()+`] y PID=[`+data["pid"].toString()+`]  </span>`
    closeServer(data["port"]);
}
function openServerByPort(){
    var ipPattern = "#ip-pattern";
    var portPattern = "#port-pattern";
    let ip = $(ipPattern).val();
    let port = $(portPattern).val();
    let monitor = document.getElementById("monitor");
    localStorage.setItem("serverStatus", "CONNECTING");
    refreshServerStatus();
    monitor.innerHTML = `<span style="color:#0d6efd"><div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Abriendo Servidor en IP=[`+ip.toString()+`] y PORT=[`+port.toString()+`]</span>`
    openServer(port);
}

function handleOpen(response){
    try{
      var data = JSON.parse(response)["server"];
      localStorage.setItem("serverInfo",JSON.stringify(data));
      localStorage.setItem("serverStatus", "RUNNING");
      printServerStatus(data);
      $("#cameraServerPort").val(data["port"]);
      blockAddServer();
    }catch(e){
        console.log(e);
        localStorage.setItem("serverStatus", "FAIL");
        localStorage.removeItem("serverInfo")
    }
  }
    //Check if server is alive
function checkIfServerIsAlive(response){
    var parsedResponse = JSON.parse(response);
    if(parsedResponse["success"] === "true"){
        var server = parsedResponse["server"];
        localStorage.setItem("serverInfo", JSON.stringify(server));
        printServerStatus(server);
        localStorage.setItem("serverStatus", "RUNNING");
        $("#port-pattern").val(server["port"]);
        $("#cameraServerPort").val(server["port"]);
        blockAddServer();
        reconnectCamara(server);
        return true;
    }

    localStorage.setItem("serverStatus", "STOPPED");
    refreshServerStatus();
    localStorage.removeItem("cameraid");
    localStorage.removeItem("serverInfo");
    unblockAddServer();
    return false;
}

function getServerStatus(){
    let rawServer = localStorage.getItem("serverInfo");
    if(rawServer != null && rawServer != undefined && rawServer != ""){
        server = JSON.parse(rawServer);
        getServer(server["port"]);
    }else{
        localStorage.removeItem("serverInfo");
        unblockAddServer();
    }
}
function replaceForm(){
    let serverData = document.getElementById("serverData");
    serverData.classList.remove("alert-online");
    serverData.innerHTML = `<div class="mb-3">
    <label for="ip-pattern" class="col-form-label">IP:</label>
    <input type="text" value="127.0.0.1" class="form-control" id="ip-pattern" disabled required></div>
    <div class="mb-3"><label for="port-pattern" class="col-form-label">PORT:</label>
        <input type="number" id="port-pattern" min="1" max="65535" class="form-control" required>
    </div>`
    var minPort = 1;
    var maxPort = 65535;
    var portPattern = "#port-pattern";
    $(portPattern).val(randomIntFromInterval(minPort, maxPort));

}
function handleClose(response){
    var data = JSON.parse(response)["success"];
    if (data === "true"){
        localStorage.removeItem("serverInfo")
        localStorage.setItem("serverStatus", "STOPPED");
        overwriteMonitor("");
        replaceForm();
        unblockAddServer();
    }else{
        localStorage.setItem("serverStatus", "FAIL");
        unblockAddServer();
    }
}
//RefeshServerStatus
function refreshServerStatus(){
    //checkServerStatus();
    let status = localStorage.getItem("serverStatus");
    let content = "";
    switch (status){
        case "FAIL":
        content = '<span class="alert-fail">FAIL</span>';
        localStorage.setItem("serverStatus", "STOPPED");
        break;
        
        case "RUNNING":
        content = '<span class="alert-connected">RUNNING</span>';
        break;
        
        case "STOPPED":
        content = '<span class="alert-danger">STOPPED</span>';
        break;

        default:
            content = '<span class="alert-danger">STOPPED</span>';

    }
    document.getElementById("status").innerHTML = content;
}

// Block Access To Server Configurations
function blockAddServer(){
    var openServerButton = document.getElementById("openserver");
    var defaultPortButton= document.getElementById("defaultPort");
    var randomPortButton = document.getElementById("randomPort");
    var openButton = document.getElementById("open");
    var closeButton = document.getElementById("close");
    var connectCamera = document.getElementById("connectCamera");

    connectCamera.classList.remove("hidden");
    openServerButton.innerHTML = "Close Server";
    openButton.classList.add("hidden");
    closeButton.classList.remove("hidden");
    openServerButton.classList.remove("btn-warning");
    openServerButton.classList.add("btn-danger");
    openButton.classList.remove("btn-success");
    openButton.classList.add("btn-danger");
    randomPortButton.classList.add("hidden");
    defaultPortButton.classList.add("hidden");
    $("#port-pattern").attr('disabled','disabled');
    refreshServerStatus();
  }

  
// Block Access To Server Configurations
function unblockAddServer(){
    var openServerButton = document.getElementById("openserver");
    var defaultPortButton= document.getElementById("defaultPort");
    var randomPortButton = document.getElementById("randomPort");
    var openButton = document.getElementById("open");
    var closeButton = document.getElementById("close");
    var connectCamera = document.getElementById("connectCamera");

    connectCamera.classList.add("hidden");
    openServerButton.innerHTML = "Open Server";
    openButton.classList.remove("hidden");
    closeButton.classList.add("hidden");
    openServerButton.classList.add("btn-warning");
    openServerButton.classList.remove("btn-danger");
    openButton.classList.add("btn-success");
    openButton.classList.remove("btn-danger");
    randomPortButton.classList.remove("hidden");
    defaultPortButton.classList.remove("hidden");
    $("#port-pattern").removeAttr('disabled');
    refreshServerStatus();
  }


