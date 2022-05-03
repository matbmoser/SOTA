<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Models\Vehiculo;
use App\Models\User;
use App\Models\TipoVehiculo;
use Illuminate\Support\Facades\Validator;

class VehiculoController extends Controller
{
        /*  
        // Display a listing of the resource.
        @return \Illuminate\Http\Response
        */
        public function index()
        {
            $vehiculos = Vehiculo::all();
            return response()->json(
                [
                    'success' => true,
                    'vehiculos' => $vehiculos->toArray()
                ], 200);
        }
        

        public function vehiculosUser($id){
            $user = User::where('id', '=', $id)->first();
            if ($user === null) {
                return response()->json([
                    'success' => false,
                    'message' => "User does not exists!"
                ], 401);
            }
            $vehiculos = Vehiculo::where('idUsuario', '=', $id)->get()->toArray();

            if($vehiculos == null){
                return response()->json([
                    'success' => false,
                    'message' => "User has no vehicles"
                ], 401);
            }

            $tipoVehiculos = TipoVehiculo::where('id' ,'>' ,0)->get()->toArray();
            $segmentos = TipoVehiculo::where('id' ,'>' ,0)->pluck('segmento','id')->toArray();
            $clasificaciones = TipoVehiculo::where('id' ,'>' ,0)->pluck('clasificacion','id')->toArray();
            
            $infoVehiculos = array();
                foreach($vehiculos as $vehiculo){
                    $v = array(
                        "id" => $vehiculo["id"],
                        "matricula" => $vehiculo["matricula"],
                        "numAparcamientos" => $vehiculo["numAparcamientos"],
                        "ultimoAparcamiento" => $vehiculo["ultimoAparcamiento"],
                        "segmento" => $segmentos[$vehiculo["idTipoVehiculo"]],
                        "clasificacion" => $clasificaciones[$vehiculo["idTipoVehiculo"]],
                        "created_at" => $vehiculo["created_at"]
                    );
                    array_push($infoVehiculos,$v);
                }
                return response()->json(
                    [
                        'success' => true,
                        'vehiculos' => $infoVehiculos,
                        'tipoVehiculos' => $tipoVehiculos
                    ], 200);

                }

        // Show the form for creating a new resource.
        /*
        @return \Illuminate\Http\Response
        */
        public function show($id)
        {
            $vehiculo = Vehiculo::find($id);
            return response()->json(
                [
                    'success' => true,
                    'vehiculo' => $vehiculo->toArray()
                ], 200);
        }
        
        /*
        @return \Illuminate\Http\Response
        */
        public function create($matricula, $idTipoVehiculo, $idUsuario) {
            return Vehiculo::firstOrCreate(
                ["matricula" => $matricula],
                [
                    "idTipoVehiculo" => $idTipoVehiculo,
                    "idUsuario" => $idUsuario
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
            $v = Validator::make($request->all(), [
                'matricula' => 'required|max:9|unique:Vehiculo',
                'idTipoVehiculo' => 'required|integer',
                'idUsuario' => 'required|integer',
            ]);
            if ($v->fails())
            {
                return response()->json([
                    'status' => 'error',
                    'errors' => $v->errors()
                ], 422);
            }
      
            $vehiculo = new Vehiculo;
            $vehiculo->matricula = $request->input('matricula');
            $vehiculo->idTipoVehiculo = $request->input('idTipoVehiculo');
            $vehiculo->idUsuario = $request->input('idUsuario');
            $vehiculo->save(); //storing values as an object
    
            return response()->json(
                    [
                        'success' => true,
                        'vehiculo' => $vehiculo,
                        'message' => "The vehicle was stored!"
                    ], 200);
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
                'matricula' => 'required|max:9|unique:Vehiculo',
                'idTipoVehiculo' => 'required|integer',
                'idUsuario' => 'required|integer',
            ]);

      
            $vehiculo = Vehiculo::findorFail($id);
            $vehiculo->matricula = $request->input('matricula');
            $vehiculo->idTipoVehiculo = $request->input('idTipoVehiculo');
            $vehiculo->idUsuario = $request->input('idUsuario');
            $vehiculo->save(); //storing values as an object
    
            return $vehiculo;
        }
        /*
        @param  int  $id
    
        @return \Illuminate\Http\Response
        */
        public function delete(Request $request)
        {
            $v = Validator::make($request->all(), [
                'id' => 'required|integer',
                'idUsuario' => 'required|integer',
            ]);
            if ($v->fails())
            {
                return response()->json([
                    'status' => 'error',
                    'errors' => $v->errors()
                ], 422);
            }
            if($request->input('idUsuario') != Auth::user()->id){
                return response()->json([
                    'success' => false,
                    'message' => "You can delete only your own vehicles!"
                ], 401);
            }
            $vehiculo = Vehiculo::where("idUsuario",Auth::user()->id)->where('id', $request->input('id'))->first(); //searching for object in database using ID
            if($vehiculo != null){ //deletes the object
                $vehiculo->delete();
                return response()->json(
                    [
                        'success' => true,
                        'message' => "The vehicle was deleted!"
                    ], 200);
            }else{
                return response()->json([
                    'success' => false,
                    'message' => "The vehicle don't exists or you don't own the vehicle!"
                ], 401);
            }
        }
    }
