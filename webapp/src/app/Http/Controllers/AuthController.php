<?php
namespace App\Http\Controllers;
use App\Models\User;
use App\Models\Rol;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Validator;

class AuthController extends Controller
{
    /*
    public function register(Request $request)
    {
        
        $v = Validator::make($request->all(), [
            'email' => 'required|email|unique:Usuario',
            'nombre' => 'required',
            'username' =>  'required|unique:Usuario',
            'apellido1' => 'required',
            'apellido2' => 'required',
            'documento' => 'required',
            'telefono' => 'required',
            'password' =>  'required',
            'password_confirmation' => 'required|same:password', 
            'fechaNacimiento' =>  'required',
            'rolName' => 'required',
        ]);
        if ($v->fails())
        {
            return response()->json([
                'status' => 'error',
                'errors' => $v->errors()
            ], 422);
        }
        $usuario = new User;
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
        return response()->json(['status' => 'success'], 200);
    }
    */
    /**
     * Generate a new user for login
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function register(Request $request){ 
        $v = Validator::make($request->all(), [
            'email' => 'required|email|unique:users',
            'nombre' => 'required',
            'username' =>  'required|unique:users',
            'apellido1' => 'required',
            'apellido2' => 'required',
            'documento' => 'required',
            'telefono' => 'required',
            'password' =>  'required',
            'password_confirmation' => 'required|same:password', 
            'fechaNacimiento' =>  'required'
        ]);
        if ($v->fails())
        {
            return response()->json([
                'status' => 'error',
                'errors' => $v->errors()
            ], 422);
        }
        
        /**
         * Creamos el usuario y ciframos su password
         */
        $usuario = new User;
        $usuario->email =  strtolower($request->input('email'));
        $usuario->nombre = $request->input('nombre');
        $usuario->username =  strtolower($request->input('username'));
        $usuario->apellido1 = $request->input('apellido1');
        $usuario->apellido2 = $request->input('apellido2');
        $usuario->documento = $request->input('documento');
        $usuario->telefono = $request->input('telefono');
        $usuario->password = bcrypt($request->input('password'));
        $usuario->token = hash("sha256",$usuario->email.$usuario->password);
        $usuario->fechaNacimiento = $request->input('fechaNacimiento');
        $usuario->correoConfirmado = 0;
        $usuario->fechaUltimaConexion = now();
        $usuario->idRol = Rol::where('nombre', 'Usuario')->get("id")[0]->id;
        $usuario->save(); //storing values as an object
        
        $token = $this->guard()->attempt(['email' => strtolower($request->input('email')), 'password' => request('password')]);
        #With passport $success['token'] =  $usuario->createToken('__appMyParking')->accessToken;
        return response()->json([
            'success' => true,
            'user' => $usuario
        ], 200)->header('Authorization', $token);;
    }


    public function login(Request $request){
        if($token = $this->guard()->attempt(['email' => strtolower($request->input('email')), 'password' => request('password')])) {
            $user = $this->guard()->user();
            
            #Wtih passport $success['token'] =  $user->createToken('__appMyParking')-> accessToken;
            return response()->json([
                'success' => true,
                'user' => $user
            ])->header('Authorization', $token);
        }
        else{
            return response()->json([
                'success' => false,
                'message' => 'Invalid Email or Password',
            ], 401);
        }
    }
    public function logout()
    {
        $this->guard()->logout();
        return response()->json([
            'success' => true,
            'message' => 'Logged out Successfully.'
        ], 200);
    }
    public function check()
    {
        if ($this->guard()->check()) {
            return response()->json([
                'success' => true
            ], 200);
        }else{
            return response()->json([
                'success' => false
            ], 401);
        }
    }
    public function user(Request $request)
    {
        $usuario = User::find(Auth::user()->id);
        return response()->json([
            'status' => 'success',
            'data' => $usuario
        ]);
    }
    public function refresh()
    {
        if ($token = $this->guard()->refresh()) {
            return response()
                ->json(['status' => 'success'], 200)
                ->header('Authorization', $token);
        }
        return response()->json(['error' => 'refresh_token_error'], 401);
    }
    private function guard()
    {
        return Auth::guard();
    }
}