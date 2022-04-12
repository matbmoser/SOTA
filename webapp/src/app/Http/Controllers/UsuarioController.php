<?php

namespace App\Http\Controllers;
use App\Usuario;
use Illuminate\Http\Request;

class UsuarioController extends Controller
{
    public function index()
    {
        return Usuario::all();
    }
 
    public function show($id)
    {
        return Usuario::find($id);
    }

    public function store(Request $request)
    {
        return Usuario::create($request->all());
    }

    public function update(Request $request, $id)
    {
        $article = Usuario::findOrFail($id);
        $article->update($request->all());

        return $article;
    }

    public function delete(Usuario $request, $id)
    {
        $article = Usuario::findOrFail($id);
        $article->delete();

        return 204;
    }
}
