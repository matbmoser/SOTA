<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\User;
use App\Models\Plaza;
use App\Models\Vehiculo;

class Incidencia extends Model
{
    protected $table = "Incidencia";
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
        'gravedad',
        'titulo',
        'descripcion',
        'fechaApartura',
        'fechaCierre',
        'resuelta',
        'notaCierre',
        'nombreArchivoFoto',
        'idAprobador',
        'idPlaza',
        'idVehiculo',
    ];
    protected $casts = [
        'fechaApartura' => 'datetime',
        'fechaCierre' => 'datetime',
        'resuelta' => 'boolean',
        'idAprobador' => 'integer',
        'idPlaza' => 'integer',
        'idVehiculo' => 'integer'
    ];

    public function aprobador()
    {
        return $this->belongsTo(User::class, 'id', 'idAprobador');
    }

    public function plaza()
    {
        return $this->belongsTo(Plaza::class, 'id', 'idPlaza');
    }

    public function vehiculo()
    {
        return $this->belongsTo(Vehiculo::class, 'id', 'idVehiculo');
    }
}
