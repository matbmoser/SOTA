<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\Rol;

class RolSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Rol::firstOrCreate(
            ["nombre" => "Administrador"],
            [
                "incidencias" => 1,
                "digitalTwin" => 1,
                "userDashboard" => 1
            ]
        );
        Rol::firstOrCreate(
            ["nombre" => "Manager"],
            [
                "incidencias" => 1,
                "digitalTwin" => 1,
                "userDashboard" => 0
            ]
        );
        
        Rol::firstOrCreate(
            ["nombre" => "Usuario"],
            [
                "incidencias" => 0,
                "digitalTwin" => 0,
                "userDashboard" => 0
            ]
        );
    }
}
