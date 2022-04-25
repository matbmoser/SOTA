<?php

if(isset($_COOKIE["PHPSESSID"])){
        if (isset($_COOKIE["__chgn"])) {
            if($_COOKIE["__chgn"] != "" || $_COOKIE["__efbr"] != "") {
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