FROM php:apache

RUN apt update \
    && apt install -y \
    g++ \
    telnet \
    net-tools \
    nmap \
    openssl \
    git \
    iputils-ping \
    libicu-dev \
    libpq-dev \
    libzip-dev \
    zip \
    zlib1g-dev \
    gcc \
    python3-dev \
    python3 \
    pip \
    && docker-php-ext-install \
    mysqli \
    pdo \
    pdo_mysql \
    && docker-php-ext-enable \
    pdo_mysql\
    mysqli


## Configuración de Permisos para el Digital Twin
WORKDIR /var/www/digital-twin
RUN usermod -a -G www-data root
RUN chmod +777 ./
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

## Instalamos las librerias necesarias
COPY ./python/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./deviceManager/ .

## Configuramos los permisos de www-data
RUN chown -R www-data:www-data /var/www
RUN chown -R www-data:www-data /usr/src/app
RUN chgrp -R www-data /var/www
RUN chgrp -R www-data /usr/src/app
