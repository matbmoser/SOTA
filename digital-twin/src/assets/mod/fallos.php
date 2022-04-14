<?php

// ERROR 151
// ERROR POR FALLA DE SEGURIDAD
function error151(){
    $host = $_SERVER['HTTP_HOST'];
    header('Location: http://'.$host.'/index.php?result=3ad735ebae3ff8aae1b3dcafa8c8bbff3e877fab8fd9cf7f3c933240f0544a0b');  
    exit;
}

// ERROR 101
// ERROR POR FALTA DE SESSIÓN INICIADA
function error101(){
    $host = $_SERVER['HTTP_HOST'];
    header('Location: http://'.$host.'/index.php?result=0');  
    exit;
}


?>