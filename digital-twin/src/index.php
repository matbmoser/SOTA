<?php
$configs = include('assets/mod/config.php');
$dbconfig = include("assets/mod/db.config.php");
require_once("assets/mod/connect.php");
require_once("assets/mod/session.php");


if(empty( $_SESSION["token"] )){
    setcookie("__LOGIN__", "", time() - 3600, "/");
    header('Location: login/');
    exit;
  }

require_once("assets/mod/token.php");
require_once("assets/mod/fallos.php");

if (empty($username)){
    header('Location: login/?result='.$configs["securityErrorToken"]);
} 
$modals = include("assets/mod/modals.php");
$ip = include("assets/mod/getIP.php"); 
?>
<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<title>Digital Twin</title>
<link rel="stylesheet" type="text/css" href="assets/css/main.css"/>
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
<script src="assets/js/CameraClient.js"></script>
<script src="assets/js/SJMPHandler.js"></script>
<script src="assets/js/config.js"></script>
<script src="assets/js/hashFunctions.js"></script>
<script src="assets/js/printFunctions.js"></script>
<script src="assets/js/workflowFunctions.js"></script>
<script src="assets/js/createClientFunctions.js"></script>
<script src="assets/js/clock.js"></script>
<script src="assets/js/dark-mode.js"></script>
<div id="pagewrapper" style="display: none!important;"> 
    <body>
      
<header class="header sticky-top">
    <nav class="navbar shadow">
      <a class="navbar-brand" href="#">
      	<img id="mylogo" class="img-light"src="../media/img/logoblue.png" style="height:4em">
        <span class="logoName">Digital Twin</span>
      </a>
        <div class="w-100 d-flex justify-content-end">
            <ul class="nav justify-content-end align-items-center">
                <li class="nav-item">
                    <?php
                    if ($username != "") {
                        echo "<span>Welcome <strong>" . $_SESSION['username'] . "</strong>!</span>";
                    }
                    ?>
                </li>
                <li class="nav-item">
                <button type="button" class="ml-3 logout btn btn-light btn-outline-dark" onclick="window.location.href= './assets/mod/logout.php?uuid=<?php echo $configs['logoutToken'] ?>'"><i class="fas fa-sign-out-alt"></i> <span>Log out</span></button>
                </li>
                <li class="nav-item">
                    <button type="button" id="dark-mode" class="ml-3 btn btn-outline-light"><i class="fas fa-sun mr-1"></i><span> Light Mode</span></button>
                </li>
            </ul>
        </div>
   </nav>
</header>
<!--
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand me-2" href="https://mdbgo.com/">
      <img
        src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp"
        height="16"
        alt="MDB Logo"
        loading="lazy"
        style="margin-top: -1px;"
      />
    </a>

    <button
      class="navbar-toggler"
      type="button"
      data-mdb-toggle="collapse"
      data-mdb-target="#navbarButtonsExample"
      aria-controls="navbarButtonsExample"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <i class="fas fa-bars"></i>
    </button>

    <div class="collapse navbar-collapse" id="navbarButtonsExample">
     
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="#">Dashboard</a>
        </li>
      </ul>


      <div class="d-flex align-items-center">
        <button type="button" class="btn btn-link px-3 me-2">
          Login
        </button>
        <button type="button" class="btn btn-primary me-3">
          Sign up for free
        </button>
        <a
          class="btn btn-dark px-3"
          href="https://github.com/mdbootstrap/mdb-ui-kit"
          role="button"
          ><i class="fab fa-github"></i
        ></a>
      </div>
    </div>
  </div>
</nav>
-->
    <div class="w-100 d-flex justify-content-center"><div id="clock" class="headerClock"></div></div>
        <div><br><br>
            
            <div id="config">
                <label for="ip">Please insert IP of server!</label>
                <input type="text" id="ip" name="ip"><br><br>
                <label for="port">Please insert PORT of server!</label>
                <input type="number" id="port" name="port"><br><br>
                <button type="submit" id="submitconf">Connect</button> 
            </div>
        </div>
    </body>
</div>
<div id="mainflow">
    <button class="btn btn-warning" style="position: fixed; bottom: 20px; left: 20px;" type="button" id="openserver">Open Server</button> 
    <button class="btn btn-warning" style="position: fixed; bottom: 20px; right: 20px;" type="button" id="refresh">Refresh</button> 
    <br><br>
    <div id = "status"><span class="alert-danger">DISCONNECTED</span></div>
    <br>
    <div id="response" class="hidden">
        <button type="button" id="disconnect">Disconnect</button> 
        <br><br>
        <label for="client">* Client to Send:</label>
        <input type="text" id="client" name="client"><br><br>
        <label for="message">* Message to Send:</label>
        <input type="text" id="message" name="message"><br><br>
        <button type="submit" id="sendmessage">Send Message</button> 
    </div>
    <br>
    <div><p style="font-size:0.8em">The fields marked with * are obligatory!</p></div>
</div>
<br><br>
<div id="output"></div>
<script src="assets/bt/js/bootstrap.js"></script>
<script src="assets/js/libs/crypto-js/aes.js"></script>
<script src="assets/js/main.js"></script>
<script src="assets/js/HTTPRequest.js"></script>
<script src="assets/js/ServerConnectionManager.js"></script>
<script src="assets/js/serverFunctions.js"></script>

<button type="button" id="inButton" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#Modal"><i class="fa-solid fa-plus"></i> Coche</button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#Modal" data-bs-whatever="@fat">Open modal for @fat</button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#Modal" data-bs-whatever="@getbootstrap">Open modal for @getbootstrap</button>

<div class="modal fade" id="Modal" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div id="modalContent" class="modal-content">
    </div>
  </div>
</div>

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
        
        // Open Server Button
        openServerButton.addEventListener('click', function() {
            window.location.href = 'http://'+config["httpHost"]+'/serverController/open.php';
        });
        inButton.addEventListener('click', function() {
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