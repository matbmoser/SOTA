<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateVehiculoTable extends Migration
{
    public function up()
    {
        Schema::create('Vehiculo', function (Blueprint $table) {

		$table->increments('id');
		$table->string('matricula',9)->unique();
        $table->integer('numAparcamientos',)->default(0);
        $table->datetime('ultimoAparcamiento')->nullable();
		$table->integer('idTipoVehiculo',)->unsigned();
        $table->integer('idUsuario',)->unsigned();
        $table->foreign('idUsuario')->references('id')->on('users')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->foreign('idTipoVehiculo')->references('id')->on('TipoVehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();   
        });
    }

    public function down()
    {
        Schema::dropIfExists('Vehiculo');
    }
}