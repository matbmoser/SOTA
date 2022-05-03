<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\User;
use App\Models\Rol;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        User::firstOrCreate(
        ['email' => "mathiasmoser@outlook.com"],
        [
            'nombre' => "Mathias",
            'username' => "matbmoser",
            'apellido1' => "Brunkow",
            'apellido2' => "Moser",
            'documento' => "07164545J",
            'telefono' => "647637778",
            'password' =>  bcrypt("123456789"),
            'token' => hash("sha256","mathiasmoser@outlook.com".hash("sha512","123456789")),
            'fechaNacimiento' => "2000-09-26",
            'correoConfirmado' => 0,
            'fechaUltimaConexion' => now(),
            'idRol' => Rol::where('nombre', 'Administrador')->get("id")[0]->id
        ]);

        User::firstOrCreate(
            ['email' => "conductor@email.com"],
            [
                'nombre' => "Conductor",
                'username' => "conductor",
                'apellido1' => "MyParking",
                'documento' => "TSH123156",
                'telefono' => "621232548",
                'password' =>  bcrypt("123456789"),
                'token' => hash("sha256","prueba@gmail.com".hash("sha512","123456789")),
                'fechaNacimiento' => "1952-10-26",
                'correoConfirmado' => 0,
                'fechaUltimaConexion' => now(),
                'idRol' => Rol::where('nombre', 'Usuario')->get("id")[0]->id
            ]);
        User::firstOrCreate(
            ['email' => "admin@myparking.com"],
            [
                'nombre' => "Admin",
                'username' => "admin",
                'apellido1' => "MyParking",
                'documento' => "YJAD67676",
                'telefono' => "21354995456",
                'password' =>  bcrypt("789456123"),
                'token' => hash("sha256","admin@ufv.myparking.com".hash("sha512","789456123")),
                'fechaNacimiento' => "2022-04-28",
                'correoConfirmado' => 0,
                'fechaUltimaConexion' => now(),
                'idRol' => Rol::where('nombre', 'Administrador')->get("id")[0]->id
            ]);
        User::firstOrCreate(
            ['email' => "manager@myparking.com"],
            [
                'nombre' => "Manager",
                'username' => "manager",
                'apellido1' => "MyParking",
                'documento' => "HJAMS45621",
                'telefono' => "5213688712",
                'password' =>  bcrypt("789456123"),
                'token' => hash("sha256","manager@myparking.com".hash("sha512","789456123")),
                'fechaNacimiento' => "2022-04-28",
                'correoConfirmado' => 0,
                'fechaUltimaConexion' => now(),
                'idRol' => Rol::where('nombre', 'Manager')->get("id")[0]->id
            ]);
    }
}
