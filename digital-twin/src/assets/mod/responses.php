
<?php

return array(
    
    "notAutorized" => "<div class='alertMessage mt-5 text-justify alert alert-danger alert-dismissible fade show'  role='alert' style='text-align: justify;'>
                        <svg class='bi flex-shrink-0 me-2' width='24' height='24' role='img' aria-label='Warning:'><use xlink:href='#exclamation-triangle-fill'/></svg>
                        <strong>Usuario no Autorizado</strong> No estás autorizado a acceder al digital twin. Contacte con un administrador en: <a target='_blank' href='mailto:ufvmyparking@gmail.com' >ufvmyparking@gmail.com</a>
                        <button type='button' class='btn-close' id='closeButton' data-bs-dismiss='alert' aria-label='Close'></button>
                        </div>",
    "wrongUserPass" => "<div class='alertMessage mt-5 text-justify alert alert-danger alert-dismissible fade show' role='alert'>
                        <svg class='bi flex-shrink-0 me-2' width='24' height='24' role='img' aria-label='Danger:'><use xlink:href='#exclamation-triangle-fill'/></svg>
                        <strong>Ups...</strong> El usuario o la contraseña son incorrectos.
                        <button type='button' class='btn-close' id='closeButton' data-bs-dismiss='alert' aria-label='Close'></button>
                        </div>",
    "securityError" => "<div class='alertMessage mt-5 text-justify alert alert-dismissible alert-warning alert-dismissible fade show'  role='alert' style='text-align: justify;'>
                        <svg class='bi flex-shrink-0 me-2' width='24' height='24' role='img' aria-label='Warning:'><use xlink:href='#exclamation-triangle-fill'/></svg>
                        <strong>Error de Seguridad</strong> Hemos detectado un intento de falla de seguridad en su cuenta!
                        La hemos bloqueado por seguridad, vuelva a hacer el login, sentimos las molestias.
                        <button type='button' class='btn-close' id='closeButton' data-bs-dismiss='alert' aria-label='Close'></button>
                        </div>",
    "success"       => "<div class='alertMessage mt-5 text-justify alert alert-dismissible alert-success alert-dismissible fade show' role='alert'>
                        <svg class='bi flex-shrink-0 me-2' width='24' height='24' role='img' aria-label='Success:'><use xlink:href='#check-circle-fill'/></svg>
                        <strong class='mr-2'>Success!</strong> El login es correcto.
                        <button type='button' class='btn-close' id='closeButton' data-bs-dismiss='alert' aria-label='Close'></button>
                        </div>",
    "wrongRequest"  => "<div class='alertMessage mt-5 alert alert-danger alert-dismissible fade show' role='alert'>
                        <svg class='bi flex-shrink-0 me-2' width='24' height='24' role='img' aria-label='Danger:'><use xlink:href='#exclamation-triangle-fill'/></svg>
                        <strong>Ups...</strong> ¡Algo salió mal! Intente hacer login otra vez.
                        <button type='button' class='btn-close' id='closeButton' data-bs-dismiss='alert' aria-label='Close'></button>
                        </div>",
    "connectionFail" => "<div class='alertMessage mt-5 text-justify alert alert-dismissible alert-warning alert-dismissible fade show'  role='alert' style='text-align: justify;'>
                        <svg class='bi flex-shrink-0 me-2' width='24' height='24' role='img' aria-label='Warning:'><use xlink:href='#exclamation-triangle-fill'/></svg>
                        <strong>Error de Conexión</strong> No ha sido posible realizar el login, sentimos las molestias. Vuelva a intentarlo en unos minutos.
                        <button type='button' class='btn-close' id='closeButton' data-bs-dismiss='alert' aria-label='Close'></button>
                        </div>"
                    );