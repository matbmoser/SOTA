<?php

$nombre = "";
$token = "";

$token = $_SESSION['token'];
$username = $_SESSION['username'];

if(empty($token) || empty($username)){
  error("securityErrorToken");
  exit;
}

$token = mysqli_real_escape_string($conexion,$token);
if(!$result = $conexion->query("SELECT * FROM users WHERE token='$token' ")){
  error("connectionFailToken");
  exit;
}

$usuario = $result->fetch_object();

$roleResult = $conexion->query("SELECT * FROM Rol WHERE `id`=".$usuario->idRol);
$rowResult = $roleResult->fetch_object();


$permits = $rowResult;
$username = $usuario->username;
?>