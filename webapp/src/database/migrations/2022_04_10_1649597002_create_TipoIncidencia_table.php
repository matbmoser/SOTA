<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateTipoIncidenciaTable extends Migration
{
    public function up()
    {
        Schema::create('TipoIncidencia', function (Blueprint $table) {

		$table->increments('id');
		$table->text('nombre');
        $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('TipoIncidencia');
    }
}