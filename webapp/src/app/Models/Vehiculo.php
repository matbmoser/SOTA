<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\TipoVehiculo;

class Vehiculo extends Model
{
    protected $table = "Vehiculo";
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
        'matricula',
        'idTipoVehiculo',
        'idUsuario'
    ];
    protected $casts = [
        'idTipoVehiculo' => 'integer',
        'idUsuario' => 'integer'
    ];

    public function tipovehiculo()
    {
        return $this->belongsTo(TipoVehiculo::class, 'id', 'idTipoVehiculo');
    }
    public function usuario()
    {
        return $this->belongsTo(User::class, 'id', 'idUsuario');
    }
}
