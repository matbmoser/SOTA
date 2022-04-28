<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateIncidenciaTable extends Migration
{
    public function up()
    {
        Schema::create('Incidencia', function (Blueprint $table) {

		$table->increments('id');
		$table->integer('gravedad',)->comment('0-5');
		$table->string('titulo');
		$table->text('descripcion');
		$table->datetime('fechaApertura');
		$table->datetime('fechaCierre');
		$table->boolean('resuelta');
		$table->text('notaCierre');
		$table->text('nombreArchivoFoto');
		$table->integer('idAprobador',)->unsigned();
		$table->integer('idPlaza',)->unsigned();
		$table->integer('idVehiculo',)->unsigned();
		$table->integer('idTipoIncidencia',)->unsigned();
		$table->foreign('idAprobador')->references('id')->on('users')->onUpdate('CASCADE')->onDelete('CASCADE'); 
		$table->foreign('idPlaza')->references('id')->on('Plaza')->onUpdate('CASCADE')->onDelete('CASCADE'); 
		$table->foreign('idVehiculo')->references('id')->on('Vehiculo')->onUpdate('CASCADE')->onDelete('CASCADE');  
        $table->timestamps();    
		});
    }

    public function down()
    {
        Schema::dropIfExists('Incidencia');
    }
}