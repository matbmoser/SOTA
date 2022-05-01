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
<script src="assets/js/map/map.js"></script>
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
    <!-- Botones -->
    <div class="container-fluid mt-2 mb-2">
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
      <div class="row d-flex justify-content-between">
        <div class="col-md-6 d-flex justify-content-lg-start justify-content-md-start mt-3 justify-content-center justify-content-xl-start">
          <button class="btn btn-warning" type="button" id="openserver" data-bs-toggle="modal" data-bs-target="#OpenServer">Open Server</button> 
        </div>
        <div class="col-md-6 d-flex align-items-center justify-content-center justify-content-lg-end mt-3 justify-content-md-end justify-content-xl-end">
          <!-- Checked switch -->
            <div class="form-check form-switch" style="margin-right: 10px; ">
              <input class="form-check-input" type="checkbox" role="switch" id="autorefresh" />
              <label class="form-check-label" for="flexSwitchCheckChecked">Auto-refresh</label>
            </div>
            <button class="btn btn-warning ml-2" type="button" id="refresh">Refresh</button>
        </div>
      </div>
    </div>
    <?php
      // Importamos modales
      include("assets/mod/front/modals/genericModal.php");
      include("assets/mod/front/modals/openServerModal.php");
      include("assets/mod/front/modals/simuladorCamaraModal.php");
      include("assets/mod/front/modals/verVehiculosModal.php");
    ?>

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
<script src="assets/js/front/dark-mode.js"></script>
<script src="assets/js/barreras/barrera.js"></script>
<script src="assets/js/front/cookieFunctions.js"></script>
<script>
    const parkingMap = new ParkingMap();
    parkingMap.refreshZonas();
      
    window.onload = function (){
      refreshServerStatus();
    }
      //HTTP Request function Callbacks
    function callback(response, tag) {
        switch (tag) {
            case "serverOpen":
                handleOpen(response);
                break;
            case "serverClose":
                handleClose(response);
                break;
            case "getServer":
                checkIfServerIsAlive(response);
                break;
            case "serverRefresh":
                break;
            case "refreshZonas":
                parkingMap.pintarZonas(response);
                break;
        }
    }

    function setAutoRefresh(){
      let content = ""
      let setAutoRefresh = localStorage.getItem("autorefresh");
      let elem = document.querySelector("#autorefresh");
      if(setAutoRefresh == "true"){
        parkingMap.startAutoRefresh();
        elem.checked = true;
      }else{
        content = `<input class="form-check-input" type="checkbox" role="switch" id="autorefresh"/>`
        parkingMap.stopAutoRefresh();
        elem.checked = false;
      }
    }

    $(function(){
        setAutoRefresh()
        $('#autorefresh').change(function() {
          if(this.checked) {
            localStorage.setItem("autorefresh", "true")
              parkingMap.startAutoRefresh();
          }else{
            localStorage.setItem("autorefresh", "false")
            parkingMap.stopAutoRefresh();
          }
        });
        currentTime();
        getServerStatus();
        document.querySelectorAll("#refresh, #refreshModal").forEach((ele) => {
          ele.addEventListener("click", function (e) {
            ele.innerHTML = `<div class="spinner-border spinner-border-sm" role="status"><span class="sr-only">Loading...</span></div> Refreshing`;
            parkingMap.refreshZonas();
          });
        });
    })

  
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

    function randomIntFromInterval(min, max) { // min and max included 
      return Math.floor(Math.random() * (max - min + 1) + min)
    }
    $(function(){
        var modalContent = document.getElementById("modalContent");
        var addVehicle = document.getElementById("addVehicle");

        barreras.addEventListener('click', function() {
          modalContent.innerHTML  = `<?php echo $modals["barreras"]; ?>`;
          adminBarreras();
        });
        
        var ipPattern = "#ip-pattern";
        var portPattern = "#port-pattern";
        var minPort = 1;
        var maxPort = 65535;

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