## Import configurations of the cameras
. startTest.sh.import

logInfo "Starting Cameras..."

# START THE ORIGIN CAMERAS
cat $PAYLOADFILE | py $FILEPATH -n $OCTCP1 $SERVERPARAMS \
> "${CLIENTRESULTFILE}${OCTCP1}.log" \
2> "${CLIENTERRFILE}${OCTCP1}.log" & echo "Origin Camera [$OCTCP1] Open on PID $!" \
& cat $PAYLOADFILE | py $FILEPATH -n $OCTCP2 $SERVERPARAMS \
> "${CLIENTRESULTFILE}${OCTCP2}.log" \
2> "${CLIENTERRFILE}${OCTCP2}.log" & echo "Origin Camera [$OCTCP2] Open on PID $!" \
& cat $PAYLOADFILE | py $FILEPATH -n $OCTCP3 $SERVERPARAMS \
> "${CLIENTRESULTFILE}${OCTCP3}.log" \
2> "${CLIENTERRFILE}${OCTCP3}.log" & echo "Origin Camera [$OCTCP3] Open on PID $!" \
& cat $PAYLOADFILE | py $FILEPATH -n $OCTCP4 $SERVERPARAMS \
> "${CLIENTRESULTFILE}${OCTCP4}.log" \
2> "${CLIENTERRFILE}${OCTCP4}.log" & echo "Origin Camera [$OCTCP4] Open on PID $!"

wait -n