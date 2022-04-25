<?php
$configs = include('assets/mod/configs/config.php');
$dbconfig = include("assets/mod/configs/db.config.php");
require_once("assets/mod/connection/connect.php");
require_once("assets/mod/auth/session.php");


if(empty( $_SESSION["token"] )){
    setcookie("__LOGIN__", "", time() - 3600, "/");
    header('Location: login/');
    exit;
  }


  require_once("assets/mod/auth/token.php");
  require_once("assets/mod/err/fallos.php");
  
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
<script>var configs = <?php echo json_encode($configs); ?>;</script>
<script>
var modals = <?php echo json_encode($modals); ?>;
var ip = "<?php echo $ip; ?>"
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
        <div class="mainContainer container-fluid">
          <div class="row d-flex align-content-center justify-content-center">
            <div class="col-xl-8 mapa">
              <div class="mapaContainer">
                <?php foreach ($zonas as $zona) {?>
                  <div id="Zona<?php echo $zona["letra"]?>" class="Zona">
                      <span class="dataZona" >0/<?php echo $zona["plazas"]?></span>
                  </div>
                <?}?>
              </div>
            </div>
          </div>
        </div>

        <button class="btn btn-warning" style="position: fixed; bottom: 20px; left: 20px;" type="button" id="openserver" data-bs-toggle="modal" data-bs-target="#Modal">Open Server</button> 
        <button class="btn btn-warning" style="position: fixed; bottom: 20px; right: 20px;" type="button" id="refresh">Refresh</button> 
    </div>

    <div class="container-fluid mt-4">
      <div class="row d-flex justify-content-center">
        <div class="col-md-3 d-flex justify-content-center">
          <button type="button" id="inButton" class="btnAccion btn btn-primary" ><i class="fa-solid fa-plus"></i> Coche</button>
        </div>
        <div class="col-md-3 d-flex justify-content-center">
          <button type="button" id="inButton" class="btnAccion btn btn-primary" ><i class="fa-solid fa-minus"></i> Coche</button>
        </div>
        <div class="col-md-3 d-flex justify-content-center">
          <button type="button" id="inButton" class="btnAccion btn btn-primary" ><i class="fa-solid fa-eye"></i> Ver Coches</button>
        </div>
      </div>
    </div>
    <div class="modal fade" id="Modal" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div id="modalContent" class="modal-content">
        </div>
      </div>
    </div>
  </body>
</div>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
<script src="assets/bt/js/bootstrap.js"></script>
<script src="assets/js/main.js"></script>
<script src="assets/js/cryptool/hashFunctions.js"></script>
<script src="assets/js/front/printFunctions.js"></script>
<script src="assets/js/front/clock.js"></script>
<script src="assets/js/map/map.js"></script>
<script src="assets/js/front/dark-mode.js"></script>
<script>

    function randomIntFromInterval(min, max) { // min and max included 
        return Math.floor(Math.random() * (max - min + 1) + min)
    }
    $(function(){
        currentTime();
        var refresh = document.getElementById("refresh");
        refresh.addEventListener('click', function() {
           ServerConnectionManager.getProcesses(); 
        });
    })
    $(function(){
        var modalContent = document.getElementById("modalContent");
        var openServerButton = document.getElementById("openserver");
        var inButton = document.getElementById("inButton");
      
        openServerButton.addEventListener('click', function() {
            //Limites
            var minPort = 1;
            var maxPort = 65535; //Habria que discutir un máximo
            var timeout;

            var ipPattern = "#ip-pattern";
            var portPattern = "#port-pattern";
            modalContent.innerHTML  = '<?php echo $modals["openServer"]; ?>';
            $(portPattern).val(randomIntFromInterval(minPort, maxPort));

            var defaultPortButton= document.getElementById("defaultPort");
            defaultPortButton.addEventListener('click', function() {
                $(ipPattern).val(configs["defaultIP"]);
                $(portPattern).val(configs["defaultPort"]);
            });

            var randomPortButton = document.getElementById("randomPort");
            randomPortButton.addEventListener('click', function() {
                $(portPattern).val(randomIntFromInterval(minPort, maxPort));
            });

            var openButton = document.getElementById("open");
            openButton.addEventListener('click', function() {
                //Open Server
                // Send POST with IP and PORT
                alert("Open");
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