<?php
  $configs = include('assets/mod/configs/config.php');
  $dbconfig = include("assets/mod/configs/db.config.php");

  require_once("assets/mod/connection/connect.php");
  require_once("assets/mod/auth/session.php");

  if(empty( $_SESSION["token"] ) || empty( $_COOKIE["UUID"])){  
    setcookie("__LOGIN__", "", time() - 3600, "/");
    header('Location: login/');
    exit;
  }

  require_once("assets/mod/err/fallos.php");
  require_once("assets/mod/auth/token.php");

  if (empty($username)){
      header('Location: login/?result='.$configs["securityErrorToken"]);
  } 
  $modals = include("assets/mod/front/modals.php");

  $ip = include("assets/mod/API/getIP.php"); 

  require_once("assets/mod/API/class.Table.php");

  $tablaZona = new Table($dbconfig, "Zona");
  $zonas = $tablaZona->getRows(array('return_type' => 'all'));

?>
<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<title>Digital Twin</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="assets/css/main.css"/>
<link rel="stylesheet" type="text/css" href="assets/css/header.css"/>
<link rel="stylesheet" type="text/css" href="assets/css/map.css"/>
<link rel="stylesheet" type="text/css" href="assets/bt/css/bootstrap.css"/>
<script src="assets/js/libs/jquery/jquery-3.5.1.slim.min.js"></script>
<link rel="icon" type="image/x-icon" href="media/favicon.ico">
<script src="https://kit.fontawesome.com/6d67b863f5.js" crossorigin="anonymous"></script>
</head>
<script>
  // Definición de constantes del servidor
  const CONFIGS = <?php echo json_encode($configs); ?>;
  const ZONAS = <?php echo json_encode($zonas); ?>;
  const MODALS = <?php echo json_encode($modals); ?>;
  const IP = "<?php echo $ip; ?>";
