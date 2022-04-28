<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Universidad extends Model
{
    protected $table = "Universidad";
    public $timestamps = true;
    public $incrementing = true;
    protected $primaryKey = 'id';

    use HasFactory;

        /**
     * The attributes that are mass assignable.
     *
     * @var array<string>
     */
    protected $fillable = [
        'nombre',
        'email',
        'telefono',
        'sigla',
        'direccion',
        'codigoPostal',
        'ciudad',
        'comunidad',
        'pais'

    ];
    protected $casts = [
        'codigoPostal' => 'integer'
    ];
}
