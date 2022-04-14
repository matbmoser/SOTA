<?php
$configs = include('config.php');

// ERROR 151
// ERROR POR FALLA DE SEGURIDAD
function error151(){
    $host = $_SERVER['HTTP_HOST'];
    header("Location: http://'.$host.'/login/index.php?result=".$configs["safetyUUID"]);  
    exit;
}


// ERROR 441
// ERROR USUARIO NO AUTORIZADO
function error441(){
    $host = $_SERVER['HTTP_HOST'];
    header('Location: http://'.$host.'/login/index.php?result='.$configs["notAutorizedToken"]);  
    exit;
}

// ERROR 101
// ERROR POR FALTA DE SESSIÓN INICIADA
function error101(){
    $host = $_SERVER['HTTP_HOST'];
    header('Location: http://'.$host.'/login/index.php?result=0');  
    exit;
}


?>