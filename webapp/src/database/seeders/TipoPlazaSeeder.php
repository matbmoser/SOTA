<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\TipoPlaza;

class TipoPlazaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        TipoPlaza::firstOrCreate(
            [
                "tipo" => "Bateria"
            ],
            [
                "ancho" => 250,
                "largo" => 515,
            ]
        );

        TipoPlaza::firstOrCreate(
            [
                "tipo" => "BateriaDiagonal"
            ],
            [
                "ancho" => 300,
                "largo" => 555,
            ]
        );

        TipoPlaza::firstOrCreate(
            [
                "tipo" => "Linea"
            ],
            [
                "ancho" => 200,
                "largo" => 500,
            ]
        );
    }
}
