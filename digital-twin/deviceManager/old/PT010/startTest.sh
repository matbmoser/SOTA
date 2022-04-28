### [PT010] PERFORMANCE TEST
# Send messages from 1 WebSocket to 1 TCP
# by: Mathias Brunkow Moser
# © CGI - ALL RIGHTS RESERVED
###
#!/usr/bin/env bash
set -x

global0="${0}"
export global0

. ${global0}.import

echo "Opening Test Server!"
startTestServer $DEFAULTRESULTSFILE $DEFAULTERRORFILE &
wait -n

# START FIRST THE DESTINATION CAMERAS THAT WILL RECEIVE THE MESSAGE
./startDC.sh  

./startOC.sh 

wait

sleep 20
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
wait
# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe

calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP1}.log" $CLIENTPERFORMANCEFILE