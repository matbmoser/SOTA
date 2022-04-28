class ServerConnectionManager{
    static close(pid) {
        HTTPRequest.POST('http://'+configs["httpHost"]+'/serverController/close.php', 'pid=' + pid+';uuid='+configs["securityUUIDToken"],  'serverClose');
    }
    static closeDefault() {
        HTTPRequest.POST('http://'+configs["httpHost"]+'/serverController/close.php', "", 'serverClose');
    }
    static getProcesses() {
        HTTPRequest.POST('http://'+configs["httpHost"]+'/serverController/psef.php', "", 'serverRefresh');
    }
}
