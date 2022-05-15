echo "[INFO] Starting to Open Camera..." 
echo "[INFO] Checking for docker daemon and opened containers..." 
if (! docker stats --no-stream );
    then
        printf "\n******* [BUILD FAILED] ******************\n"
        printf "[ERROR] Your Docker Daemon is not up, please open your docker app!"
        printf "\n*****************************************"
        exit -1
fi
printf "\n\n[SUCCESS] Docker Daemon is up!\n\n"

printf "\n\n[INFO] Opening Camera Manager...\n" 
## Open the camara simulator
docker exec -it digital-twin python3 CameraManager.py -cmd
printf "\n[INFO] Closing Camera Manager..." 