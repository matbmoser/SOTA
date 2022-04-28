FROM php:apache

RUN apt update \
    && apt install -y \
    g++ \
    telnet \
    net-tools \
    nmap \
    openssl \
    iputils-ping \
    git \
    libicu-dev \
    libpq-dev \
    libzip-dev \
    zip \
    zlib1g-dev \
    && docker-php-ext-install \
    mysqli \
    pdo \
    pdo_mysql \
    && docker-php-ext-enable \
    pdo_mysql

WORKDIR /var/www/webapp

## Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

## Install Node JS and NPM
ENV NODE_VERSION=16.14.2 
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version

RUN npm install -g npm@latest

