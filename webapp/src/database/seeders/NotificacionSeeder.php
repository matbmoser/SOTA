<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use App\Models\Notificacion;
use App\Models\User;
use App\Models\Vehiculo;
use App\Models\Plaza;

class NotificacionSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Notificacion::firstOrCreate(
            [
                'titulo' => "Incidencia Creada",
                'descripcion' => "Titulo: Aparcamiento Ilegal, Contenido: El vehiculo con matricula 4545-ASD aparcó en dos plazas",
                'boton' => 1,
                'tituloBoton' => "Ver Incidencia",
                'enlaceBoton' => "incidencias/".Plaza::where("idVehiculo", Vehiculo::where("matricula", "3201-PGL")->get("id")[0]->id)->get("token")[0]->token,
                'idUsuario' => User::where("id", Vehiculo::where("matricula", "3201-PGL")->get("idUsuario")[0]->idUsuario)->get("id")[0]->id,
            ]);
    }
}
