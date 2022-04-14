<?php

if(isset($_COOKIE["PHPSESSID"])){
        if (isset($_COOKIE["__chgn"])&&isset($_COOKIE["__efbr"])) {
            if($_COOKIE["__chgn"] != "" || $_COOKIE["__efbr"] != "") {
                require("class.Encryption.php");
                $password = $_COOKIE["PHPSESSID"];
                $user = encryption::decrypt($_COOKIE["__chgn"], $password);
                #$pass = encryption::decrypt($_COOKIE["__efbr"], $password);
            }else{
                $user = "";
                #$pass = "";
            }
        }else{
            $user = "";
            #$pass = "";
        }
}else{
    session_start();
    $user = "";
    #$pass = "";
}
?>