<?php

$username = "";
$token = "";



$token = $_SESSION['token'];
$username = $_SESSION['username'];

if(empty($token) || empty($username)){
  error151();
  exit;
}

if(!$result = $conexion->query("SELECT * FROM Usuario")){
  error101();
  exit;
}

$row = $result->fetch_object();
$r_token = hash('sha256',$row->email.$row->password);

if($token != $r_token){
  error101();
  exit;
}

$roleResult = $conexion->query("SELECT * FROM Rol WHERE `id`=".$row->idRol);
$rowResult = $roleResult->fetch_object();

if($rowResult->digitalTwin != 1){
  error441();
}

$username = $row->username;
?>