</script>
<div id="pagewrapper"> 
  <body>
    <header class="header sticky-top">
      <nav class="navbar navbar-expand-lg">
        <div class="container">

          <a class="navbar-brand me-2" href="">
            <img id="mylogo" src="../media/img/logoblue.png" height="90" loading="lazy" class="img-light" style="margin-top: -1px;"/>
          </a>

            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link logoName" href="#">Digital Twin</a>
              </li>
            </ul>

              <button
                id="openbtn"
                class="openbtn navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#buttonArea"
                aria-controls="buttonArea"
                aria-expanded="false"
                aria-label="Toggle navigation"
              >
              <i class="fas fa-bars"></i>
            </button>

          <div id="buttonArea" class="collapse navbar-collapse justify-content-end">

            <div class="d-flex align-items-center justify-content-end">
              <div class="px-3 me-2">
                <?php if ($username != "") { echo "<span>Welcome <strong>" . $_SESSION['username'] . "</strong>!</span>"; } ?>
              </div>
              <button type="button" class="btn me-3 btn-light btn-outline-dark" onclick="window.location.href= './assets/mod/user/logout.php?uuid=<?php echo $configs['logoutToken'] ?>'">
                <i class="fas fa-sign-out-alt"></i> 
                <span>Log out</span>
              </button>
              <button type="button" id="dark-mode" class="ml-3 btn btn-outline-light">
                <i class="fas fa-sun mr-1"></i>
                <span> Light Mode</span>
              </button>
            </div>
          </div>
        </div>
      </nav>
      <div class="clockContainer w-100 d-flex justify-content-between">

        <div id="clock" class="headerClock"></div>

        <div class="headerClock">Parking "<?php echo $configs['letraAparcamiento'];?>" - <?php echo $ip?> - <?php echo $configs['siglaUniversidad'];?></div>
      
      </div>
    </header>

    <div id="mainflow">
        <div class="mapaMainContainer container-fluid">
          <div class="row d-flex align-content-center justify-content-center">
            <div class="col-xl-8 mapa">
              <div class="mapaContainer">
                <?php foreach ($zonas as $zona) {?>
                  <div id="Zona<?php echo $zona["letra"]?>" class="Zona">
                      <span class="dataZona" id="dataZona<?php echo $zona["id"]?>">-/<?php echo $zona["plazas"]?></span>
                  </div>
                <?}?>
              </div>
            </div>
          </div>
        </div>

        <button class="btn btn-warning" style="position: fixed; bottom: 20px; left: 20px;" type="button" id="openserver" data-bs-toggle="modal" data-bs-target="#Modal">Open Server</button> 
        <button class="btn btn-warning" style="position: fixed; bottom: 20px; right: 20px;" type="button" id="refresh">Refresh</button> 
    </div>
    <!-- Botones -->
    <div class="container-fluid mt-4 mb-4">
      <div class="row d-flex justify-content-center">
        <div class="col-md-2 mt-2  mb-2 d-flex justify-content-center">
          <button type="button" data-bs-toggle="modal" data-bs-target="#EntradaVehiculo"class="btnAccion btn btn-primary" ><i class="fa-solid fa-plus"></i> Añadir Vehiculo</button>
        </div>
        <div class="col-md-2 mt-2  mb-2 d-flex justify-content-center">
          <button type="button" id="deleteVehicle" data-bs-toggle="modal" data-bs-target="#SalidaVehiculo"class="btnAccion btn btn-primary" ><i class="fa-solid fa-minus"></i> Borrar Vehiculo</button>
        </div>
        <div class="col-md-2 mt-2 mb-2 d-flex justify-content-center">
          <button type="button" id="seeVehicles" data-bs-toggle="modal" data-bs-target="#VerPlazas"class="btnAccion btn btn-primary" ><i class="fa-solid fa-eye"></i> Ver Plazas</button>
        </div>
        <div class="col-md-2 mt-2 mb-2 d-flex justify-content-center">
          <button type="button" id="barreras" data-bs-toggle="modal" data-bs-target="#Modal" class="btnAccion btn btn-primary w-100" ><i class="fa-solid fa-triangle-exclamation"></i> Barreras</button>
        </div>
      </div>
    </div>
  
    <!-- Modal genérico -->
    <div class="modal fade" id="Modal" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div id="modalContent" class="modal-content">
        </div>
      </div>
    </div>
    
    <!-- Entrada Vehiculo Añadir Matricula-->
    <div class="modal fade" id="EntradaVehiculo" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div id="modalContent" class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Camera Entrada E1</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>
        <div class="modal-body">
          <input type="text" class="form-control" name="matriculaEntrada" maxlength = "12" placeholder="Matricula" required/>
          <textfield class="w-100 h-100" id="monitorEntrada" disable></textfield>
        </div>
        <div class="modal-footer">
          <button class="btn btn-success" id="addVehiculo" type="submit">Enviar Matricula</button>
        </div>
        </div>
      </div>
    </div>

    <!-- Salida Vehiculo Borrar Matricula-->
    <div class="modal fade" id="SalidaVehiculo" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
      <div id="modalContent" class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Camera Salida S1</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>
        <div class="modal-body">
          <input type="text" class="form-control" name="matriculaEntrada" maxlength = "12" placeholder="Matricula" required/>
          <textfield class="w-100 h-100" id="monitorSalida" disable></textfield>
        </div>
        <div class="modal-footer">
          <button class="btn btn-success" id="deleteVehiculo" type="submit">Enviar Matricula</button>
        </div>
        </div>
      </div>
    </div>

     <!-- Ver Vehiculos-->
    <div class="modal fade" id="VerPlazas" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-fullscreen modal-dialog-scrollable">
      <div id="modalContent" class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Ver Plazas</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button></div>
        <div class="modal-body">
          <div class="container-fluid mt-4 d-flex justify-content-center table-responsive" style="background: var(--color); color: var(--bg-color);">
              <div class="row mt-5">    
              <div class="col-12">
              <h2 class="text-center">
                Plazas Ocupadas<strong style="color:green"></strong>
              </h2>
              </div>
              <table class="table m-2 table-striped table-hovertext-nowrap">
                  <thead>
                    <tr>
                      <th>idPlaza</th>
                      <th>Matrícula</th>
                      <th>Segmento</th>
                      <th>Tamaño</th>
                      <th>Fecha Entrada</th>
                    </tr>
                  </thead>
                  <tbody id="verPlazasTable">
                  
                  </tbody>
                </table>
            </div>
          </div>
        </div>
        <div class="modal-footer d-flex justify-content-between">
          <button class="btn btn-warning" id="refreshModal">Refresh</button>
          <button class="btn btn-danger" data-bs-dismiss="modal" type="button">Cerrar</button>
        </div>
        </div>
      </div>
    </div>
  </body>
