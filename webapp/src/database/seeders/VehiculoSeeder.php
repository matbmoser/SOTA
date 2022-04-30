<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\Vehiculo;
use App\Models\User;
use App\Models\TipoVehiculo;

class VehiculoSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Vehiculo::firstOrCreate(
            ["matricula" => "1605-LDJ"],
            [
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'C')->get("id")[0]->id,
                "idUsuario" => User::where('username', 'matbmoser')->get("id")[0]->id
            ]
        );
        Vehiculo::firstOrCreate(
            ["matricula" => "4561-QWR"],
            [
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'A')->get("id")[0]->id,
                "idUsuario" => User::where('username', 'manager')->get("id")[0]->id
            ]
        );
        Vehiculo::firstOrCreate(
            ["matricula" => "3201-PGL"],
            [
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'E')->get("id")[0]->id,
                "idUsuario" => User::where('username', 'matbmoser')->get("id")[0]->id
            ]
        );
        Vehiculo::firstOrCreate(
            ["matricula" => "1234-ZXC"],
            [
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'D')->get("id")[0]->id,
                "idUsuario" => User::where('username', 'conductor')->get("id")[0]->id
            ]
        );
        Vehiculo::firstOrCreate(
            ["matricula" => "4321-ZXC"],
            [
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'E')->get("id")[0]->id,
                "idUsuario" => User::where('username', 'conductor')->get("id")[0]->id
            ]
        );
        Vehiculo::firstOrCreate(
            ["matricula" => "4545-ASD"],
            [
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'B')->get("id")[0]->id,
                "idUsuario" => User::where('username', 'admin')->get("id")[0]->id
            ]
        );
        
    }
}
