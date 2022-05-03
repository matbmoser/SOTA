#!/usr/bin/env bash
. ./functions.import
SERVERPORT=${1}


if [ -z "$SERVERPORT" ];
then
    echo "[ERROR] Please indicate the Server PORT: get.sh <PORT>"
    exit -1
fi

getServerByPort $SERVERPORT

