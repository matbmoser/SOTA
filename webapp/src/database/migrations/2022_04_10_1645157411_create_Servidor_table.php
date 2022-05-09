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
        $table->string('socketKey', 20)->unique();
		$table->integer('idUniversidad')->unsigned();
        $table->foreign('idUniversidad')->references('id')->on('Universidad')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('Servidor');
    }
}