<?php

    $conexion   = new mysqli($dbconfig["host"], $dbconfig["user"], $dbconfig["pass"], $dbconfig["name"]);
    $acentos    = $conexion->query("SET NAMES 'utf8'");
    if ($conexion->connect_error) {
        echo json_encode(array('responseCode' => $configs["connectionFailToken"]));
        die("La conexion falló: " . $conexion->connect_error);
    }
/** MathiasBrunkowMosermatbmoser07160465J64763778mathiasmoser@outlook.com
 * INSERT INTO `Rol` (`nombre`, `incidencias`, `digitalTwin`, `created_at`, `updated_at`) VALUE ('Administrador', 1, 1, NOW(), NOW());
 * INSERT INTO `Usuario`(`nombre`, `username`, `apellido1`, `apellido2`, `documento`, `telefono`, `email`, `password`, `token`, `fechaNacimiento`, `correoConfirmado`, `correoConfirmadoEn`, `fechaUltimaConexion`, `idRol`, `created_at`, `updated_at`) VALUES ('Mathias','matbmoser','Brunkow','Moser','07160465J','64763778','mathiasmoser@outlook.com','d9e6762dd1c8eaf6d61b3c6192fc408d4d6d5f1176d0c29169bc24e71c3f274ad27fcd5811b313d681f7e55ec02d73d499c95455b6b5bb503acf574fba8ffe85','719f2b3ffdc309d0b11faa29b5c69142a568a7afd21a9f7dcdcb080d244d3738','2000-09-26',1,NOW(),NOW(),1,NOW(),NOW()); */

    ?>
