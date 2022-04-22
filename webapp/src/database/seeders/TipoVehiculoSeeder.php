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
                "ancho" => 172,
                "largo" => 298,
                "alto" => 166
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "B",
                "clasificacion" => "medio pequeño"    
            ],
            [
                "clasificacion" => "medio pequeño",
                "ancho" => 182,
                "largo" => 449,
                "alto" => 170
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "C",
                "clasificacion" => "medio",
            ],
            [
                
                "ancho" => 198,
                "largo" => 477,
                "alto" => 186
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "D",
                "clasificacion" => "medio grande"
            ],
            [
                
                "ancho" => 193,
                "largo" => 477,
                "alto" => 183
            ]
        );
        TipoVehiculo::firstOrCreate(
            [
                "segmento" => "E", 
                "clasificacion" => "grande"
            ],
            [
                "ancho" => 198,
                "largo" => 501,
                "alto" => 181
            ]
        );


    }
}
