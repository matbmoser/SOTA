<?php
setcookie("UUID",$configs["securityUUIDToken"], time() + 3600, "/");
  if(!empty($_GET)){ //Checkeamos si la variable GET esta puesta
      if(isset($_GET['result'])){
          switch ($_GET['result']){

            case $configs["securityErrorToken"]:
              setcookie("PHPSESSID","", time() - 3600, "/");
              setcookie("__chgn", "",time() - 3600, "/");
              setcookie("__err__", "securityError",time() + 3600,"/");
              break;
            
            case $configs["notAuthorizedToken"]:
              setcookie("__err__", "notAutorized",time() + 3600,"/");
              setcookie("PHPSESSID","", time() - 3600, "/");
              break;
            
            case $configs["wrongUserPassToken"]:
              setcookie("__err__", "wrongUserPass",time() + 3600,"/");
              break;
            
            case $configs["successToken"]:
              setcookie("__err__", "success",time() + 3600,"/");
              break;
            
            case $configs["wrongRequestToken"]:
              setcookie("__err__", "wrongRequest",time() + 3600,"/");
              break;
            
            case $configs["connectionFail"]:
              setcookie("__err__", "connectionFail",time() + 3600,"/");
              break;
          }
      }
      header("Location:  ./");
    }
    ?>