## STARTS THE ORIGIN CAMERAS

. startTest.sh.import

logInfo "Starting Origin Cameras..."

# ORIGIN CAMERAS
py $FILEPATH -f $PAYLOADFILE -n $OCTCP1 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$OCTCP1.log" \
2> "${CLIENTERRFILE}$OCTCP1.log" & logMessage "Origin Camera [$OCTCP1] Open on PID $!" \

py $FILEPATH -f $PAYLOADFILE -n $OCTCP2 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$OCTCP2.log" \
2> "${CLIENTERRFILE}$OCTCP2.log" & logMessage "Origin Camera [$OCTCP2] Open on PID $!" \

py $FILEPATH -f $PAYLOADFILE -n $OCTCP3 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$OCTCP3.log" \
2> "${CLIENTERRFILE}$OCTCP3.log" & logMessage "Origin Camera [$OCTCP3] Open on PID $!"

py $FILEPATH -f $PAYLOADFILE -n $OCTCP4 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$OCTCP4.log" \
2> "${CLIENTERRFILE}$OCTCP4.log" & logMessage "Origin Camera [$OCTCP4] Open on PID $!" \

