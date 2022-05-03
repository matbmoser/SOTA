<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class TipoPlaza extends Model
{
    protected $table = "TipoPlaza";
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
        'tipo',
        'ancho',
        'largo',
    ];
    protected $casts = [
        'ancho' => 'integer',
        'largo' => 'integer'
    ];
}
