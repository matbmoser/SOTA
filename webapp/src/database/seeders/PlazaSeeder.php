<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Zona;
use App\Models\User;
use App\Models\Vehiculo;
use App\Models\Plaza;

class PlazaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Plaza::firstOrCreate(
            ["letra" => "Y"],
            [   
                "token" =>hash("sha512",) 
                "color" => "Amarillo",
                "localizacion" => "SurEste",
                "idUniversidad" => Universidad::where('sigla', 'UFV')->get("id")[0]->id
            ]
        );
        
    }
}
