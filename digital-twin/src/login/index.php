<?php
$configs = include('../assets/mod/config.php');
if(!empty($_COOKIE["__LOGIN__"]) && $_COOKIE["__LOGIN__"] == "TRUE"){
  header("Location:  ../index.php");
}
setcookie("UUID",$configs["safetyUUID"], time() + 3600, "/");
 
if(!empty($_GET)){ //Checkeamos si la variable GET esta puesta
  if(isset($_GET['result'])){
      if($_GET['result'] ==  $configs["sefetyErrorToken"]){
          setcookie("PHPSESSID","", time() - 3600, "/");
          setcookie("__chgn", "",time() - 3600, "/");
          setcookie("__err__", "TRUE",time() - 3600,"/");
      }
  }else{
      header("Location:  index.php");
  }
}




$user = "";
$pass = "";
require_once("../assets/mod/requestuser.php");
?>
<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<title>Digital Twin Login</title>
<link rel="stylesheet" type="text/css" href="../assets/css/login.css"/>
<link rel="stylesheet" type="text/css" href="../assets/css/main.css"/>
<link rel="stylesheet" type="text/css" href="../assets/bt/css/bootstrap.css"/>
<script src="../assets/js/libs/jquery/jquery-3.5.1.slim.min.js"></script>
<script src="https://kit.fontawesome.com/6d67b863f5.js" crossorigin="anonymous"></script>
<link rel="icon" type="image/x-icon" href="../media/favicon.ico">
</head>
<section class="vh-100 gradient-custom">

<div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <form id="loginform" method="post" class="needs-validation" novalidate autocomplete="off">

              <img class="loginlogo" id="logo" src="../media/img/logowhite.png"/>
              <h2 class="fw-bold mb-2 text-uppercase mb-4">Digital Twin</h2>
              

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
                    Introduzca su password.
                </div>
              </div>


              <div class="d-flex justify-content-left align-items-center checkbox mb-4">
              <input type="checkbox" style="height: 17px;width: 17px;vertical-align: middle;" id="remember" value="check">  
              <label for="remember" style="padding:5px">Remember me</label>
                </div>
              <button id="buttonLogin" class="btn btn-outline-light btn-lg w-100" type="submit">Login</button>
              
              <?php
              if(isset($_GET['result'])){
                if($_GET['result'] == "1"){
                  echo "<div class='mt-5 alert alert-success d-flex justify-content-between align-items-center fade show' role='alert'>
                  <span><strong class='mr-2'>Enhorabuena!</strong> El login ha sido realizado!</span>
                </div>";
                }
                else if ($_GET['result'] == "0"){
                echo"<div class='mt-5 alert alert-danger fade show' role='alert'>
                  <strong>¡Qué pena!</strong> Algo salió mal. Intente hacer el login otra vez.
                </div>";
                }
                else if($_GET['result'] == $configs["notAuthorizedToken"]){
                  echo"<div class='mt-5 text-justify alert alert-danger alert-dismissible fade show'  role='alert' style='text-align: justify;'>
                  <strong>¡Usuario no Autorizado!</strong> No estás autorizado a acceder al digital twin. Contacte con un administrador en: <a target='_blank' href='mailto:ufvmyparking@gmail.com' >ufvmyparking@gmail.com</a>
                  
                  <button type='button' class='btn-close' data-dismiss='alert' aria-label='Close'></button>
                  </div>";
                
                }
              }
              if(isset($_COOKIE["__err__"]) && $_COOKIE["__err__"] == "TRUE"){
                  echo"<div class='mt-5 text-justify alert alert-warning alert-dismissible fade show'  role='alert' style='text-align: justify;'>
                  <strong>¡Error de Seguridad!</strong> Hemos detectado un intento de falla de seguridad en su cuenta!
                  La hemos bloqueado por seguridad, vuelva a hacer el login, sentimos las molestias.
                  </div>";
                  setcookie("__err__", "",time() - 3600,"/");
              }
              ?>
              
              <div id="loading" class='mt-5 alert alert-light d-flex justify-content-center align-items-center fade show' role='alert'>
                <span><strong class='mr-2'>Cargando...</strong></span>
                <button type='button' class='spinner-border ml-4 text-light bg-transparent' data-dismiss='alert' aria-label='Close'></button>
            </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<script src="../assets/bt/js/bootstrap.js"></script>
<script src="../assets/js/libs/crypto-js/aes.js"></script>
<script src="../assets/js/hashFunctions.js"></script>
<script src="../assets/js/check.js"></script>