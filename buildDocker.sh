echo "[INFO] Starting build..." 
echo "[INFO] Checking for docker daemon and opened containers..." 
if (! docker stats --no-stream );
    then
        printf "\n******* [BUILD FAILED] ******************\n"
        printf "[ERROR] Your Docker Daemon is not up, please open your docker app!"
        printf "\n*****************************************"
        exit -1
fi
printf "\n[INFO] Docker Daemon is up... "
printf "\n[STATUS] Trying to create appNet Network...\n"
## Configure the container internal net
docker network create appNet
printf "\n[STATUS] Building Docker Compose Containers...\n"
## Configure the containers with docker compose.
docker-compose up -d --build 

printf "\n[INFO] Setting up containers settings..."
## Configure permits
docker exec -it php-webapp chmod -R 777 storage

printf "\n\n[STATUS] Installing PHP Packets...\n"
## Install all the PHP Laravel packets
docker exec -it php-webapp composer install
printf "\n[STATUS] Finishing Install of PHP Packets..."

printf "\n[INFO] Checking for npm updates...\n"
docker exec -it php-webapp npm install -g npm@latest --loglevel error
printf "\n[INFO] Finishing checking or updating npm...\n"

printf "\n[STATUS] Installing JS Packets...\n"
## Install all JS Packets 
docker exec -it php-webapp npm install --force --loglevel silent
printf "[STATUS] Finishing Install of JS Packets...\n"

printf "\n[INFO] Setting up database... [Waiting 15 seconds...]"
sleep 15

printf "\n[STATUS] Executing Database Migrations..."
## Execute the migration of the database
docker exec -it php-webapp npm run migrate 
printf "\n[STATUS] Finishing Database Migrations..."

printf "\n[INFO] Build Finished..."
