<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        $this->call([
            RolSeeder::class,
            UserSeeder::class,
            UniversidadSeeder::class,
            TipoVehiculoSeeder::class,
            AparcamientoSeeder::class,
            TipoPlazaSeeder::class,
            ZonaSeeder::class,
            TipoVehiculoTipoPlazaSeeder::class,
            VehiculoSeeder::class,
            UserVehiculoSeeder::class
        ]);
  
    }
}
