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
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "A",
                "clasificacion" => "pequeño"
            ],
            [
                "ancho" => 1.72,
                "largo" => 2.98,
                "alto" => 1.66
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "B",
                "clasificacion" => "medio pequeño"    
            ],
            [
                "clasificacion" => "medio pequeño",
                "ancho" => 1.82,
                "largo" => 4.49,
                "alto" => 1.7
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "C",
                "clasificacion" => "medio",
            ],
            [
                
                "ancho" => 1.98,
                "largo" => 4.77,
                "alto" => 1.86
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "D",
                "clasificacion" => "medio grande"
            ],
            [
                
                "ancho" => 1.93,
                "largo" => 4.77,
                "alto" => 1.83
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "E", 
                "clasificacion" => "grande"
            ],
            [
                "ancho" => 1.98,
                "largo" => 5.01,
                "alto" => 1.815
            ]
        );


    }
}
