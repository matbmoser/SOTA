<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;
use App\Models\TipoPlaza;
use App\Models\Aparcamiento;
use App\Models\Zona;

class ZonaSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Zona::firstOrCreate(
            ["letra" => "A"],
            [
                "plazas" => 24,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "B"],
            [
                "plazas" => 25,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "C"],
            [
                "plazas" => 22,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "D"],
            [
                "plazas" => 21,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "E"],
            [
                "plazas" => 21,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "F"],
            [
                "plazas" => 21,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "G"],
            [
                "plazas" => 21,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'BateriaDiagonal')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "H"],
            [
                "plazas" => 4,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Linea')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        Zona::firstOrCreate(
            ["letra" => "I"],
            [
                "plazas" => 23,
                "idTipoPlaza" => TipoPlaza::where('tipo', 'Bateria')->get("id")[0]->id,
                "idAparcamiento" => Aparcamiento::where('letra', 'Y')->get("id")[0]->id
            ]
        );
        
    }
}
