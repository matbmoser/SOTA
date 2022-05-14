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

$tablaZona = new Table($dbconfig, "Zona");
$zonas = $tablaZona->getRows(array('return_type' => 'all'));

$tablaVehiculo = new Table($dbconfig, "Vehiculo");
$vehiculos = $tablaVehiculo->getRows(array('return_type' => 'all'));


$tablaTipoVehiculo = new Table($dbconfig, "TipoVehiculo");
$tipoVehiculo = $tablaTipoVehiculo->getRows(array('return_type' => 'all'));

$tablaPlaza = new Table($dbconfig, "Plaza");
$conditions = array(
  'return_type' => 'all',
  'where'       => array(
    'valido' => '1'
  ),
);

$plazasOcupadas = $tablaPlaza->getRows($conditions);
function getIDValue($arr, $id, $value){
  $ids = array();
  foreach ($arr as $elem){
    $ids[$elem[$id]] = $elem[$value];
  }
  return $ids;
}

//Información Vehiculos
$clasificacionesVehiculos = getIDValue($tipoVehiculo, "id", "clasificacion");
$segmentosVehiculos = getIDValue($tipoVehiculo, "id", "segmento");
$idVehiculos = getIDValue($vehiculos, "id", "idTipoVehiculo");
$matriculas = getIDValue($vehiculos, "id", "matricula");


## Información plazas
$plazasZonas = array();
$vehiculosPlazas= array();
foreach ($zonas as $zona) {
  $nplazas = 0;
  $vehiculosPlazasZona = array();
  foreach ($plazasOcupadas as $plaza){
    if($zona["id"] == $plaza["idZona"]){
      $nplazas++;
      array_push($vehiculosPlazasZona, array(
        "idPlaza" => $zona["letra"].$plaza['id'],
        "matricula" => $matriculas[$plaza['idVehiculo']],
        "segmento" => $segmentosVehiculos[$idVehiculos[$plaza["idVehiculo"]]],
        "clasificacion" => $clasificacionesVehiculos[$idVehiculos[$plaza["idVehiculo"]]],
        "created_at" => $plaza['created_at']
      ));
    }
  }
  $plazasZonas[$zona["id"]] = $nplazas;
  $vehiculosPlazas[$zona["id"]] = $vehiculosPlazasZona;
}

echo json_encode(array("success" => "true","plazasZonas" => $plazasZonas, "vehiculosPlazas" => $vehiculosPlazas));
