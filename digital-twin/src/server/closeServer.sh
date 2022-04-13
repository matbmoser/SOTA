#!/usr/bin/env bash
. ./functions.import
echo "Trying to close Server..."
if [ -z {$1} ];
then
    closeDefaultServer server.log 
else
    closeDefaultServer server.log ${1}
fi
    

