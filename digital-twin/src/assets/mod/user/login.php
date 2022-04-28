
<?php
$configs = include('../configs/config.php');
$dbconfig = include("../configs/db.config.php");
include("../connection/connect.php");
if (empty($_POST['token']) || $_POST['uuid'] != $configs["securityUUIDToken"]){

    echo json_encode(array('responseCode' => $configs["wrongRequestToken"]));
    exit;

}
$token = mysqli_real_escape_string($conexion, $_POST['token']);
$sql = "SELECT * from `users` where token='$token'";
if($result = $conexion->query($sql)){
        $row = $result->fetch_object();
        if(empty($row)){
            echo json_encode(array('responseCode' => $configs["wrongUserPassToken"]));
            exit;
        }

    $arraySucess=array(
        'responseCode' => $configs["successToken"],
        'username' => $row->username,
        'token' => $row->token
        );

    echo json_encode($arraySucess);

}else{
    echo json_encode(array('responseCode' => $configs["connectionFail"]));
}

