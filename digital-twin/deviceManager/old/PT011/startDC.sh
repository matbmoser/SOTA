## STARTS THE DESTINATION CAMERAS

. startTest.sh.import


logInfo "Starting Destination Cameras..."

## DESTINATION CAMERAS
py $FILEPATH -n $DCTCP1 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$DCTCP1.log" \
2> "${CLIENTERRFILE}$DCTCP1.log" & logMessage "Destination Camera [$DCTCP1] Open on PID $!"

