
<!DOCTYPE html>
<head>
<meta charset = "utf-8" />
<title>Digital Twin Login</title>
<link rel="stylesheet" type="text/css" href="../assets/css/login.css"/>
<link rel="stylesheet" type="text/css" href="../assets/css/main.css"/>
<script src="../assets/js/libs/jquery/jquery-3.5.1.slim.min.js"></script>
<script src="https://kit.fontawesome.com/6d67b863f5.js" crossorigin="anonymous"></script>
<link rel="stylesheet" type="text/css" href="../assets/bt/css/bootstrap.css"/>
</head>
<section class="vh-100 gradient-custom">

<div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card bg-dark text-white" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">

            <form id="loginform" method="post" class="mb-md-5 mt-md-4 pb-5 needs-validation" novalidate autocomplete="off">

              <h2 class="fw-bold mb-2 text-uppercase">Digital Twin <br>Login</h2>
              <p class="text-white-50 mb-5">¡Introduzca su Correo y Contraseña de Administrador en MyParking!</p>

              <div class="form-floating mb-4">
                <input type="email" id="inputEmail" class="form-control fieldsForm" placeholder="example@email.com"/>
                <label for="email">Email</label>
                <div class="valid-feedback">
                    OK!
                </div>
                <div class="invalid-feedback">
                    Introduzca un email válido.
                </div>
              </div>

              <div class="form-floating mb-4">
                <input type="password" id="inputPassword" class="form-control fieldsForm" placeholder="Password"/>
                <label class="form-label" for="password">Password</label>
                <div class="valid-feedback">
                    OK!
                </div>
                <div class="invalid-feedback">
                    Introduzca su password.
                </div>
              </div>


              <div class="checkbox mb-4">
                <label>
                    <input type="checkbox" id="remember" value="check"> Remember me
                </label>
                </div>
              <button id="buttonLogin" class="btn btn-outline-light btn-lg w-100" type="submit">Login</button>
              <div id="demo" class='mt-5 alert alert-info d-flex justify-content-center align-items-center fade show' role='alert'>
                <span><strong class='mr-2'>Cargando...</strong></span>
                <button type='button' class='spinner-border ml-4 text-info bg-transparent' data-dismiss='alert' aria-label='Close'></button>
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
<script src="../assets/js/check.js"></script>
<script>
/*
loginButton = document.getElementById("buttonLogin")

loginButton.onclick = function() {
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;

    if(email=="" or password=="" or email == null or password==null){

    }

}
*/

</script>