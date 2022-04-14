#!/usr/bin/env bash
. ./functions.import
echo "Trying to close Server..."
if [ -z {$1} ];
then
    closeServer 
else
    closeServer ${1}
fi
    

