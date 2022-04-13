function closeServer(pid) {
    ServerConnectionManager.close(pid)
}
function callback(message) {
    writeToScreen(message)
}