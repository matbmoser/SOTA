<?php
$pid = $_POST['pid'];
$configs = include("../assets/mod/configs/config.php");
if(!isset($_POST['uuid'])){
    echo '{"fail":"Bad Request"}';
    exit;
}

if($_POST['uuid'] != $configs["securityUUIDToken"]){
   echo '{"fail":"Bad Request UUID"}';
   exit;
}

$output = shell_exec('./closeServer.sh '.$pid);
echo json_encode(array("success"=>"true", "serverData" => json_decode($output)));