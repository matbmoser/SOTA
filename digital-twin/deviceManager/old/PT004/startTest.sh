### [PT004] PERFORMANCE TEST
# Send messages between WebSocket cameras at the same moment
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

# Start the Destination cameras
./startDC.sh

# Start origin cameras
./startOC.sh

wait -n

sleep 15
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
wait -n

# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe