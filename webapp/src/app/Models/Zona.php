<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\TipoPlaza;
use App\Models\Aparcamiento;

class Zona extends Model
{
    protected $table = "Zona";
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
        'letra',
        'plazas',
        'idTipoPlaza',
        'idAparcamiento'
    ];
    protected $casts = [
        'plazas' => 'integer',
        'idTipoPlaza' => 'integer',
        'idAparcamiento' => 'integer'
    ];

    public function tipoplaza()
    {
        return $this->belongsTo(TipoPlaza::class, 'id', 'idTipoPlaza');
    }

    public function aparcamiento()
    {
        return $this->belongsTo(Aparcamiento::class, 'id', 'idAparcamiento');
    }
}
