<?php
$port = $_POST['port'];
$configs = include("../assets/mod/configs/config.php");
if(!isset($_POST['uuid'])){
    echo '{"fail":"Bad Request"}';
    exit;
}

if($_POST['uuid'] != $configs["securityUUIDToken"]){
   echo '{"fail":"Bad Request UUID"}';
   exit;
}

$output = shell_exec('./getServer.sh '.$port);
echo json_encode(array("success"=>"true", "serverData" => json_decode($output)));