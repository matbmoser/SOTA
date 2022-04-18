<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\TipoVehiculo;

class TipoVehiculoSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Rol::firstOrCreate(
            ["nombre" => "Compacto"],
            [
                "ancho" => 1.8,
                "largo" => 4.1
                "alto" => 1.45
            ]
        );
    }
}
