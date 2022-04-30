<?php 
$configs = include("../configs/config.php");

if (!isset( $_POST )) {
    son_encode(array("success" => "false", "err"=>"Bad Request"));
    exit;
}

if(empty( $_POST['uuid']) ||  $_POST['uuid'] != $configs["securityUUIDToken"]){

    echo json_encode(array("success" => "false", "err"=>"Not Authorized"));
    exit;
}

$dbconfig = include("../configs/db.config.php");
include("class.Table.php");
$tablaPlaza = new Table($dbconfig, "Plaza");
$conditions = array(
  'return_type' => 'all',
  'where'       => array(
    'valido' => '1'
  ),
);

$plazasOcupadas = $tablaPlaza->getRows($conditions);


echo json_encode(array("success" => "true","plazas" => $plazasOcupadas));
