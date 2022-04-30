<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Zona;
use App\Models\User;
use App\Models\Vehiculo;
use App\Models\TipoVehiculoTipoPlaza;
use App\Models\Plaza;
use Illuminate\Support\Facades\DB;

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
            [
                "id" => 1,
                "idVehiculo" => Vehiculo::where('matricula', '4321-ZXC')->get("id")[0]->id,
                "idZona" =>  Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '1605-LDJ')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id,
                "valido" => 1,
            ],
            [
                "fechaEntrada" => now(),
                "incidencia" => 0,
                "token" => hash("sha512","\$token{".now()."1". Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '1605-LDJ')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id."}"), 
            ]
        );
        Plaza::firstOrCreate(
            [
                "id" => 2,
                "idVehiculo" => Vehiculo::where('matricula', '1234-ZXC')->get("id")[0]->id,
                "idZona" =>  Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '1234-ZXC')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id,
                "valido" => 1,
            ],
            [
                "fechaEntrada" => now(),
                "incidencia" => 0,
                "token" => hash("sha512","\$token{".now()."2". Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '1234-ZXC')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id."}"), 
            ]
        );
        Plaza::firstOrCreate(
            [
                "id" => 1,
                "idZona" =>  Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '3201-PGL')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id,
                "valido" => 1,
                "idVehiculo" => Vehiculo::where('matricula', '3201-PGL')->get("id")[0]->id,
            ],
            [
                "fechaEntrada" => now(),
                "incidencia" => 1,
                "token" => hash("sha512","\$token{".now()."1". Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '3201-PGL')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id."}"), 
            ]
        );
        Plaza::firstOrCreate(
            [
                "id" => 3,
                "idVehiculo" => Vehiculo::where('matricula', '4561-QWR')->get("id")[0]->id,
                "idZona" =>  Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula',  '4561-QWR')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id,
                "valido" => 1,
            ],
            [
                "fechaEntrada" => now(),
                "incidencia" => 0,
                "token" => hash("sha512","\$token{".now()."3". Zona::whereIn("idTipoPlaza", TipoVehiculoTipoPlaza::where("idTipoVehiculo", Vehiculo::where('matricula', '4561-QWR')->get("id")[0]->id)->get("idTipoPlaza"))->inRandomOrder()->first()->id."}"), 
            ]
        );
         
    }
}
