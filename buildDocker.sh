## Script para abrir el dockerCompose y configurar la base de datos
docker network create appNet
docker-compose up -d --build 

## Migraciones y configuraciones posteriores
docker exec -it php-webapp chmod -R 777 storage
sleep 15

## Install all the PHP Laravel packets
docker exec -it php-webapp composer install
## Install all JS Packets 
docker exec -it php-webapp npm install --force

## Execute the migration of the database
docker exec -it php-webapp npm run migrate 
