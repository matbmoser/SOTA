<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Universidad;

class UniversidadSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Universidad::firstOrCreate(
        [
            'sigla' => "UFV",
            'email' => "gerencia@ufv.es"
        ],
        [
            'nombre' => "Universidad Francisco de Vitoria",
            'email' => "gerencia@ufv.es",
            'telefono' => "+34 91 709 14 00",
            'direccion' => "Ctra. Pozuelo-Majadahonda KM 1.800",
            'codigoPostal' => 28223,
            'ciudad' => "Pozuelo de Alarcón",
            'comunidad' => "Comunidad de Madrid",
            'pais' => "España"
        ]);
    }
}
