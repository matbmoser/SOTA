<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTipoVehiculoTable extends Migration
{
    public function up()
    {
        Schema::create('TipoVehiculo', function (Blueprint $table) {

		$table->increments('id');
		$table->text('nombre');
		$table->integer('ancho',);
		$table->integer('largo',);
		$table->integer('alto',);
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('TipoVehiculo');
    }
}