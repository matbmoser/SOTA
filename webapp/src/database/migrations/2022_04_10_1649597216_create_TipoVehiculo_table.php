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
		$table->string('nombre', 30)->unique();
		$table->float('ancho',);
		$table->float('largo',);
		$table->float('alto',);
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('TipoVehiculo');
    }
}