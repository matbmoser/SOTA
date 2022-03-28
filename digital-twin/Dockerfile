FROM php:apache

RUN apt update \
    && apt install -y \
    g++ \
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
    pdo_mysql


WORKDIR /var/www/digital-twin
RUN chmod 777 ./


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./deviceManager/ .
RUN chmod 777 ./*
RUN chmod 777 /usr/src/app/ServerManager.py
RUN chgrp www-data /usr/src/app/ServerManager.py