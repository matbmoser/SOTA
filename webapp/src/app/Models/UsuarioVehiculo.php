<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Vehiculo;
use App\Models\Usuario;

class UsuarioVehiculo extends Model
{
    protected $table = "UsuarioVehiculo";
    public $timestamps = true;
    public $incrementing = false;
    protected $primaryKey = ['idUsuario', 'idVehiculo'];

    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<string>
     */
    protected $fillable = [
        'idUsuario',
        'idVehiculo',
        'aparcado',
        'numAparcamientos',
        'fechaUltimoAparcamiento'
    ];
    protected $casts = [
        'aparcado' => 'boolean',
        'numAparcamientos' => 'integer',
        'fechaUltimoAparcamiento' => 'datetime',
        'idUsuario' => 'integer',
        'idVehiculo' => 'integer'
    ];

    public function usuario()
    {
        return $this->belongsTo(Usuario::class, 'id', 'idUsuario');
    }

    public function vehiculo()
    {
        return $this->belongsTo(Vehiculo::class, 'id', 'idVehiculo');
    }
}