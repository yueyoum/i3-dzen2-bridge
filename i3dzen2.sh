#!/bin/bash

SELF_PATH=`readlink -f $0`
PROJECT_PATH=`dirname "$SELF_PATH"`

cd "$PROJECT_PATH"

sleep 1
i3status | ./i3-dzen-bridge.py | dzen2 -y -1 -fn "ubuntu mono" -ta r &

exit 0

