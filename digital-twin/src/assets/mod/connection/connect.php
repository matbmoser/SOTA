<?php

    $conexion   = new mysqli($dbconfig["host"], $dbconfig["user"], $dbconfig["pass"], $dbconfig["name"]);
    $acentos    = $conexion->query("SET NAMES 'utf8'");
    if ($conexion->connect_error) {
        echo json_encode(array('responseCode' => $configs["connectionFailToken"]));
        die("La conexion falló: " . $conexion->connect_error);
    }

    ?>
