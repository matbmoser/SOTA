<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\User;
use App\Models\Rol;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;

class UserController extends Controller
{
    /*  
    // Display a listing of the resource.
    @return \Illuminate\Http\Response
    */
    public function index()
    {
        $users = User::all();
        return response()->json(
            [
                'success' => true,
                'users' => $users->toArray()
            ], 200);
    }
    
    // Show the form for creating a new resource.
    /*
    @return \Illuminate\Http\Response
    */
    public function show($id)
    {
        $user = User::find($id);
        return response()->json(
            [
                'success' => true,
                'user' => $user->toArray()
            ], 200);
    }
    

    public function edit($id) {
        //editing data
    }
    /*
    @return \Illuminate\Http\Response
    */
    public function create($email, $nombre, $username, $apellido1, $apellido2, $documento, $telefono, $password, $fechaNacimiento, $rolname) {
        return User::firstOrCreate(
            ['email' => $email],
            [
                'nombre' => $nombre,
                'username' =>  $username,
                'apellido1' => $apellido1,
                'apellido2' => $apellido2,
                'documento' => $documento,
                'telefono' => $telefono,
                'password' =>  hash("sha512",$password),
                'token' => hash("sha256",$email.hash("sha512",$password)),
                'fechaNacimiento' =>  $fechaNacimiento,
                'correoConfirmado' => 0,
                'fechaUltimaConexion' => now(),
                'idRol' => Rol::where('nombre', $rolname)->get("id")[0]->id
            ]);
    }
    /*
    // Store a newly created resource in storage.   
        @param  \Illuminate\Http\Request  $request

        @return \Illuminate\Http\Response
    */
    public function store(Request $request)
    {
        $this->validate($request, [ //inputs are not empty or null
            'email' => 'required|email|unique:users',
            'nombre' => 'required',
            'nombre' => 'required',
            'username' =>  'required|unique:users',
            'apellido1' => 'required',
            'apellido2' => 'required',
            'documento' => 'required',
            'telefono' => 'required',
            'password' =>  'required',
            'fechaNacimiento' =>  'required',
            'rolName' => 'required',
        ]);
  
        $usuario = new User;
        $usuario->email = $request->input('email');
        $usuario->nombre = $request->input('nombre');
        $usuario->username = $request->input('username');
        $usuario->apellido1 = $request->input('apellido1');
        $usuario->apellido2 = $request->input('apellido2');
        $usuario->documento = $request->input('documento');
        $usuario->telefono = $request->input('telefono');
        $usuario->password = bcrypt($request->input('password'));
        $usuario->token = hash("sha256",$usuario->email.$usuario->password);
        $usuario->fechaNacimiento = $request->input('fechaNacimiento');
        $usuario->correoConfirmado = 0;
        $usuario->fechaUltimaConexion = now();
        $usuario->idRol = Rol::where('nombre', $request->input('rolName'))->get("id")[0]->id;
        $usuario->save(); //storing values as an object


        return $usuario;
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
            'email' => 'required',
            'nombre' => 'required',
            'nombre' => 'required',
            'username' =>  'required',
            'apellido1' => 'required',
            'apellido2' => 'required',
            'documento' => 'required',
            'telefono' => 'required',
            'password' =>  'required',
            'fechaNacimiento' =>  'required',
            'rolName' => 'required',
        ]);
  
        $usuario = User::findorFail($id);
        $usuario->email = $request->input('email');
        $usuario->nombre = $request->input('nombre');
        $usuario->username = $request->input('username');
        $usuario->apellido1 = $request->input('apellido1');
        $usuario->apellido2 = $request->input('apellido2');
        $usuario->documento = $request->input('documento');
        $usuario->telefono = $request->input('telefono');
        $usuario->password = hash("sha512",$request->input('password'));
        $usuario->token = hash("sha256",$usuario->email.$usuario->password);
        $usuario->fechaNacimiento = $request->input('fechaNacimiento');
        $usuario->correoConfirmado = 0;
        $usuario->fechaUltimaConexion = now();
        $usuario->idRol = Rol::where('nombre', $request->input('rolName'))->get("id")[0]->id;
        $usuario->save(); //storing values as an object
        
        return $usuario; //returns the stored value if the operation was successful.
    }
    public function updateData(Request $request, $id)
    {       
        $v = Validator::make($request->all(), [
            'id' => 'required|integer',
            'email' => 'required|email',
            'nombre' => 'required',
            'username' =>  'required',
            'password' =>  'required',
            'password_confirmation' => 'required|same:password', 
        ]);
        if ($v->fails())
        {
            return response()->json([
                'status' => 'error',
                'errors' => $v->errors()
            ], 422);
        }
  
        $usuario = User::findorFail($id);
        if($usuario == null){
            return response()->json([
                'success' => false,
                'message' => "Usuario no encontrado!"
            ], 401);
        }
        $usuario->email = $request->input('email');
        $usuario->nombre = $request->input('nombre');
        $usuario->username = $request->input('username');
        $usuario->password = bcrypt($request->input('password'));
        $usuario->token = hash("sha256",$usuario->email.hash("sha512",$request->input('password')));
        $usuario->fechaUltimaConexion = now();
        $usuario->save(); //storing values as an object

        $token = Auth::guard()->attempt(['email' => strtolower($request->input('email')), 'password' => request('password')]);
        
        return response()->json([
            'success' => true,
            'user' => $usuario
        ], 200)->header('Authorization', $token);;
    }
    /*
    @param  int  $id

    @return \Illuminate\Http\Response
    */
    public function delete($id)
    {
        $usuario = User::findorFail($id); //searching for object in database using ID
        if($usuario->delete()){ //deletes the object
            return 'deleted successfully'; //shows a message when the delete operation was successful.
        }
    }
}
