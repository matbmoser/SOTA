<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Universidad;

class Aparcamiento extends Model
{
    protected $table = "Aparcamiento";
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
        'color',
        'localización',
        'idUniversidad',
    ];
    protected $casts = [
        'idUniversidad' => 'integer'
    ];

    public function universidad()
    {
        return $this->belongsTo(Universidad::class, 'id', 'idUniversidad');
    }
}
