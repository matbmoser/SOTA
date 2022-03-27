## STARTS THE DESTINATION CAMERAS

. startTest.sh.import


logInfo "Starting Destination Cameras..."

## DESTINATION CAMERAS
py $FILEPATH -n $DCTCP $SERVERPARAMS -nC $NCLIENTS -t "RECEIVE" -oC $NCLIENTS -oM $NMSGS \
> "${CLIENTRESULTFILE}$DCTCP.log" \
2> "${CLIENTERRFILE}$DCTCP.log" & logMessage "Destination Camera [$DCTCP1] Open on PID $!"
