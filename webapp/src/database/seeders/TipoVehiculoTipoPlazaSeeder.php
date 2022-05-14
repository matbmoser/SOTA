<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\TipoPlaza;
use App\Models\TipoVehiculo;
use App\Models\TipoVehiculoTipoPlaza;

class TipoVehiculoTipoPlazaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Linea')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'A')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'A')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Linea')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'B')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'B')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'C')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'D')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'E')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'BateriaDiagonal')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'D')->get("id")[0]->id
            ],
            []
        );
        TipoVehiculoTipoPlaza::firstOrCreate(
            [
                "idTipoPlaza" => TipoPlaza::where('tipo', 'BateriaDiagonal')->get("id")[0]->id,
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'E')->get("id")[0]->id
            ],
            []
        );
    }
}