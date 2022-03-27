## STARTS THE DESTINATION CAMERAS

. startTest.sh.import

cd ../../

path=$(pwd | awk '{ print substr ($0, 3 ) }')


logInfo "Starting Origin WS Cameras..."


## DESTINATION CAMERAS

"$FIREFOXPATH" "file:///C:${path}/${FILENAME}?cameraid=${OCWS3}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}&text=${TESTPAYLOADTEXT}&cameras=${DCTCP1}&count=${NMSGS}" 


