FROM httpd:latest

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
            pip


RUN mkdir -p /usr/src/deviceManager
WORKDIR /usr/src/deviceManager
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /var/www/sota-digital-twin