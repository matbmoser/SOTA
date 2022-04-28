### [PT002] PERFORMANCE TEST
# Send messages defined in a file from 4 TCP cameras to other 4 TCP cameras 
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

sleep 2
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE

sleep 2
# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe

calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP1}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP2}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP3}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP4}.log" $CLIENTPERFORMANCEFILE

calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP1}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP2}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP3}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP4}.log" $CLIENTPERFORMANCEFILE