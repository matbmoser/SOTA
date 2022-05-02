<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;
use App\Http\Controllers\RolController;
use App\Http\Controllers\ZonaController;
use App\Http\Controllers\PlazaController;
/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::prefix('auth')->group(function () {
    Route::post('register', 'App\Http\Controllers\AuthController@register');
    Route::post('login', 'App\Http\Controllers\AuthController@login');
    Route::get('refresh', 'App\Http\Controllers\AuthController@refresh');
    Route::get('check', 'App\Http\Controllers\AuthController@check');
    Route::group(['middleware' => 'auth:api'], function(){
        Route::get('user', 'App\Http\Controllers\AuthController@user');
        Route::post('logout', 'App\Http\Controllers\AuthController@logout');
    });
});

Route::group(['middleware' => 'auth:api'], function(){
    // Users
    Route::get('users', 'App\Http\Controllers\UserController@index')->middleware('isAdmin');
    Route::get('user/{id}', 'App\Http\Controllers\UserController@show')->middleware('isAdminOrSelf');
    
    // Roles
    Route::get('roles', 'App\Http\Controllers\RolController@index')->middleware('isAdmin');
    Route::get('rol/{id}', 'App\Http\Controllers\RolController@show')->middleware('isAdminOrSelfRol');

    // Zonas
    Route::get('zonas', 'App\Http\Controllers\ZonaController@index');
    Route::get('zona/{id}', 'App\Http\Controllers\ZonaController@show');

    // Plazas
    Route::get('plazas', 'App\Http\Controllers\PlazaController@index');
    Route::get('plaza/{id}', 'App\Http\Controllers\PlazaController@show');
    Route::get('plazas/validas', 'App\Http\Controllers\PlazaController@validas');
    Route::get('plazas/validas/zonas', 'App\Http\Controllers\PlazaController@validasZona');
});