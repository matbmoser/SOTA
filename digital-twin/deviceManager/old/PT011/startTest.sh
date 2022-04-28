### [PT011] PERFORMANCE TEST
# Send Messages from TCP Camera to another TCP Camera
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
# TO REVIEW !!
./startDC.sh  
wait -n
./startOC.sh 
wait

sleep 600
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
sleep 2
# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe

calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP1}.log" $CLIENTPERFORMANCEFILE

calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP1}.log" $CLIENTPERFORMANCEFILE
