<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Plaza;
use App\Models\Zona;
use App\Models\TipoPlaza;
use App\Models\Vehiculo;

class PlazaController extends Controller
{
    /*  
    // Display a listing of the resource.
    @return \Illuminate\Http\Response
    */
    public function index()
    {
        $plazas = Plaza::all();
        return response()->json(
            [
                'status' => 'success',
                'plazas' => $plazas->toArray()
            ], 200);
    }
    
    public function getTicket($token)
    {
        $plaza = Plaza::where("token", $token)->first();
        if($plaza == null){
            return response()->json([
                'success' => false,
                'message' => "Not valid ticket token!"
            ], 401);
        }
        $matricula = Vehiculo::where('id' ,$plaza["idVehiculo"])->first()->matricula;
        if($matricula == null){
            return response()->json([
                'success' => false,
                'message' => "Not valid ticket vehicle!"
            ], 401);
        }
        $zonas = Zona::where('id' ,'>' ,0)->pluck('letra','id')->toArray();
        $ticket = array(
                "idPlaza" => $zonas[$plaza["idZona"]].$plaza["id"],
                "token" => $plaza["token"],
                "valido" => $plaza["valido"],
                "matricula" => $matricula,
                "entrada" => $plaza["fechaEntrada"],
                "salida" => $plaza["fechaSalida"]
            );
        
        return response()->json(
            [
                'success' => true,
                'ticket' => $ticket,
            ], 200);    
    }

    public function show($id)
    {
        $plaza = Plaza::find($id);
        return response()->json(
            [
                'status' => 'success',
                'plaza' => $plaza->toArray()
            ], 200);
    }
    // Show the form for creating a new resource.
    /*
    @return \Illuminate\Http\Response
    */
    public function validas()
    {
        $plazas = Plaza::where("valido", 1)->get();
        return response()->json(
            [
                'status' => 'success',
                'plazas' => $plazas->toArray()
            ], 200);
    }
        // Show the form for creating a new resource.
    /*
    @return \Illuminate\Http\Response
    */
    public function validasZona()
    {   
        $zonas = Zona::all()->toArray();
        $tipoPlazas = TipoPlaza::where('id' ,'>' ,0)->pluck('tipo','id')->toArray();
        $plazas = Plaza::where("valido", 1)->get()->toArray();
        
        $plazasZonas = array();
        foreach($zonas as $zona){
            $nplazas = 0;
            $vehiculosPlazasZona = array();
            foreach ($plazas as $plaza){
                if($zona["id"] != $plaza["idZona"]){
                    continue;
                }
                $nplazas++;
            }
            $plazasZonas[$zona["id"]] = $nplazas;
        }
        return response()->json(
            [
                'status' => 'success',
                'plazas' => $plazasZonas,
                'zonas' => $zonas,
                'tipoPlazas' => $tipoPlazas
            ], 200);
    }
    /*
    // Store a newly created resource in storage.   
        @param  \Illuminate\Http\Request  $request

        @return \Illuminate\Http\Response
    */
    public function getTickets($id)
    {   
        $zonas = Zona::where('id' ,'>' ,0)->pluck('letra','id')->toArray();
        $vehiculosUsuario = Vehiculo::where("idUsuario", $id)->get()->toArray();
        $plazas = Plaza::all()->toArray();

        $tickets = array();
        foreach ($vehiculosUsuario as $vehiculo){
            foreach ($plazas as $plaza){
                if($plaza["idVehiculo"] != $vehiculo["id"]){
                    continue;    
                }
                    $ticket = array(
                        "idPlaza" => $plaza["id"].$zonas[$plaza["idZona"]],
                        "token" => $plaza["token"],
                        "valido" => $plaza["valido"],
                        "matricula" => $vehiculo["matricula"],
                        "entrada" => $plaza["fechaEntrada"],
                        "salida" => $plaza["fechaSalida"]
                    );
                array_push($tickets, $ticket);
            }
        }

        if($plazas == null || $vehiculosUsuario == null || $tickets == [] || $tickets == null){
            return response()->json([
                'success' => false,
                'message' => "The user has no tickets!"
            ], 401);
        }

        return response()->json(
            [
                'success' => true,
                'tickets' => $tickets,
            ], 200);
    }
}
