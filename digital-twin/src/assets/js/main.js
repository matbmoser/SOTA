var submitconf = document.getElementById('submitconf');
var sendmessage = document.getElementById('sendmessage');
var nom = "";
var output = document.getElementById("output");;

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

//-----------------Slide In desde la Arriba Bajo----------------
$(document).ready(function(){
    // Slide in elements on scroll
    $(window).scroll(function() {
        $(".slideanim").each(function(){
            var pos = $(this).offset().top;

            var winTop = $(window).scrollTop();
            if (pos < winTop + 600) {
                $(this).addClass("slide");
            }
        });
    });
})
//-----------------Slide In desde la Arriba Bajo----------------
$(document).ready(function() {
    $(window).scroll(function() {
        $(".RevealLeft").each(function() {
            var pos = $(this).offset().top;
            var winTop = $(window).scrollTop();
            if (pos < winTop + 700) {
                $(this).addClass("revealLeft");
            }
        });
    });
});