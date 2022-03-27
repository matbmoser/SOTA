### [PT008] PERFORMANCE TEST
# Send messages from TCP to WebSocket
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
wait -n
./startOC.sh 

wait -n


sleep 25
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
wait
# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe

calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP1}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP2}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP3}.log" $CLIENTPERFORMANCEFILE
