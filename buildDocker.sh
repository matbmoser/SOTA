docker network create appNet
docker-compose up -d --build 
docker exec -it php-webapp chmod -R 777 storage
sleep 15
docker exec -it php-webapp npm run migrate 