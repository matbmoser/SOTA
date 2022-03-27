## STARTS THE DESTINATION CAMERAS

. startTest.sh.import

cd ../../

path=$(pwd | awk '{ print substr ($0, 3 ) }')


logInfo "Starting Origin WS Cameras..."


## DESTINATION CAMERAS
"$CHROMEPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS1}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCWS1}|${DCWS2}|${DCWS3}|${DCWS4}&count=${NMSGS}" &

"$EDGEPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS2}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCWS1}|${DCWS2}|${DCWS3}|${DCWS4}&count=${NMSGS}" &

"$EDGEPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS3}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCWS1}|${DCWS2}|${DCWS3}|${DCWS4}&count=${NMSGS}" &

wait -n

"$FIREFOXPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS4}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras${DCWS1}|${DCWS2}|${DCWS3}|${DCWS4}&count=${NMSGS}" &

sleep 10 &

wait