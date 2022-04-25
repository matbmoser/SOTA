<?php
$configs = include('../configs/config.php');
if (empty( $_GET )) {
    header('Location: ../../../');
    exit;
}
if(empty( $_GET['uuid'] ) || $_GET['uuid'] != $configs["logoutToken"]){
    header('Location: ../../../');
    exit;
}
$_SESSION = [];
session_start();
session_unset();
session_destroy();
session_write_close();
setcookie("__LOGIN__", "",time() - 3600,"/");
header('Location: ../../../login/');
?>