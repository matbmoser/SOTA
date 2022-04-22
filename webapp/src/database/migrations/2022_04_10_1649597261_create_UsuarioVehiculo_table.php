<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsuarioVehiculoTable extends Migration
{
    public function up()
    {
        Schema::create('UsuarioVehiculo', function (Blueprint $table) {

		$table->integer('idUsuario',)->unsigned();
		$table->integer('idVehiculo',)->unsigned();
		$table->integer('numAparcamientos',);
		$table->datetime('fechaUltimoAparcamiento');
        $table->boolean('aparcado');
		$table->primary(['idUsuario','idVehiculo']);
        $table->foreign('idUsuario')->references('id')->on('Usuario')->onUpdate('CASCADE')->onDelete('CASCADE');   
        $table->foreign('idVehiculo')->references('id')->on('Vehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();   
        });
    }

    public function down()
    {
        Schema::dropIfExists('UsuarioVehiculo');
    }
}