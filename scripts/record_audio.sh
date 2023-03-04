#!/bin/bash

INPUTMP3_FILE="audio/chatgpt_input.mp3"
VERSION_FILE="audio/chatgpt_input.version"

arecord -v -f cd -t raw | lame -r - "$INPUTMP3_FILE"

if [ -f "$VERSION_FILE" ]; then
    VERSION=$(cat $VERSION_FILE)
else
    VERSION=0
fi
echo $(($VERSION+1)) > $VERSION_FILE
