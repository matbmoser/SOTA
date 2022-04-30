function closeServer(pid) {
    ServerConnectionManager.close(pid);
}
function openServer(port) {
    ServerConnectionManager.open(port);
}