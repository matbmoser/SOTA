

// Usage

function currentTime() {
    var date = new Date();
    var hh = date.getHours();
    var session = "AM";
  
    if(hh >= 12){
        session = "PM";
     }
    
    var dateTimeString = date.toLocaleString("es-ES", { timeZone: "Europe/Madrid" });
    var time = dateTimeString + " " + session;
    document.getElementById("clock").innerText = time; 
    let t = setTimeout(function(){ currentTime() }, 1000);
  }