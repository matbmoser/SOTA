class ServerConnectionManager{
    static open(port) {
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/open.php', 'port=' + port.toString()+'&uuid='+CONFIGS["securityUUIDToken"],  'serverOpen');
    }
    static close(pid) {
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/close.php', 'pid=' + pid+'&uuid='+CONFIGS["securityUUIDToken"],  'serverClose');
    }
    static closeDefault() {
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/close.php', "", 'serverClose');
    }
    static getProcesses() {
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/psef.php', "", 'serverRefresh');
    }
}
