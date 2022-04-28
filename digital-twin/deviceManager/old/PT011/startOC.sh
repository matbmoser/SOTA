## STARTS THE ORIGIN CAMERAS

. startTest.sh.import

logInfo "Starting Origin Cameras..."

# ORIGIN CAMERAS
py $FILEPATH -nM $NMSGS -c "$DCLIENTS" -m "$TESTPAYLOADTEXT" -n $OCTCP1 $SERVERPARAMS \
> "${CLIENTRESULTFILE}$OCTCP1.log" \
2> "${CLIENTERRFILE}$OCTCP1.log" & logMessage "Origin Camera [$OCTCP1] Open on PID $!" \
