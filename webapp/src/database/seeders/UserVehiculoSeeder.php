<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\Vehiculo;
use App\Models\User;
use App\Models\UserVehiculo;

class UserVehiculoSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        UserVehiculo::firstOrCreate(
            [
                "idUsuario" => User::where('username', 'matbmoser')->get("id")[0]->id,
                "idVehiculo" => Vehiculo::where('matricula', '1605-LDJ')->get("id")[0]->id
            ],
            [
                "numAparcamientos" => 0,
                "fechaUltimoAparcamiento" => now(),
                "aparcado" => 0
            ]
        );
    }
}
