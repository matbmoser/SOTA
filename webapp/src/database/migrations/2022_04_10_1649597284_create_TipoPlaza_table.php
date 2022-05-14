<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTipoPlazaTable extends Migration
{
    public function up()
    {
        Schema::create('TipoPlaza', function (Blueprint $table) {

		$table->increments('id');
		$table->string('tipo', 25)->unique();
		$table->integer('ancho',);
		$table->integer('largo',);
        $table->timestamps();
            
        });
    }

    public function down()
    {
        Schema::dropIfExists('TipoPlaza');
    }
}