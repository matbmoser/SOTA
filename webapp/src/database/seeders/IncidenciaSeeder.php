<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Incidencia;
use App\Models\Vehiculo;
use App\Models\Plaza;


class IncidenciaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Incidencia::firstOrCreate(
            [
                'gravedad' => 4,
                'titulo' => "Aparcamiento Ilegal",
                'descripcion' => "El vehiculo con matricula 4545-ASD aparcó en dos plazas",
                'tokenPlaza' => Plaza::where("idVehiculo", Vehiculo::where("matricula", "3201-PGL")->get("id")[0]->id)->get("token")[0]->token,
            ]);
    }
}
