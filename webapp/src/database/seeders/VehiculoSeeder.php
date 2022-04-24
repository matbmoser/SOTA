<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\Vehiculo;
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
                "idTipoVehiculo" => TipoVehiculo::where('segmento', 'C')->get("id")[0]->id
            ]
        );
        
    }
}
