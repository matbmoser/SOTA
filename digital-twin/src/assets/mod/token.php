<?php

$username = "";
$token = "";

$token = $_SESSION['token'];
$username = $_SESSION['username'];

if(empty($token) || empty($username)){
  error("securityErrorToken");
  exit;
}

if(!$result = $conexion->query("SELECT * FROM Usuario")){
  error("connectionFailToken");
  exit;
}

$row = $result->fetch_object();
$r_token = hash('sha256',$row->email.$row->password);

if($token != $r_token){
  error("securityErrorToken");
  exit;
}

$roleResult = $conexion->query("SELECT * FROM Rol WHERE `id`=".$row->idRol);
$rowResult = $roleResult->fetch_object();

if($rowResult->digitalTwin != 1){
  error("notAuthorizedToken");
}

$username = $row->username;
?>