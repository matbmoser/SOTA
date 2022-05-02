<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Rol;

class RolController extends Controller
{
        /*  
        // Display a listing of the resource.
        @return \Illuminate\Http\Response
        */
        public function index()
        {
            $roles = Rol::all();
            return response()->json(
                [
                    'status' => 'success',
                    'roles' => $roles->toArray()
                ], 200);
        }
        
        // Show the form for creating a new resource.
        /*
        @return \Illuminate\Http\Response
        */
        public function show($id)
        {
            $rol = Rol::find($id);
            return response()->json(
                [
                    'status' => 'success',
                    'rol' => $rol->toArray()
                ], 200);
        }
        
    
        public function edit($id) {
            //editing data
        }
        /*
        @return \Illuminate\Http\Response
        */
        public function create($nombre, $incidencias, $userDashboard) {
            return Rol::firstOrCreate(
                ["nombre" => $nombre],
                [
                    "incidencias" => $incidencias,
                    "digitalTwin" => $digitalTwin,
                    "userDashboard" => $userDashboard
                ]
            );
        }
        /*
        // Store a newly created resource in storage.   
            @param  \Illuminate\Http\Request  $request
    
            @return \Illuminate\Http\Response
        */
        public function store(Request $request)
        {
            $this->validate($request, [ //inputs are not empty or null
                'nombre' => 'required|unique:Rol',
                'digitalTwin' => 'required|bool',
                'incidencias' => 'required|bool',
                "userDashboard" => 'required|bool'
            ]);
      
            $rol = new Rol;
            $rol->nombre = $request->input('nombre');
            $rol->digitalTwin = $request->input('digitalTwin');
            $rol->incidencias = $request->input('incidencias');
            $rol->userDashboard = $request->input('userDashboard');
            $rol->save(); //storing values as an object
    
            return $rol;
        }
        /*
        @param  int  $id
    
        @param  \Illuminate\Http\Request  $request
    
        @param  int  $id
     
        @return \Illuminate\Http\Response
        */
        public function update(Request $request, $id)
        {
            $this->validate($request, [ //inputs are not empty or null
                'nombre' => 'required|unique:Rol',
                'digitalTwin' => 'required|bool',
                'incidencias' => 'required|bool',
                "userDashboard" => 'required|bool'
            ]);
      
            $rol = Rol::findorFail($id);
            $rol->nombre = $request->input('nombre');
            $rol->digitalTwin = $request->input('digitalTwin');
            $rol->incidencias = $request->input('incidencias');
            $rol->userDashboard = $request->input('userDashboard');
            $rol->save(); //storing values as an object
    
            return $rol;
        }
        /*
        @param  int  $id
    
        @return \Illuminate\Http\Response
        */
        public function delete($id)
        {
            $rol = Rol::findorFail($id); //searching for object in database using ID
            if($rol->delete()){ //deletes the object
                return 'deleted successfully'; //shows a message when the delete operation was successful.
            }
        }
    }