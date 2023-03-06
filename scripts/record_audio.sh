#!/bin/bash

INPUTWAV_FILE="audio/chatgpt_input.wav"
VERSION_FILE="audio/chatgpt_input.version"

#arecord -v -f cd -t raw | lame -r - "$INPUTWAV_FILE"
#
#if [ -f "$VERSION_FILE" ]; then
#    VERSION=$(cat $VERSION_FILE)
#else
#    VERSION=0
#fi
#echo $(($VERSION+1)) > $VERSION_FILE

python3 src/AudioRec.py
