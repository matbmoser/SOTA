## Import configurations of the cameras
. startTest.sh.import

logInfo "Starting Cameras..."

# START THE ORIGIN CAMERAS
py $FILEPATH -nM $NMSGS -m "$TESTPAYLOADTEXT" -n $OCTCP1 $SERVERPARAMS \
> "${CLIENTRESULTFILE}${OCTCP1}.log" \
2> "${CLIENTERRFILE}${OCTCP1}.log" & echo "Origin Camera [$OCTCP1] Open on PID $!" \
