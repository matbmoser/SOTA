<?php
namespace database\factories;
 
use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;;
 
class UniversidadFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'nombre' => "Universidad Francisco de Vitoria",
            'email' => "gerencia@ufv.es",
            'telefono' => "+34 913 51 03 03",
            'sigla' => 'UFV',
            'direccion' => 'Carretera Pozuelo a, Av de Majadahonda, Km 1.800'
            'codigoPostal' => '28223'
            'ciudad' => 'Pozuelo de Alarcón'
            'comunidad' => 'Comunidad de Madrid'
            'pais' => 'España'
        ];
    }
}