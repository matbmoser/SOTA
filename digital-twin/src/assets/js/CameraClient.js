class CameraClient{
    constructor(cameraid) {
        this.serverip = null;
        this.serverport = null;
        this.serverkey = null;
        this.cameraid = cameraid;
        this.parsedMessage = null;
        this.status = null
        this.socket = null;
        this.type=null;
        // Until the server sends the data the id and session id will be empty
        this.token = null;
        this.SJMPHandler = new SJMPHandler(this)
    }
    async start(ip, port){
        setConnecting()
        this.serverip = ip;
        this.serverport = port;
        this.serverkey = ip + ":" + port.toString();
        let protocolPayload = ["SJMP",encodeURIComponent(this.SJMPHandler.getSYN())];
        this.socket = new WebSocket('ws://'+this.serverip+':'+this.serverport.toString(),protocolPayload);
        this.setSocket();
    }
    async close(){
        this.socket.close();
        unlockConfig();
        stopMessage();
        setOffline();
        this.status = "OFFLINE"
        if(this.type != "manual"){
            closeWindow();
        }
    }
    async setSocket(){
        this.socket.onopen = function(evt) {
            startMessage();
            setConnected();
            this.status = "CONNECTED";
        };

        this.socket.onclose = function(evt) {
            writeToScreen('<span style = "color: red;">CLIENT FORCED DISCONNECTED</span>');
            client.close();
        };
        
        this.socket.onmessage = function(evt) {
            writeToScreen('<span style = "color: gray; font-size:0.8em">RAW MESSAGE: ' + 
            evt.data+'</span>');
            client.parseMessage(evt.data)
        };
        
        this.socket.onerror = function(evt) {
            writeToScreen('<span style = "color: red;font-size:0.8em">ERROR: </span> '
            + evt.data);
            unlockConfig();
            stopMessage();
            setOffline();
            this.status = "OFFLINE"
            client.close()
        }; 
    }
    
    async sendMessageToClient(cameraid, message){
        this.sendMessageToServer(this.SJMPHandler.getMSG(cameraid, message))
    }

    async sendMessageToServer(message) {
        try{
            this.socket.send(message);
            writeToScreen("<span style='font-size:0.8em'>SENT: " + message+"</span>"); 
        }
        catch (e){
            writeToScreen('<span style = "color: red;font-size:0.8em">ERROR: </span> '
            + e.toString());
        }
    }
    async parseMessage(message){
        try{
            message = message.toString();
            message = message.replaceAll("\'", "\"");
            this.parsedMessage = JSON.parse(message);
            let color = "blue";
            if("flag" in this.parsedMessage){
                // Personalize message printed
                if(this.parsedMessage["flag"] == "ERR"){
                    color= "#fb4934";
                }else if(this.parsedMessage["flag"] == "ACK"){
                    color = "#fabd2f";
                }
                else if(this.parsedMessage["flag"] == "OK"){
                    color = "#198754";
                    this.token = this.parsedMessage["token"];
                    document.cookie = "token="+encodeURIComponent(this.token)+"; path=/";
                }
                writeToScreenSpan("<span style='color:"+color+"'><strong>FLAG ["+this.parsedMessage["flag"]+"]:</strong></span><span style='color:#0d6efd'> INFO: </span>");
                if("srv-time" in this.parsedMessage){
                    writeToScreenSpan("<span style='color:#0d6efd'>server-time = ["+this.parsedMessage["srv-time"]+"] </span>");
                }
                if("clt-time" in this.parsedMessage){
                    writeToScreenSpan("<span style='color:#0d6efd'>clt-time = ["+this.parsedMessage["clt-time"]+"] </span>");
                }
                writeToScreenSpan("<br>");
            }
            if(this.parsedMessage["flag"] == "OK"){
                writeToScreenSpan("<span style='color:"+color+"'><strong>["+this.serverkey+"] token = </strong>"+ this.parsedMessage["token"]+"</span>");
                writeToScreenSpan("<br><span style='color:#33ff00'>The connection is Opened! Client is Online, you can send messages!</span>");
                setOnline();
                this.status = "ONLINE"
            }
            if("cameraid" in this.parsedMessage){
                writeToScreenSpan("<span style='color:"+color+"'><strong>["+this.parsedMessage["cameraid"]+"] says -> </strong>"+ this.parsedMessage["message"]+"</span>");
            }else if(this.parsedMessage["message"] != "" && this.parsedMessage["message"] != null){
                writeToScreenSpan("<span style='color:"+color+"'><strong>["+this.serverkey+"] says -> </strong>"+ this.parsedMessage["message"]+"</span>");
            }
            
        }catch(e){
            console.log(e.message+" Error on Client.parseMessage("+message+"). ");
        }
    }
    async printMessages(messages={},color="blue"){
        for (const key in messages){
            writeToScreenSpan("<span style='color:"+color+"'><strong>"+key +":</strong> "+messages[key].toString()+"</span> ");
        }
    }
}