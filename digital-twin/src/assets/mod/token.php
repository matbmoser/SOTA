<?php
require_once("fallos.php");
$token = $_SESSION['token'];
$id = $_SESSION['id'];
  if(!empty($token) && !empty($id)){
    include("connect.php");
    require_once("sha.php");
   
    if($result = $conexion->query("SELECT * FROM Usuario")){
        $row = $result->fetch_object();
        $r_token = hash('sha256',$row->email.$row->password);
          if($token == $r_token){
              $username = $row->username;
            }else{
              error151();
            }
        }else{
          error151();
        }
    }
    else{
      error101();
    }
?>