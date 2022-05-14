<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Zona;

class ZonaController extends Controller
{
    /*  
    // Display a listing of the resource.
    @return \Illuminate\Http\Response
    */
    public function index()
    {
        $zonas = Zona::all();
        return response()->json(
            [
                'success' => true,
                'zonas' => $zonas->toArray()
            ], 200);
    }
    
    // Show the form for creating a new resource.
    /*
    @return \Illuminate\Http\Response
    */
    public function show($id)
    {
        $zona = Zon::find($id);
        return response()->json(
            [
                'success' => true,
                'zona' => $zona->toArray()
            ], 200);
    }
    
}
