<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCameraTable extends Migration
{
    public function up()
    {
        Schema::create('Camera', function (Blueprint $table) {

		$table->increments('id');
		$table->string('camaraid',50)->unique();
        $table->string('ip', 12);
        $table->integer('port', 5);
		$table->datetime('fechaAlta');
		$table->integer('idServidor',)->unsigned();
		$table->integer('idAparcamiento',)->unsigned();
        $table->foreign('idAparcamiento')->references('id')->on('Aparcamiento')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->foreign('idServidor')->references('id')->on('Servidor')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();    
        });
    }

    public function down()
    {
        Schema::dropIfExists('Camera');
    }
}