<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Rol extends Model
{   
    protected $table = "Rol";
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
        'nombre',
        'incidencias',
        'digitalTwin'
    ];
    protected $casts = [
        'incidencias' => 'boolean',
        'digitalTwin' => 'boolean'
    ];
}
