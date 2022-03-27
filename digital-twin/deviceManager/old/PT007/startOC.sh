## STARTS THE DESTINATION CAMERAS

. startTest.sh.import

cd ../../

path=$(pwd | awk '{ print substr ($0, 3 ) }')


logInfo "Starting Origin WS Cameras..."


## DESTINATION CAMERAS

"$FIREFOXPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS3}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCTCP2}|${DCTCP3}|${DCTCP1}&count=${NMSGS}" & 

"$EDGEPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS2}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCTCP3}|${DCTCP2}|${DCTCP1}&count=${NMSGS}" &

"$CHROMEPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS1}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCTCP1}|${DCTCP2}|${DCTCP3}&count=${NMSGS}"&

sleep 40

