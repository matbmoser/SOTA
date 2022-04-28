## STARTS THE DESTINATION CAMERAS

. startTest.sh.import


logInfo "Starting Destination Cameras..."

## DESTINATION CAMERAS
py $FILEPATH -n $DCTCP1 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$DCTCP1.log" \
2> "${CLIENTERRFILE}$DCTCP1.log" & logMessage "Destination Camera [$DCTCP1] Open on PID $!"

py $FILEPATH -n $DCTCP2 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$DCTCP2.log" \
2> "${CLIENTERRFILE}$DCTCP2.log" & logMessage "Destination Camera [$DCTCP2] Open on PID $!"

py $FILEPATH -n $DCTCP3 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$DCTCP3.log" \
2> "${CLIENTERRFILE}$DCTCP3.log" & logMessage "Destination Camera [$DCTCP3] Open on PID $!" 

