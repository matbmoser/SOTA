<?php

$nombre = "";
$token = "";

if(empty($_SESSION['token']) || empty($_SESSION['username'])){
  
  error("securityErrorToken", $configs);
  exit;
}

$token = $_SESSION['token'];
$username = $_SESSION['username'];

$token = mysqli_real_escape_string($conexion,$token);
if(!$result = $conexion->query("SELECT * FROM users WHERE token='$token' ")){
  error("connectionFailToken", $configs);
  exit;
}

$usuario = $result->fetch_object();

$roleResult = $conexion->query("SELECT * FROM Rol WHERE `id`=".$usuario->idRol);
$rowResult = $roleResult->fetch_object();


$permits = $rowResult;
$username = $usuario->username;
?>