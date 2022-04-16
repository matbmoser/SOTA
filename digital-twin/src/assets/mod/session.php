<?php
session_start();
if (!empty( $_GET )) {
    if(!empty( $_GET['token'] ) && !empty( $_GET['username'] )){
        $_SESSION['username'] = $_GET['username'];
        $_SESSION['token'] = $_GET['token'];
        header('Location: ./');
    }
}
?>
