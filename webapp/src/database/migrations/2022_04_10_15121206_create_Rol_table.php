<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateRolTable extends Migration
{
    public function up()
    {
        Schema::create('Rol', function (Blueprint $table) {

		$table->increments('id');
		$table->string('nombre', 30)->unique();
		$table->boolean('incidencias');
		$table->boolean('digitalTwin');
        $table->boolean('userDashboard');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('Rol');
    }
}