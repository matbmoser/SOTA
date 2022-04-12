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
		$table->datetime('fechaRegistro');
		$table->integer('idTipoVehiculo',)->unsigned();
        $table->foreign('idTipoVehiculo')->references('id')->on('TipoVehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();   
        });
    }

    public function down()
    {
        Schema::dropIfExists('Vehiculo');
    }
}