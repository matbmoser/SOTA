<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Notifications\Notifiable;
use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Foundation\Auth\User as Authenticatable;
use App\Models\Rol;
use Tymon\JWTAuth\Contracts\JWTSubject;

class User extends Authenticatable implements JWTSubject 
{
    use Notifiable;
    
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
        'token',
        'idRol'
    ];
    protected $casts = [
        'fechaUltimaConexion' => 'datetime',
        'correoConfirmadoEn' => 'datetime',
        'fechaNacimiento' => 'date',
        'email_verified_at' => 'datetime',
        'idRol' => 'integer',
        
    ];
    
    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];
    /**
     * Get the rol record associated with the user.
     */
    public function rol()
    {
        return $this->belongsTo(Rol::class, 'id', 'idRol');
    }
    public function getJWTIdentifier()
    {
        return $this->getKey();
    }
    
    public function getJWTCustomClaims()
    {
        return [];
    }
}