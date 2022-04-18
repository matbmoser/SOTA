docker network create appNet
docker-compose up -d --build
docker exec -it php-webapp npm run migrate