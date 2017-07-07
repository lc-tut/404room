#!/bin/bash

TOKEN='YourTOKEN'
USER='DoorSensor'
CHANNEL='random'
MESSAGE="The door was opened at $(date +'%H:%M:%S')"

curl -XPOST -d "token=$TOKEN" \
            -d "channel=#$CHANNEL" \
            -d "text=$MESSAGE" \
            -d "username=$USER" \
            "https://slack.com/api/chat.postMessage"

echo
