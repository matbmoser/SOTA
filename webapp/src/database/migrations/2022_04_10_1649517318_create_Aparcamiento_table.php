<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateAparcamientoTable extends Migration
{
    public function up()
    {
        Schema::create('Aparcamiento', function (Blueprint $table) {

		$table->increments('id');
        $table->string("letra", 2)->unique();
		$table->text('color');
		$table->text('localizacion');
		$table->integer('idUniversidad',)->unsigned();
        $table->foreign('idUniversidad')->references('id')->on('Universidad')->onUpdate('CASCADE')->onDelete('CASCADE');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('Aparcamiento');
    }
}