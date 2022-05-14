<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" type="image/x-icon" href="media/favicon.ico">
          <!-- CSRF Token -->
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <title>UFV MyParking</title>

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,400;0,500;0,700;0,800;1,300;1,400;1,500;1,600;1,700;1,800&display=swap" rel="stylesheet">
          <!-- Styles -->
        <link href="{{ asset('css/app.css') }}" rel="stylesheet">
    </head>
    <body>
        <div id="app" style="min-height:100%!important"></div>
    </body>
    <script src="{{ asset('js/app.js') }}"></script>
    <style>
      html, body, #app{
        overflow: auto;
        height: 100%!important;
    }

    </style>
</html>