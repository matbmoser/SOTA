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

$output = shell_exec('./get.sh '.$port);
$response = json_decode($output, true);

if(!empty($response["err"])){
    echo json_encode(array("success" => "false", "err" => $response["err"]));
    exit;
}

echo json_encode(array("success" => "true", "server" => $response));
