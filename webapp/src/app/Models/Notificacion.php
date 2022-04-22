<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Usuario;

class Notificacion extends Model
{   
    protected $table = "Notificacion";
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
        'titulo',
        'descripcion',
        'boton',
        'tituloBoton',
        'enlaceBoton',
        'idUsuario'
    ];
    protected $casts = [
        'boton' => 'boolean'
        'idUsuario' => 'integer'
    ];
    
    public function usuario()
    {
        return $this->belongsTo(Usuario::class, 'id', 'idUsuario');
    }
}
