### [PT001] PERFORMANCE TEST
# Send 80 messages from 4 cameras to the default test server
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