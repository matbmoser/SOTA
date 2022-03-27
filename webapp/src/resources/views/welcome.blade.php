<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Laravel</title>
        <link href="https://unpkg.com/primevue/resources/themes/lara-light-indigo/theme.css" rel="stylesheet">
        <link href="https://unpkg.com/primevue/resources/primevue.min.css" rel="stylesheet">
        <link href="https://unpkg.com/primeicons/primeicons.css" rel="stylesheet">

        <script src="https://unpkg.com/vue@next"></script>
        <script src="https://unpkg.com/primevue/core/core.min.js"></script>
        <script src="https://unpkg.com/primevue/slider/slider.min.js"></script>
        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    </head>
    <body>
        <div id="app"></div>
    </body>
    <script src="{{ asset('js/app.js') }}"></script>
</html>