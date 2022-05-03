<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateIncidenciaTable extends Migration
{
    public function up()
    {
        Schema::create('Incidencia', function (Blueprint $table) {

		$table->increments('id');
		$table->integer('gravedad',)->comment('0-5');
		$table->string('titulo');
		$table->text('descripcion');
		$table->datetime('fechaCierre')->nullable();
		$table->boolean('resuelta')->default(0);
		$table->text('notaCierre')->nullable();
		$table->text('nombreArchivoFoto')->nullable();
		$table->integer('idAprobador',)->unsigned()->nullable();
		$table->string('tokenPlaza',128)->unique()->comment('Unique sha512 hash');
		$table->foreign('idAprobador')->references('id')->on('users')->onUpdate('CASCADE')->onDelete('CASCADE'); 
		$table->foreign('tokenPlaza')->references('token')->on('Plaza')->onUpdate('CASCADE');
        $table->timestamps();    
		});
    }

    public function down()
    {
        Schema::dropIfExists('Incidencia');
    }
}