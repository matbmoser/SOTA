class ServerConnectionManager{
    static open(port) {
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/open.php', 'port=' + port.toString()+'&uuid='+CONFIGS["securityUUIDToken"],  'serverOpen');
    }
    static close(port) {
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/close.php', 'port=' + port+'&uuid='+CONFIGS["securityUUIDToken"],  'serverClose');
    }
    static get(port){
        HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/serverController/get.php', 'port=' + port.toString()+'&uuid='+CONFIGS["securityUUIDToken"],  'getServer');
      }
    static getLog(serverid){
        HTTPRequest.GET('http://'+CONFIGS["httpHost"]+'/serverController/log/'+serverid.toString()+'/serverStatus.log',"", "serverLog");
    }
}
