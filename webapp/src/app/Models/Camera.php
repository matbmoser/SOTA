<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Aparcamiento;
use App\Models\Servidor;

class Camera extends Model
{
    protected $table = "Camera";
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
        'camaraid',
        'socketKey',
        'type',
        'protocol',
        'idServidor',
        'idAparcamiento'
    ];
    protected $casts = [
        'idServidor' => 'integer',
        'idAparcamiento' => 'integer'
    ];

    public function aparcamiento()
    {
        return $this->belongsTo(Aparcamiento::class, 'id', 'idAparcamiento');
    }

    public function servidor()
    {
        return $this->belongsTo(Servidor::class, 'id', 'idServidor');
    }
}
