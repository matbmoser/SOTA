var client = null;
var type = null;
DEFAULTSERVERIP = "127.0.0.1";
DEFAULTSERVERPORT = "8080";
window.onload = function () {
  const params = new URLSearchParams(window.location.search);
  if (params.has("cameraid") == false || params.get("cameraid") == "") {
    document.getElementById("pagewrapper").style = "display: block!important";
    type = "manual";
  } else {
    type = "auto";
    let cameraid = params.get("cameraid");
    document.getElementById("pagewrapper").style = "display: none!important";
    if (params.has("ip") == false) {
      createAndConnectClient(cameraid, DEFAULTSERVERIP, DEFAULTSERVERPORT);
    } else {
      let ip = params.get("ip");
      if (params.has("port") == false) {
        createAndConnectClient(cameraid, ip, DEFAULTSERVERPORT);
      } else {
        let port = params.get("port");
        hasClients = params.has("CAMERAS");
        hasText = params.has("text");
        if (!hasText) {
          createAndConnectClient(cameraid, ip, port);
          return;
        }

        let count = null;
        let wait = null;
        if (params.has("count")) {
          count = params.get("count");
        }
        if (params.has("wait")) {
          wait = params.get("wait");
        }

        let text = decodeURI(params.get("text"));

        if (hasClients) {
          let CAMERAS = decodeURI(params.get("CAMERAS"));
          console.log(CAMERAS);
          createAndConnectClientToClients(
            text,
            CAMERAS,
            cameraid,
            ip,
            port,
            count,
            wait
          );
        } else {
          createAndConnectClientWithText(text, cameraid, ip, port, count, wait);
        }
      }
    }
  }
};
