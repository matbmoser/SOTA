<?php

namespace App\Http\Controllers;
use App\Models\Plaza;
use App\Models\Zona;
use App\Models\TipoPlaza;
use App\Models\Vehiculo;
use App\Models\User;
use App\Models\Incidencia;


use Illuminate\Http\Request;

class IncidenciaController extends Controller
{
        /*  
    // Display a listing of the resource.
    @return \Illuminate\Http\Response
    */
    public function index()
    {
        $incidencias = Incidencia::all()->toArray();
        if($incidencias == null || $incidencias == []){
            return response()->json([
                'success' => false,
                'message' => "There is no issues!"
            ], 401);
        }
        return response()->json(
            [
                'success' => true,
                'incidencias' => $incidencias
            ], 200);
    }
    public function getIncidencias($id)
    {   
        $vehiculosUsuario = Vehiculo::where("idUsuario", $id)->get()->toArray();
        $plazas = Plaza::all()->toArray();
        $incidencias = Incidencia::all()->toArray();
        
        if($plazas == null || $vehiculosUsuario == null || $incidencias == null || $incidencias == []){
            return response()->json([
                'success' => false,
                'message' => "The user has no issues!"
            ], 401);
        }

        $incidencias = array();
        foreach ($vehiculosUsuario as $vehiculo){
            foreach ($plazas as $plaza){
                if($plaza["idVehiculo"] != $vehiculo["id"]){
                    continue;    
                }
                if($plaza["incidencia"] != 1){
                    continue;
                }
                $indicencia = Incidencia::where("tokenPlaza", $plaza["token"]);

                array_push($incidencias, $indicencia);
            }
        }

        return response()->json(
            [
                'success' => true,
                'incidencias' => $incidencias,
            ], 200);
    }
}
