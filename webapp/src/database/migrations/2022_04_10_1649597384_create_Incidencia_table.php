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
		$table->text('matriculaImplicada');
		$table->string('titulo');
		$table->text('descripcion');
		$table->datetime('fechaApertura');
		$table->datetime('fechaCierre');
		$table->boolean('resuelta');
		$table->text('notaCierre');
		$table->text('nombreArchivoFoto');
		$table->integer('idAprobador',)->unsigned();
		$table->integer('idTicket',)->unsigned();
		$table->integer('idTipoIncidencia',)->unsigned();
		$table->foreign('idAprobador')->references('id')->on('Usuario')->onUpdate('CASCADE')->onDelete('CASCADE'); 
		$table->foreign('idTicket')->references('id')->on('Ticket')->onUpdate('CASCADE')->onDelete('CASCADE'); 
		$table->foreign('idTipoIncidencia')->references('id')->on('TipoIncidencia')->onUpdate('CASCADE')->onDelete('CASCADE'); 
        $table->timestamps();    
		});
    }

    public function down()
    {
        Schema::dropIfExists('Incidencia');
    }
}