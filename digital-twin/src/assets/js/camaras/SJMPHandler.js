class SJMPHandler{

  constructor(client){
      this.client = client
      this.flags = ["SYN", "OK", "IN", "OUT", "FIN", "ACK", "FETCH"]
  }
  
  getMSG(cameraid, message)
  {
      return "{'clt-time': '"+new Date().getTime().toString()+"', 'token': '"+this.client.token+"', 'cameraid': '"+cameraid+"', 'flag': 'MSG', 'message': '"+message+"'}".toString();
  }
  getSYN()
  {
      return "{'clt-time': '"+new Date().getTime().toString()+"', 'cameraid': '"+this.client.cameraid+"', 'flag': 'SYN'}".toString();
  }

}