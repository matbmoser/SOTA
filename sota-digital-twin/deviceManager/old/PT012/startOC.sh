## STARTS THE ORIGIN CAMERAS

. startTest.sh.import

logInfo "Starting Origin Cameras..."

# ORIGIN CAMERAS
py $FILEPATH -nM $NMSGS -m "$TESTPAYLOADTEXT" -n $OCTCP $SERVERPARAMS -dC $DCTCP -nC $NCLIENTS -t "SEND"\
> "${CLIENTRESULTFILE}$OCTCP.log" \
2> "${CLIENTERRFILE}$OCTCP.log" & logMessage "Origin Camera [$OCTCP1] Open on PID $!"
