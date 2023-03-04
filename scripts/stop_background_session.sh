#!/bin/bash

PIDPATH=".session.pid"

if [ -f "$PIDPATH" ]; then
    kill "$(cat $PIDPATH)"
    rm -f $PIDPATH
fi
