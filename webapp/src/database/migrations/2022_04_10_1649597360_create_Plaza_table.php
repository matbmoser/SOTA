<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePlazaTable extends Migration
{
    public function up()
    {
        Schema::create('Plaza', function (Blueprint $table) {
				
			$table->integer('id',)->unsigned();
			$table->datetime('fechaEntrada')->now();
			$table->datetime('fechaSalida');
			$table->boolean('valido')->default('1');
			$table->boolean('incidencia')->default('0');
			$table->integer('idZona',)->unsigned();
			$table->integer('idVehiculo',)->unsigned();
			$table->primary(['id','idZona','valido']);
			$table->string('token',128)->unique()->comment('Unique sha512 hash');
			$table->foreign('idVehiculo')->references('id')->on('Vehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');   
			$table->foreign('idZona')->references('id')->on('Zona')->onUpdate('CASCADE')->onDelete('CASCADE');   
			$table->timestamps();    
		});
    }

    public function down()
    {
        Schema::dropIfExists('Plaza');
    }
}