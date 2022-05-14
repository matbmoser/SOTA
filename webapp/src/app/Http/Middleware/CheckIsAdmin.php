<?php
namespace App\Http\Middleware;
use Closure;
use App\Models\Rol;
use Illuminate\Support\Facades\Auth;
class CheckIsAdmin
{
    public function handle($request, Closure $next)
    {
        if(Auth::user()->idRol === Rol::where("nombre", "Administrador")->get("id")[0]->id) {
            return $next($request);
        }
        else {
            return response()->json(['error' => 'Unauthorized'], 403);
        }
    }
}