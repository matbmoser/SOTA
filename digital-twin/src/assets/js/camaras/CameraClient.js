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
        this.sessionid = null;
        this.SJMPHandler = new SJMPHandler(this)
        this.self = null
        this.sendedMessage = null;
    }
    async start(ip, port, self){
        setConnecting();
        this.serverip = ip;
        this.serverport = port;
        this.serverkey = ip + ":" + port.toString();
        let protocolPayload = ["SJMP",encodeURIComponent(this.SJMPHandler.getSYN())];
        this.socket = new WebSocket('ws://'+this.serverip+':'+this.serverport.toString(),protocolPayload);
        this.setSocket();
        this.self = self;
    }
    async close(){
        this.socket.close();
        stopMessage();
        setOffline();
        this.status = "OFFLINE"
        localStorage.setItem("cameraStatus", this.status)
    }
    async setSocket(){
        var self = this;
        this.socket.onopen = function(evt) {
            startMessage();
            setConnected();
            self.status = "CONNECTED";
            localStorage.setItem("cameraStatus", this.status)
        };

        this.socket.onclose = function(evt) {
            writeToScreen('<span style = "color: red;">CLIENT FORCED DISCONNECTED</span>');
            self.close();
        };
        
        this.socket.onmessage = function(evt) {
            writeToScreen('<span style = "color: gray; font-size:0.8em">RAW MESSAGE: ' + 
            evt.data+'</span>');
            self.parseMessage(evt.data);
        };
        
        this.socket.onerror = function(evt) {
            writeToScreen('<span style = "color: red;font-size:0.8em">ERROR: </span> '
            + evt.data);
            unlockConfig();
            stopMessage();
            setOffline();
            self.status = "OFFLINE"
            localStorage.setItem("cameraStatus", this.status )
            self.close();
        }; 
    }
    async sendPlateToServer(matricula, tipo) {
        if (tipo === "IN"){
            this.sendedMessage = "IN";
            this.sendMessageToServer(this.SJMPHandler.getIN(matricula))
        }else if(tipo === "OUT"){
            this.sendedMessage = "OUT";
            this.sendMessageToServer(this.SJMPHandler.getOUT(matricula))
        }
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
                    if (this.sendedMessage == "IN"){
                        printLn("monitorEntrada", "<span style='color:" + color +"'><strong>[ERROR]</strong> " + this.parsedMessage["response"]+"</span>");
                    } else if (this.sendedMessage == "OUT") {
                        printLn("monitorSalida", "<span style='color:" + color +"'><strong>[ERROR]</strong> " + this.parsedMessage["response"] + "</span>");
                    }
                }else if(this.parsedMessage["flag"] == "ACK"){
                    color = "#158a00";
                    if (this.sendedMessage == "IN") {
                        printLn("monitorEntrada", "<span style='color:" + color +"'><strong>[ADDED]</strong> " + this.parsedMessage["response"] + "</span>");
                    } else if (this.sendedMessage == "OUT") {
                        printLn("monitorSalida", "<span style='color:" + color +"'><strong>[DELETED]</strong> " + this.parsedMessage["response"] + "</span>");
                    }
                }
                else if(this.parsedMessage["flag"] == "OK"){
                    color = "#198754";
                    this.sessionid = this.parsedMessage["sessionid"];
                    document.cookie = "sessionid="+encodeURIComponent(this.sessionid)+"; path=/";
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
            if (this.parsedMessage["flag"] == "OK"){
                writeToScreenSpan("<span style='color:" + color + "'><strong>[" + this.serverkey + "] sessionid = </strong>" + this.parsedMessage["sessionid"]+"</span>");
                writeToScreenSpan("<br><span style='color:#00b92c'>La conexión está abierta, ¡puedes enviar matriculas!</span>");
                setOnline();
                this.status = "ONLINE";
                localStorage.setItem("cameraid", this.cameraid);
                localStorage.setItem("cameraStatus", this.status);
            }
            if("cameraid" in this.parsedMessage){
                writeToScreenSpan("<span style='color:" + color + "'><strong>[" + this.parsedMessage["cameraid"] + "] says -> </strong>" + this.parsedMessage["response"]+"</span>");
            } else if (this.parsedMessage["response"] != "" && this.parsedMessage["response"] != null){
                writeToScreenSpan("<span style='color:" + color + "'><strong>[" + this.serverkey + "] says -> </strong>" + this.parsedMessage["response"]+"</span>");
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