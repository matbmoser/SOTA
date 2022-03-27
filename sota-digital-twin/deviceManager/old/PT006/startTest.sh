### [PT003] PERFORMANCE TEST
# Send Messages to server from different WebSocket cameras in parallel
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

# Start the origin cameras and sent to the server
./startOC.sh

sleep 10
calcTestServerPerformance $DEFAULTRESULTSFILE $DEFAULTPERFORMANCEFILE
wait -n

# KILL SERVER
echo "Closing Test Server!"
taskkill //f //im python.exe

