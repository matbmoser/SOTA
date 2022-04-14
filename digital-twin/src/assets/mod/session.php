<?php
session_start();
require_once("fallos.php");
if (!empty( $_GET )) {
    if(!empty( $_GET['token'] ) && !empty( $_GET['id'] )){
    $_SESSION['id'] = $_GET['id'];
    $_SESSION['token'] = $_GET['token'];
    header('Location: index.php');
   }else{
    session_destroy();
    error151();
   }
   
}
?>
