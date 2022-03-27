### [PT012] PERFORMANCE TEST
# Send Messages from 3 TCP cameras to 3 TCP cameras
# by: Mathias Brunkow Moser
# © CGI - ALL RIGHTS RESERVED
###
#!/usr/bin/env bash
set -x

global0="${0}"
export global0

. ${global0}.import

echo "Opening Test Server!"
startTestServer $DEFAULTRESULTSFILE $DEFAULTERRORFILE $TESTOBJECTIVE $NCLIENTS $NMSGS &
wait -n

# START FIRST THE DESTINATION CAMERAS THAT WILL RECEIVE THE MESSAGE
# TO REVIEW !!
./startDC.sh  
wait -n
./startOC.sh 
wait

sleep $WAITINGTIME
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe
sleep 2

calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP}.log" $CLIENTPERFORMANCEFILE
calcTestCameraPerformance "${CLIENTRESULTFILE}${DCTCP}.log" $CLIENTPERFORMANCEFILE
