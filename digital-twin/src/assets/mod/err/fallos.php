<?php

function error($type){
    if(array_key_exists($type, $configs)){
        $host = $_SERVER['HTTP_HOST'];
        header("Location: http://'.$host.'/login/index.php?result=".$configs[$type]);  
        exit;
    }
}

?>