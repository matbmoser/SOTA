<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\TipoVehiculo;
use App\Models\TipoPlaza;


class TipoVehiculoTipoPlaza extends Model
{
    protected $table = "TipoVehiculoTipoPlaza";
    public $timestamps = true;
    public $incrementing = false;
    protected $primaryKey = ['idTipoVehiculo', 'idTipoPlaza'];

    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<string>
     */
    protected $fillable = [
        'idTipoVehiculo',
        'idTipoPlaza',
    ];
    protected $casts = [
        'idTipoVehiculo' => 'integer',
        'idTipoVehiculo' => 'integer'
    ];

    public function tipovehiculo()
    {
        return $this->belongsTo(TipoVehiculo::class, 'id', 'idTipoVehiculo');
    }

    public function tipoplaza()
    {
        return $this->belongsTo(TipoPlaza::class, 'id', 'idTipoPlaza');
    }
}