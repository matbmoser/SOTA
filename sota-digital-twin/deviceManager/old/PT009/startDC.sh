## STARTS THE DESTINATION CAMERAS

. startTest.sh.import

cd ../../

path=$(pwd | awk '{ print substr ($0, 3 ) }')


logInfo "Starting Origin WS Cameras..."


## DESTINATION CAMERAS
"$CHROMEPATH" "file:///C:${path}/${FILENAME}?cameraid=${DCWS1}&ip=${DEFAULTSERVERIP}&port=${DEFAULTSERVERPORT}"

