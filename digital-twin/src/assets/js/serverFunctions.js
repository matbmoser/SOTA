function closeServer(pid) {
    ServerConnectionManager.close(pid)
}
function callback(message, tag) {
    switch (tag) {
        case "serverClose":
            writeToScreen(message);
            break;
        case "serverRefresh":
            overwriteScreen("[REFRESH]"+message);
            break;
    }
}