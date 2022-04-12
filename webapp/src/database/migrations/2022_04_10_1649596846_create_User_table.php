<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUserTable extends Migration
{
    public function up()
    {	
        Schema::create('User', function (Blueprint $table) {

		$table->increments('id');
		$table->text('name');
		$table->string('email', 320)->unique();
		$table->string('password',128)->comment('Encriptado con SHA512');;
		$table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('User');
    }
}