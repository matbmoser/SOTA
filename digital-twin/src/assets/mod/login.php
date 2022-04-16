
<?php
$configs = include('config.php');
$dbconfig = include("db.config.php");
include("connect.php");
if (empty($_POST['email']) || empty($_POST['pass']) || $_POST['uuid'] != $configs["securityUUIDToken"]){

    echo json_encode(array('responseCode' => $configs["wrongRequestToken"]));
    exit;

}

$sql = "SELECT * from `Usuario` where `email`="."'".mysqli_real_escape_string($conexion,$_POST['email'])."'"." AND `password`="."'".mysqli_real_escape_string($conexion,$_POST['pass'])."'";
if($result = $conexion->query($sql)){
    $row = $result->fetch_object();
    if(empty($row)){
        echo json_encode(array('responseCode' => $configs["wrongUserPassToken"]));
        exit;
    }
    $token = hash('sha256',$row->email.$row->password);
    if($row->username == NULL && $_POST['token'] != $token){
        echo json_encode(array('responseCode' => $configs["securityErrorToken"]));
        exit;
    }

    $arraySucess=array('responseCode' => $configs["successToken"]);
    $userData = json_decode(json_encode($row), true);
    echo json_encode(array_merge($arraySucess,$userData));

}else{
    echo json_encode(array('responseCode' => $configs["connectionFail"]));
}

