<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateCamaraTable extends Migration
{
    public function up()
    {
        Schema::create('Camara', function (Blueprint $table) {

		$table->increments('id');
		$table->string('cameraid',50)->unique();
        $table->string('socketKey', 20)->unique();
        $table->string('type', 4)->comment('IN/OUT/BOTH');
        $table->text('protocol')->comment('TCP, HTTP, WebSocket, TCPSJMP', 'WebSocketSJMP');
		$table->integer('idServidor',)->unsigned();
		$table->integer('idAparcamiento',)->unsigned();
        $table->foreign('idAparcamiento')->references('id')->on('Aparcamiento')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->foreign('idServidor')->references('id')->on('Servidor')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();    
        });
    }

    public function down()
    {
        Schema::dropIfExists('Camara');
    }
}