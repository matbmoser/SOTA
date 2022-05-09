<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateNotificacionTable extends Migration
{
    public function up()
    {
        Schema::create('Notificacion', function (Blueprint $table) {

		$table->increments('id');
		$table->string('titulo');
		$table->text('descripcion');
		$table->boolean('boton')->defalt(0);
		$table->string('tituloBoton',25)->nullable();
		$table->text('enlaceBoton')->nullable();
		$table->integer('idUsuario',)->unsigned();
        $table->foreign('idUsuario')->references('id')->on('users')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('Notificacion');
    }
}