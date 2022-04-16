<?php
$pid = $_POST['pid'];
$configs = include("../assets/mod/config.php");
if(!isset($_POST['uuid'])){
    echo '{"fail":"Bad Request"}';
    exit;
}

if($_POST['uuid'] != $configs["securityUUIDToken"]){
   echo '{"fail":"Bad Request UUID"}';
   exit;
}

$output = shell_exec('./closeServer.sh '.$pid);
echo "<pre>$output</pre>";