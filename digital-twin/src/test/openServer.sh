#!/usr/bin/env bash
. ./functions.import
SERVERFILENAME="ServerManager.py"
RES=$(getPythonFilePID $SERVERFILENAME)
echo $RES
echo "Starting Server..."
mkdir -p ./log 
openDefaultServer log/server.log  
ps -ef
