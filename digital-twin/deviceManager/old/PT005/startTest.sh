### [PT005] PERFORMANCE TEST
# Send 80 messages from one TCP Camera to the server
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


# Start the origin cameras and sent to the server
./startOC.sh

sleep 360
# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe

calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
sleep 2
calcTestCameraPerformance "${CLIENTRESULTFILE}${OCTCP1}.log" $CLIENTPERFORMANCEFILE