<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\TipoVehiculo;

class TipoVehiculoController extends Controller
{
    /*  
    // Display a listing of the resource.
    @return \Illuminate\Http\Response
    */
    public function index()
    {
        $tipoVehiculos = TipoVehiculo::all();
        return response()->json(
            [
                'success' => true,
                'tipoVehiculos' => $tipoVehiculos->toArray()
            ], 200);
    }
    
    // Show the form for creating a new resource.
    /*
    @return \Illuminate\Http\Response
    */
    public function show($id)
    {
        $tipoVehiculo = TipoVehiculo::find($id);
        return response()->json(
            [
                'success' => true,
                'zotipoVehiculo' => $tipoVehiculo->toArray()
            ], 200);
    }
}
