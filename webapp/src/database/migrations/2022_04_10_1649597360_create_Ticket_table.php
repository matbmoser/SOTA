<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTicketTable extends Migration
{
    public function up()
    {
        Schema::create('Ticket', function (Blueprint $table) {

		$table->increments('id');
		$table->integer('plaza',);
		$table->string('token',128)->unique()->comment('Unique hash');
		$table->datetime('fechaEntrada');
		$table->datetime('fechaSalida');
		$table->boolean('valido')->default('1');
		$table->boolean('incidencia')->default('0');
		$table->integer('idZona',)->unsigned();
		$table->integer('idUsuario',)->unsigned();
		$table->integer('idVehiculo',)->unsigned();
		$table->foreign('idUsuario')->references('id')->on('Usuario')->onUpdate('CASCADE')->onDelete('CASCADE');   
        $table->foreign('idVehiculo')->references('id')->on('Vehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');   
		$table->foreign('idZona')->references('id')->on('Zona')->onUpdate('CASCADE')->onDelete('CASCADE');   
        $table->timestamps();    
		});
    }

    public function down()
    {
        Schema::dropIfExists('Ticket');
    }
}