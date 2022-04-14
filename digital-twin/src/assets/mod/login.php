
<?php
$configs = include('config.php');

if (empty($_POST['email']) || empty($_POST['pass']) || $_POST['uuid'] != $configs["safetyUUID"]){

    echo json_encode(array('success' => '0'));

} else {
    include("connect.php");
    $sql = "SELECT * from `Usuario` where `email`="."'".mysqli_real_escape_string($conexion,$_POST['email'])."'"." AND `password`="."'".mysqli_real_escape_string($conexion,$_POST['pass'])."'";
    if($result = $conexion->query($sql)){
        $row = $result->fetch_object();
        $token = hash('sha256',$row->email.$row->password);
        if($row->username != NULL && $_POST['token'] == $token){
            $arraySucess=array('success' => '1');
            $userData = json_decode(json_encode($row), true);
            echo json_encode(array_merge($arraySucess,$userData));
        }else{
            echo json_encode(array('success' => '-2'));
        }
    }else{
        echo json_encode(array('success' => '-1'));
    }
}
