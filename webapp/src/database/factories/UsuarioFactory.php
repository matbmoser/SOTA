<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;
use App\Models\Usuario;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Usuario>
 */
class UsuarioFactory extends Factory
{
    protected $model = Usuario::class;
 /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'nombre' => "Mathias",
            'username' => "matbmoser",
            'apellido1' => "Brunkow",
            'apellido2' => "Moser",
            'documento' => "07164545J",
            'telefono' => "647637778",
            'email' => "mathiasmoser@outlook.com",
            'password' =>  hash("sha-512","123456789"),
            'fechaNacimiento' => "26/09/2000",
            'codigoPostal' => "28223",
            'ciudad' => "Pozuelo de Alarcón",
            'comunidad' => "Comunidad de Madrid",
            'pais' => "España",
        ];
    }
}
