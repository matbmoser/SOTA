<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Plaza;
use App\Models\Zona;
use App\Models\TipoPlaza;

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
                if($zona["id"] == $plaza["idZona"]){
                    $nplazas++;
                }
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
}
