<?php

function error($type, $configs){
    if(array_key_exists($type, $configs)){
        $host = $_SERVER['HTTP_HOST'];
        header("Location: http://'.$host.'/login/?result=".$configs[$type]);  
        exit;
    }
}

?>