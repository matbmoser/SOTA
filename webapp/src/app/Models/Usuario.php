<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Rol;

class Usuario extends Model
{
    use HasFactory;

    protected $table = "Usuario";
    
    /**
     * Indicates if the model's ID is auto-incrementing.
     *
     * @var bool
     */
    public $incrementing = true;
    
    /**
     * The primary key associated with the table.
     *
     * @var string
     */
    protected $primaryKey = 'id';

    /**
     * Indicates if the model should be timestamped.
     *
     * @var bool
     */
    public $timestamps = true;

    /**
     * The attributes that are mass assignable.
     *
     * @var array<string>
     */
    protected $fillable = [
        'nombre',
        'username',
        'apellido1',
        'apellido2',
        'documento',
        'telefono',
        'fechaNacimiento',
        'email',
        'password',
        'idRol'
    ];
    protected $guarded = array('password');
    /**
     * The attributes that should be cast.
     *
     * @var array
     */
    protected $casts = [
        'fechaUltimaConexion' => 'datetime',
        'correoConfirmadoEn' => 'datetime',
        'fechaNacimiento' => 'date',
        'correoConfirmado' => 'boolean',
        'idRol' => 'integer',
    ];
    /**
     * Get the phone record associated with the user.
     */
    public function rol()
    {
        return $this->belongsTo(Rol::class, 'id', 'idRol');
    }
}