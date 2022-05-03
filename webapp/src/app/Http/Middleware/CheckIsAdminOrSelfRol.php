<?php
namespace App\Http\Middleware;
use App\Models\Rol;
use Closure;
use Illuminate\Support\Facades\Auth;
class CheckIsAdminOrSelfRol
{
    public function handle($request, Closure $next)
    {
        $requestedUserId = $request->route()->parameter('id');
        if(
            Auth::user()->idRol === Rol::where("nombre", "Administrador")->get("id")[0]->id ||
            Auth::user()->idRol == $requestedUserId 
        ) {
            return $next($request);
        }
        else {
            return response()->json(['error' => 'Unauthorized'], 403);
        }
    }
}