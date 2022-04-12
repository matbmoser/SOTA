<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUniversidadTable extends Migration
{
    public function up()
    {
        Schema::create('Universidad', function (Blueprint $table) {

		$table->increments('id');
		$table->integer('nombre',);
        $table->string('email',320)->unique();
        $table->text('telefono');
		$table->integer('sigla',);
		$table->text('direccion');
		$table->integer('codigoPostal',);
		$table->text('ciudad');
		$table->text('comunidad');
		$table->text('pais');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('Universidad');
    }
}