</div>
<div id="output"></div>
<script src="assets/js/connection/HTTPRequest.js"></script>
<script src="assets/js/server/ServerConnectionManager.js"></script>
<script src="assets/js/server/serverFunctions.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="assets/bt/js/bootstrap.js"></script>
<script src="assets/js/main.js"></script>
<script src="assets/js/cryptool/hashFunctions.js"></script>
<script src="assets/js/front/printFunctions.js"></script>
<script src="assets/js/front/clock.js"></script>
<script src="assets/js/map/map.js"></script>
<script src="assets/js/front/dark-mode.js"></script>
<script src="assets/js/barreras/barrera.js"></script>
<script src="assets/js/front/cookieFunctions.js"></script>
<script>
      //HTTP Request function Callbacks
      function callback(message, tag) {
        switch (tag) {
            case "serverOpen":
                handleServer(message);
                break;
            case "serverClose":
                writeToMonitor(message);
                break;
            case "serverRefresh":
                break;
            case "refreshZonas":
                pintarZonas(message);
                break;
        }
    }
    //RefeshServerStatus
    async function refreshServerStatus(){
        //checkServerStatus();
        let status = localStorage.getItem("serverStatus");
        let content = "";
        switch (status){
          case "CREATING":
            content = '<span class="alert-fail">CREATING</span>';
            break;
          
          case "RUNNING":
            content = '<span class="alert-connected">RUNNING</span>';
            break;
          
          case "STOPPED":
            content = '<span class="alert-danger">STOPPED</span>';
            break;

        }
        document.getElementById("status").innerHTML = content;

      }

    refreshZonas();
    refreshServerStatus();

    function pintarZonas(response){
        var parsedResponse = JSON.parse(response);
        var ocupacionZonas = parsedResponse["plazasZonas"];
        var plazasOcupadas = parsedResponse["vehiculosPlazas"];
        var lenzonas = ZONAS.length;
        var zonasPattern = "#dataZona";
        let i = 0;
        let table = $("#verPlazasTable");
        let tableContent = "";
        while(i < lenzonas){
          //Constante zonas mapa
          let zona = ZONAS[i];
          let idZona = zona["id"];
          let aforo = zona["plazas"];
          // Datos recogidos
          let plazasZona = plazasOcupadas[idZona];
          let lenplazaszona = plazasZona.length;
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
          datoZona = $(zonasPattern+idZona.toString()).html(ocupacionZonas[idZona].toString() +"/"+ aforo.toString()) 
          i++;
        }
        table.html(tableContent);
        document.querySelectorAll("#refresh, #refreshModal").forEach((ele) => {
            ele.innerHTML = `Refresh`;
        });
    }

    function refreshZonas(){
      var uuid = getCookie("UUID");
      var data = "uuid="+uuid;
      HTTPRequest.POST('http://'+CONFIGS["httpHost"]+'/assets/mod/API/getPlazasZonas.php', data,  'refreshZonas');
    }

    const refreshInterval = setInterval(function() {
      let ele = document.getElementById("refresh");
      ele.innerHTML = `<div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Refreshing`;
      refreshZonas();
    }, 20 * 1000); // 60 * 1000 milsec

    function randomIntFromInterval(min, max) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min)
    }

    $(function(){
        currentTime();
        document.querySelectorAll("#refresh, #refreshModal").forEach((ele) => {
          ele.addEventListener("click", function (e) {
            ele.innerHTML = `<div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Refreshing`;
            refreshZonas();
          });
        });
    })

    function handleServer(response){
      try{
        overwriteMonitor(response);
        var data = JSON.parse(response)["serverData"];
        localStorage.setItem("serverInfo",JSON.stringify(data));
        console.log(data);
        localStorage.setItem("serverStatus", "RUNNING");
        printlnMonitor(data);
        printlnMonitor("Servidor Abierto!");
      }catch(e){
        overwriteMonitor("Was not posible to start server: ["+ e.toString()+"]")
        localStorage.setItem("serverStatus", "FAIL");
        localStorage.removeItem("serverInfo")
      }
    }
    function overwriteMonitor(data){
      let monitor = document.getElementById("monitor");
      monitor.innerHTML = data;
    }

    function printlnMonitor(data){
        var pre = document.createElement("p"); 
        pre.style.wordWrap = "break-word"; 
        pre.innerHTML = data; 
        document.getElementById("monitor").appendChild(pre);
    }

      async function printMonitor(data) {
        var pre = document.createElement("span"); 
        pre.style.wordWrap = "break-word"; 
        pre.innerHTML = data; 
        document.getElementById("monitor").appendChild(pre);
      }

    function uuidv4() {
      return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
      );
    }
    function blockAddServer(){
      var openServerButton = document.getElementById("openserver");
      var defaultPortButton= document.getElementById("defaultPort");
      var randomPortButton = document.getElementById("randomPort");
      var openButton = document.getElementById("open");

      openServerButton.innerHTML = "Close Server";
      openButton.innerHTML = "Cerrar Servidor";
      openButton.classList.remove("btn-success");
      openButton.classList.add("btn-danger");
      randomPortButton.classList.add("hidden");
      defaultPortButton.classList.add("hidden");
      $("#port-pattern").attr('disabled','disabled');
      refreshStatus();
    }
    $(function(){
        var modalContent = document.getElementById("modalContent");
        var openServerButton = document.getElementById("openserver");
        var addVehicle = document.getElementById("addVehicle");

        barreras.addEventListener('click', function() {
          modalContent.innerHTML  = `<?php echo $modals["barreras"]; ?>`;
          adminBarreras();
        });
        openServerButton.addEventListener('click', function() {
            //Limites de Puertos
          
            modalContent.innerHTML  =  `<?php echo $modals["openServer"]; ?> `;

            var server = localStorage.getItem("serverInfo");
            if(server!=null){
              $("#port-pattern").val(JSON.parse(server)["port"]);
              blockAddServer();
              var openButton = document.getElementById("open");

              openButton.addEventListener('click', function() {
                let pid = JSON.parse(localStorage.getItem("serverInfo"))["pid"];
                closeServer(pid);
              });

            }else{
              var ipPattern = "#ip-pattern";
              var portPattern = "#port-pattern";
              var minPort = 1;
              var maxPort = 65535; 
              var timeout;
              var ipPattern = "#ip-pattern";
              var portPattern = "#port-pattern";
              modalContent.innerHTML  =  `<?php echo $modals["openServer"]; ?> `;

              $(portPattern).removeAttr('disabled');
              $(portPattern).val(randomIntFromInterval(minPort, maxPort));

              var defaultPortButton= document.getElementById("defaultPort");
              defaultPortButton.classList.remove("hidden");
              defaultPortButton.addEventListener('click', function() {
                  $(ipPattern).val(CONFIGS["defaultIP"]);
                  $(portPattern).val(CONFIGS["defaultPort"]);
              });

              var randomPortButton = document.getElementById("randomPort");
              randomPortButton.classList.remove("hidden");
              randomPortButton.addEventListener('click', function() {
                  $(portPattern).val(randomIntFromInterval(minPort, maxPort));
              });

              var openButton = document.getElementById("open");
              openButton.addEventListener('click', function() {
                  let ip = $(ipPattern).val();
                  let port = $(portPattern).val();
                  let monitor = document.getElementById("monitor");
                  localStorage.setItem("serverStatus", "CONNECTING");
                  monitor.innerHTML = `<span style="color:green"><div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Abriendo Servidor en IP=[`+ip.toString()+`] y PORT=[`+port.toString()+`]</span>`
                  openServer(port);
                  blockAddServer();
                  refreshStatus();
                  var server = localStorage.getItem("serverInfo");
                  if(server!=null){
                    $("#port-pattern").val(JSON.parse(server)["port"]);
                    blockAddServer();
                    var openButton = document.getElementById("open");

                    openButton.addEventListener('click', function() {
                      let pid = JSON.parse(localStorage.getItem("serverInfo"))["pid"];
                      closeServer(pid);
                    });
                  }
                });
              $(portPattern).change(function () { //Cuando detecta un cambio mira si ha superado el maximo o el minimo y lo cambia
                try {
                    var valor = parseInt($(portPattern).val());
                    if (valor < minPort) {
                        $(portPattern).val(minPort);
                    } else if (valor > maxPort) {
                        $(portPattern).val(maxPort);
                    }
                } catch (Exception) {
                    $(portPattern).val(minPort);
                }
            });
          }
        });
    });
    // Disable form submissions if there are invalid fields
    (function() {
        'use strict';
        window.addEventListener('load', function() {
            // Get the forms we want to add validation styles to
            var forms = document.getElementsByClassName('needs-validation');
            // Loop over them and prevent submission
            var validation = Array.prototype.filter.call(forms, function(form) {
                form.addEventListener('submit', function(event) {
                    if (form.checkValidity() === false) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        }, false);
    })();
</script>
