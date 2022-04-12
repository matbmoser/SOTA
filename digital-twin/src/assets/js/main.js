var submit = document.getElementById('submit');
var submitconf = document.getElementById('submitconf');
var sendmessage = document.getElementById('sendmessage');
var disconnect = document.getElementById('disconnect');
var clean = document.getElementById('clean');
var nom = "";
var output = document.getElementById("output");;

submit.onclick = function() {
    var cameraid = document.getElementById("name").value;
    if (cameraid != ""){
        document.getElementById("nmess").innerText = "Your ClientId is: ";
        document.getElementById("name").disabled = true;
        submit.classList.add("hidden");
        document.getElementById("config").classList.remove("hidden");
    }else{
        alert("[ERROR] Please insert a name!");
    }
}


submitconf.onclick = function(){
    let cameraid = document.getElementById("name").value;
    let ip = document.getElementById("ip").value;
    let port = document.getElementById("port").value;
    if (ip == ""){
        ip = DEFAULTSERVERIP;
        document.getElementById("ip").value = ip;
    }
    if (port == ""){
        port = DEFAULTSERVERPORT;
        document.getElementById("port").value = port;
    }
    createAndConnectClient(cameraid, ip, port)
    
}

sendmessage.onclick = function(){
    let destinationClientid = document.getElementById("client").value; // Message Text Field Value
    let message = document.getElementById("message").value; // Message Text Field Value
    
    if (message != ""){
        client.sendMessageToClient(destinationClientid,message)
    }else{
        alert("[ERROR] Please insert a message!");
    }
    
}

clean.onclick = function(){
    cleanOutput();
}

disconnect.onclick = function(){
    client.close()
    stopMessage();
}