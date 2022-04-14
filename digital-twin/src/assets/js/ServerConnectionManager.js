class ServerConnectionManager{
    static close(pid) {
        HTTPRequest.POST('http://localhost:3333/server/close.php', 'pid='+pid)
    }
    static closeDefault() {
        HTTPRequest.POST('http://localhost:3333/server/close.php')
    }
}
