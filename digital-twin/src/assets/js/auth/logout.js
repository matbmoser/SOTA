function logout() {
    let cameraid = localStorage.getItem("cameraid");
    if (cameraid != null && cameraid != undefined && cameraid != "") {
        disconnectFromServer();
    }
    let rawServer = localStorage.getItem("serverInfo");
    if (rawServer != null && rawServer != undefined && rawServer != "") {
        closeServerByPort();
    }
    localStorage.removeItem("serverInfo");
    localStorage.removeItem("cameraid");
    localStorage.removeItem("serverStatus");
    localStorage.removeItem("cameraStatus");

    window.location.href = `./assets/mod/user/logout.php?uuid=`+ CONFIGS["logoutToken"];

}