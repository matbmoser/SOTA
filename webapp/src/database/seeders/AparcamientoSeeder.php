<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\Aparcamiento;
use App\Models\Universidad;

class AparcamientoSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Aparcamiento::firstOrCreate(
            ["letra" => "Y"],
            [
                "color" => "Amarillo",
                "localizacion" => "SurEste",
                "idUniversidad" => Universidad::where('sigla', 'UFV')->get("id")[0]->id
            ]
        );
        
    }
}
