<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateUsersTable extends Migration
{
    public function up()
    {	
        Schema::create('users', function (Blueprint $table) {

		$table->increments('id');
		$table->text('nombre');
		$table->text('apellido1');
		$table->text('apellido2')->nullable();
		$table->string('username',50)->unique();
		$table->text('documento');
		$table->text('telefono');
		$table->string('email', 320)->unique();
		$table->string('password',128)->comment('Encriptado con SHA512');
		$table->string('token',64)->comment('Hash SHA256');
		$table->date('fechaNacimiento');
		$table->boolean('correoConfirmado');
		$table->datetime('correoConfirmadoEn')->nullable();
		$table->datetime('fechaUltimaConexion');
		$table->integer('idRol',)->unsigned();
		$table->foreign('idRol')->references('id')->on('Rol')->onUpdate('CASCADE')->onDelete('CASCADE');
		$table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('users');
    }
}