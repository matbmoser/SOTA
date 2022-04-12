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
            'nombre' => $this->faker->firstName(),
            'username' =>$this->faker->userName(),
            'apellido1' => $this->faker->lastName(),
            'apellido2' => $this->faker->lastName(),
            'documento' => Str::random(9),
            'telefono' => $this->faker->phone(),
            'email' => $this->faker->unique()->safeEmail(),
            'password' =>  hash('sha512',$faker->word()),
            'fechaNacimiento' => $this->faker->date()
            'codigoPostal' => random_int(1,5),
            'ciudad' => $this->faker->address(),
            'comunidad' => $this->faker->text(15),
            'pais' => $this->faker->text(12),
        ];
    }
}
