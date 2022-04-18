<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\Usuario;
use App\Models\Rol;

class UsuarioSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Usuario::firstOrCreate(
        ['email' => "mathiasmoser@outlook.com"],
        [
            'nombre' => "Mathias",
            'username' => "matbmoser",
            'apellido1' => "Brunkow",
            'apellido2' => "Moser",
            'documento' => "07164545J",
            'telefono' => "647637778",
            'password' =>  hash("sha512","123456789"),
            'token' => hash("sha256","mathiasmoser@outlook.com".hash("sha512","123456789")),
            'fechaNacimiento' => "2000-09-26",
            'correoConfirmado' => 0,
            'fechaUltimaConexion' => now(),
            'idRol' => Rol::where('nombre', 'Administrador')->get("id")[0]->id
        ]);

        Usuario::firstOrCreate(
            ['email' => "prueba@gmail.com"],
            [
                'nombre' => "Prueba",
                'username' => "Prueba123",
                'apellido1' => "Prueba12321",
                'apellido2' => "Prueba12345",
                'documento' => "12132123",
                'telefono' => "512131",
                'password' =>  hash("sha512","123456789"),
                'token' => hash("sha256","prueba@gmail.com".hash("sha512","123456789")),
                'fechaNacimiento' => "1952-10-26",
                'correoConfirmado' => 0,
                'fechaUltimaConexion' => now(),
                'idRol' => Rol::where('nombre', 'Usuario')->get("id")[0]->id
            ]);
    }
}
