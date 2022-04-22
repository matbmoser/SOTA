<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Usuario;
use App\Models\Ticket;
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
        'idTicket',
        'idVehiculo',
    ];
    protected $casts = [
        'fechaApartura' => 'datetime',
        'fechaCierre' => 'datetime',
        'resuelta' => 'boolean',
        'idAprobador' => 'integer',
        'idTicket' => 'integer',
        'idVehiculo' => 'integer'
    ];

    public function aprobador()
    {
        return $this->belongsTo(Usuario::class, 'id', 'idAprobador');
    }

    public function ticket()
    {
        return $this->belongsTo(Ticket::class, 'id', 'idTicket');
    }

    public function vehiculo()
    {
        return $this->belongsTo(Vehiculo::class, 'id', 'idVehiculo');
    }
}
