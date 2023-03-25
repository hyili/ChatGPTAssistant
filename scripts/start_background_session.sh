#!/bin/bash

PIDPATH=".session.pid"

if [ -f "$PIDPATH" ]; then
    kill "$(cat $PIDPATH)"
    rm -f $PIDPATH
fi

rm -f audio/*
python3 src/from_voice.py 2>/dev/null &
echo "$!" > $PIDPATH
