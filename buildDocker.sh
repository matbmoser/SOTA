## Script para abrir el dockerCompose y configurar la base de datos
docker network create appNet
docker-compose up -d --build 

## Migraciones y configuraciones posteriores
docker exec -it php-webapp chmod -R 777 storage
sleep 15
docker exec -it php-webapp npm run migrate 