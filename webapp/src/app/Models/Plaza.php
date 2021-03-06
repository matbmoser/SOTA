<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\User;
use App\Models\Zona;
use App\Models\Vehiculo;

class Plaza extends Model
{
    protected $table = "Plaza";
    public $timestamps = true;
    public $incrementing = false;
    protected $primaryKey = ['id','idZona', 'token'];

    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<string>
     */
    protected $fillable = [
        'token',
        'fechaEntrada',
        'fechaSalida',
        'valido',
        'incidencia',
        'idZona',
        'idUsuario',
        'idVehiculo'
    ];
    protected $casts = [
        'fechaEntrada' => 'datetime',
        'fechaCierre' => 'datetime',
        'valido' => 'boolean',
        'incidencia' => 'boolean',
        'idUsuario' => 'integer',
        'idZona' => 'integer',
        'idVehiculo' => 'integer'
    ];

    public function usuario()
    {
        return $this->belongsTo(User::class, 'id', 'idUsuario');
    }

    public function zona()
    {
        return $this->belongsTo(Zona::class, 'id', 'idZona');
    }

    public function vehiculo()
    {
        return $this->belongsTo(Vehiculo::class, 'id', 'idVehiculo');
    }
}
