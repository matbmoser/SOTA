<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateServidorTable extends Migration
{
    public function up()
    {
        Schema::create('Servidor', function (Blueprint $table) {

		$table->increments('id');
		$table->string('serverid',50)->unique();
        $table->string('ip', 12);
        $table->integer('port', 5);
		$table->datetime('fechaAlta')->comment('Fecha de Creación');
		$table->integer('idUniversidad')->unsigned();
        $table->foreign('idUniversidad')->references('id')->on('Universidad')->onUpdate('CASCADE')->onDelete('CASCADE');
        });

        


    }

    public function down()
    {
        Schema::dropIfExists('Servidor');
    }
}