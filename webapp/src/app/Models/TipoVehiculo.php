<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TipoVehiculo extends Model
{
    protected $table = "TipoVehiculo";
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
        'segmento',
        'clasificacion',
        'ancho',
        'largo',
        'alto'
    ];
    protected $casts = [
        'ancho' => 'float',
        'largo' => 'float',
        'alto' => 'float'
    ];
}
