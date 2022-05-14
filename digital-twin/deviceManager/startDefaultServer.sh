#!/usr/bin/env bash
echo "Starting Server... "
python3 ServerManager.py --default \
& echo "On PID [$!]"
