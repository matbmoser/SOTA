class RTJPHandler{

  constructor(client){
      this.client = client
      this.flags = ["MSG", "FIN", "SYN", "ACK", "ERR", "OK"]
  }
  
  getMSG(clientid, message)
  {
      return "{'device-time': '"+new Date().getTime().toString()+"', 'token': '"+this.client.token+"', 'clientid': '"+clientid+"', 'flag': 'MSG', 'message': '"+message+"'}".toString();
  }
  getSYN()
  {
      return "{'device-time': '"+new Date().getTime().toString()+"', 'clientid': '"+this.client.clientid+"', 'flag': 'SYN'}".toString();
  }

}