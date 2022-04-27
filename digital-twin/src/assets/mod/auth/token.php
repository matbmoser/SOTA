<?php

$nombre = "";
$token = "";

$token = $_SESSION['token'];
$username = $_SESSION['username'];

if(empty($token) || empty($username)){
  error("securityErrorToken");
  exit;
}

if(!$result = $conexion->query("SELECT * FROM Usuario WHERE token='$token' ")){
  error("connectionFailToken");
  exit;
}

$usuario = $result->fetch_object();

$r_token = hash('sha256',$usuario->email.$usuario->password);

if($token != $r_token){
  error("securityErrorToken");
  exit;
}

$roleResult = $conexion->query("SELECT * FROM Rol WHERE `id`=".$usuario->idRol);
$rowResult = $roleResult->fetch_object();


$permits = $rowResult;
$username = $usuario->username;
?>