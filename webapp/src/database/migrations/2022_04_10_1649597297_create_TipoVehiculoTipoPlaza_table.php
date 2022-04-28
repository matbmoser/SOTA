<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTipoVehiculoTipoPlazaTable extends Migration
{
    public function up()
    {
        Schema::create('TipoVehiculoTipoPlaza', function (Blueprint $table) {

		$table->integer('idTipoVehiculo',)->unsigned();
		$table->integer('idTipoPlaza',)->unsigned();
		$table->primary(['idTipoVehiculo','idTipoPlaza']);
        $table->foreign('idTipoVehiculo')->references('id')->on('TipoVehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->foreign('idTipoPlaza')->references('id')->on('TipoPlaza')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('TipoVehiculoTipoPlaza');
    }
}