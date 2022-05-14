<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateZonaTable extends Migration
{
    public function up()
    {
        Schema::create('Zona', function (Blueprint $table) {

		$table->increments('id');
		$table->string('letra',2)->unique();
        $table->integer('plazas',);
		$table->integer('idTipoPlaza',)->unsigned();
		$table->integer('idAparcamiento',)->unsigned();
        $table->foreign('idAparcamiento')->references('id')->on('Aparcamiento')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->foreign('idTipoPlaza')->references('id')->on('TipoPlaza')->onUpdate('CASCADE')->onDelete('CASCADE');  
        $table->timestamps();    
        });
    }

    public function down()
    {
        Schema::dropIfExists('Zona');
    }
}