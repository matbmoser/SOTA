

class ParkingMap{
  constructor(){
    this.refreshIntervalMap=null;
  }
  pintarZonas(response){
    var parsedResponse = JSON.parse(response);
    var ocupacionZonas = parsedResponse["plazasZonas"];
    var plazasOcupadas = parsedResponse["vehiculosPlazas"];
    var lenzonas = ZONAS.length;
    var zonasPattern = "#dataZona";
    let i = 0;
    let table = $("#verPlazasTable");
    let tableContent = "";
    let aforoTotal = 0;
    let aforoOcupadas = 0;
    while(i < lenzonas){
      //Constante zonas mapa
      let zona = ZONAS[i];
      let idZona = zona["id"];
      let aforo = zona["plazas"];
      aforoTotal += parseInt(aforo);
      // Datos recogidos
      let plazasZona = plazasOcupadas[idZona];
      let lenplazaszona = plazasZona.length;
      aforoOcupadas += lenplazaszona;
      let j = 0;
      while(j < lenplazaszona){
        let plaza = plazasZona[j];
        let idPlaza = plaza["idPlaza"].toString();
        let matricula = plaza["matricula"].toString();
        let segmento = plaza["segmento"].toString();
        let clasificacion = plaza["clasificacion"].toString();
        let created_at = plaza["created_at"].toString();
        let row = `<tr>
          <td>`+idPlaza+`</td>
          <td>`+matricula+`</td>
          <td>`+segmento+`</td>
          <td>`+clasificacion+`</td>
          <td>`+created_at+`</td>
        </tr>`;
        tableContent += row;
        j++;
      }
      document.querySelector(zonasPattern+idZona.toString()).innerHTML = ocupacionZonas[idZona].toString() +"/"+ aforo.toString()
      i++;
    }
    let aforoLibres = aforoTotal - aforoOcupadas
    $("#aforoLibres").html("Plazas Libres: "+aforoLibres+"/"+aforoTotal)
    $("#aforoOcupadas").html("Plazas Ocupadas: " + aforoOcupadas + "/" + aforoTotal)
    table.html(tableContent);
    document.querySelectorAll("#refresh, #refreshModal").forEach((ele) => {
        ele.innerHTML = `Refresh`;
    });
}

 refreshZonas(){
  var uuid = getCookie("UUID");
  var data = "uuid="+uuid;
  HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/assets/mod/API/getPlazasZonas.php', data,  'refreshZonas');
  }

 startAutoRefresh(){
  var self = this;
  this.refreshIntervalMap = setInterval(function() {
    let ele = document.getElementById("refresh");
    ele.innerHTML = `<div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Refreshing`;
    self.refreshZonas();
  },8000); // 60 * 1000 milsec
 }
 stopAutoRefresh(){
  clearInterval(this.refreshIntervalMap);
 }
}

