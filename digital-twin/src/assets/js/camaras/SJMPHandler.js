class SJMPHandler{

  constructor(camera){
      this.camera = camera
      this.flags = ["SYN", "OK", "IN", "OUT", "FIN", "ACK"]
  }
  
  getIN(matricula)
  {
      return "{'clt-time': '"+new Date().getTime().toString()+"', 'sessionid': '"+this.camera.sessionid+"', 'flag': 'IN', 'matricula': '"+matricula+"'}".toString();
  }
  getOUT(matricula)
  {
      return "{'clt-time': '"+new Date().getTime().toString()+"', 'sessionid': '"+this.camera.sessiond+"', 'flag': 'OUT', 'matricula': '"+matricula+"'}".toString();
  }
  getSYN()
  {
      return "{'clt-time': '"+new Date().getTime().toString()+"', 'cameraid': '"+this.camera.cameraid+"', 'flag': 'SYN', 'type': '"+this.camera.type+"'}".toString();
  }

}