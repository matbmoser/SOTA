<?php
  $configs = include('../assets/mod/configs/config.php');
  if(!empty($_COOKIE["__LOGIN__"]) && $_COOKIE["__LOGIN__"] == "TRUE"){
    header("Location:  ../");
  }
  
  include('../assets/mod/user/loginCookies.php');
    

  $user = "";
  $pass = "";
  $errorType="";
  require("../assets/mod/cryptool/class.Encryption.php");
  include("../assets/mod/user/requestuser.php");

  $responses = include("../assets/mod/front/responses.php");
  if(isset($_COOKIE["__err__"])){
    $errorType = $_COOKIE["__err__"];
  }
  
?>
<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Digital Twin Login</title>
<link rel="stylesheet" type="text/css" href="../assets/css/login.css"/>
<link rel="stylesheet" type="text/css" href="../assets/css/main.css"/>
<link rel="stylesheet" type="text/css" href="../assets/bt/css/bootstrap.css"/>
<script src="../assets/js/libs/jquery/jquery-3.5.1.slim.min.js"></script>
<script src="https://kit.fontawesome.com/6d67b863f5.js" crossorigin="anonymous"></script>
<link rel="icon" type="image/x-icon" href="../media/favicon.ico">
</head>
<script>var configs = <?php echo json_encode($configs); ?>;</script>
<section class="gradient-custom">

<div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" style="border-radius: 1rem;">
          <div class="main-card card-body text-center">

            <form id="loginform" method="post" class="needs-validation" novalidate autocomplete="off">

              <img class="loginlogo" id="logo" src="../media/img/logowhite.png"/>
              <h2 class="loginTitle fw-bold mb-2 mb-4">Digital Twin</h2>
              

              <div class="form-floating mb-4">
                <input type="email" id="inputEmail" value="<?php echo $user?>" class="form-control fieldsForm" placeholder="example@email.com" required/>
                <label for="inputEmail">Email</label>
                <div class="valid-feedback">
                    OK!
                </div>
                <div class="invalid-feedback">
                    Introduzca un email válido.
                </div>
              </div>

              <div class="form-floating mb-4">
                <input type="password" id="inputPassword" class="form-control fieldsForm" placeholder="Password" required/>
                <label class="form-label" for="inputPassword">Password</label>
                <div class="valid-feedback">
                    OK!
                </div>
                <div class="invalid-feedback">
                    Introduzca su contraseña.
                </div>
              </div>


              <div class="d-flex justify-content-left align-items-center checkbox mb-4">
                <input type="checkbox" style="height: 17px;width: 17px;vertical-align: middle;" id="remember" value="check">  
                <label for="remember" style="padding:5px">Remember me</label>
              </div>
              <button id="buttonLogin" class="btn btn-outline-light btn-lg w-100" type="submit">Login</button>
              <div id="loading" class='mt-5 alert alert-light d-flex justify-content-center align-items-center fade show' role='alert'>
                <span><strong class='mr-2'>Cargando...</strong></span>
                <button type='button' class='spinner-border ml-4 text-light bg-transparent' data-dismiss='alert' aria-label='Close'></button>
            </div>
            </form>
          </div>
        </div>
        <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
          <symbol id="exclamation-triangle-fill" fill="currentColor" viewBox="0 0 16 16">
            <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
          </symbol>
          <symbol id="check-circle-fill" fill="currentColor" viewBox="0 0 16 16">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
          </symbol>
        </svg>
        <?php
            if(isset($errorType) && array_key_exists($errorType, $responses)){
                echo $responses[$errorType];
            }
          ?>
      </div>
    </div>
  </div>
</section>
<script src="../assets/bt/js/bootstrap.js"></script>
<script src="../assets/js/libs/crypto-js/aes.js"></script>
<script src="../assets/js/cryptool/hashFunctions.js"></script>
<script src="../assets/js/login/login.js"></script>