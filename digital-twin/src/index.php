<?php
require_once("assets/mod/connect.php");
require_once("assets/mod/session.php");

if(empty( $_SESSION["token"] )){
    header('Location: login/');
    exit;
  }

require_once("assets/mod/token.php");
include("assets/mod/config.php");
require_once("assets/mod/fallos.php");

if (empty($username)){
    header('Location: login/');
} 

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
<script src="assets/js/CameraClient.js"></script>
<script src="assets/js/SJMPHandler.js"></script>
<script src="assets/js/config.js"></script>
<script src="assets/js/hashFunctions.js"></script>
<script src="assets/js/printFunctions.js"></script>
<script src="assets/js/workflowFunctions.js"></script>
<script src="assets/js/createClientFunctions.js"></script>

<div id="pagewrapper" style="display: none!important;"> 
    <body>
    <header class="header sticky-top">
    <nav class="navbar navbar-expand-lg shadow">
      <a class="navbar-brand" href="../../">
      	<img id="mylogo" src="../../media/img/logo2.png">
      </a>
      <button class="navbar-toggler" style="border-radius: 0!important;" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <i class="fa fa-bars"></i>
  </button>
  <script src="../../assets/js/dark-mode.js"></script>
  <div class="collapse navbar-collapse" id="navbarText">
    <div class="w-100 d-flex justify-content-end">
        <ul class="nav navbar-nav justify-content-end align-items-center">
        <li class="nav-item">
            <?php
            if ($username != "") {
                echo "<span>Welcome <strong>" . $_SESSION['username'] . "</strong>!</span>";
            } else {
                echo "<a class='nav-link'  href='./login/index.php?result=eb31b018bdf10eda25e94c40e73736aa'><strong>Log in</strong></span></a>";
            }
            ?>
        </li>
            <li class="nav-item">
            <button type="button" class="ml-3 logout btn btn-light btn-outline-dark" onclick="window.location.href= './assets/mod/logout.php?uuid=<?php echo $configs['logoutToken'] ?>'"><i class="fas fa-sign-out-alt"></i> <span>Log out</span></button>
            </li>
            <li class="nav-item">
            	<button type="button" id="dark-mode" class="ml-3 btn btn-outline-light"><i class="fas fa-sun mr-1"></i><span>Light Mode</span></button>
          	</li>
        </ul>
    </div>
  </div>
   </nav>
</header>
        <div>
            <h2>Welcome <?php echo $_SESSION['username'] ?></h2><br><br>
            <button type="submit" id="submit">Start</button> 
            
            <div id="config" class="hidden">
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
    <button style="position: fixed; bottom: 20px; left: 20px;" type="button" onclick="window.location.href = 'http://<?php echo $_SERVER['HTTP_HOST']; ?>/serverController/open.php;" id="openserver">Open Server</button> 
    <button style="position: fixed; top: 20px; right: 20px;" type="button" id="clean">Clean</button> 
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
<script src="../assets/bt/js/bootstrap.js"></script>
<script src="../assets/js/libs/crypto-js/aes.js"></script>
<script src="../assets/js/hashFunctions.js"></script>
<script src="assets/js/main.js"></script>


<script>
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