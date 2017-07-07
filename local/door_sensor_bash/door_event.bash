#!/bin/bash

### Door OPEN
if [ "$1" = "opened" ]
then

  ### Check first OPEN on day
  if [ $2 = "1" ]
  then

    echo "First OPEN"

    ### Re-set day
    day="$(date +'%y%m%d')"

    ### Post to Slack
    TOKEN='yourToken'
    USER='DoorBot'
    CHANNEL='door-sensor'
    MESSAGE="The door was opened at $(date +'%H:%M:%S')"

    curl -s -XPOST -d "token=$TOKEN" \
                   -d "channel=#$CHANNEL" \
                   -d "text=$MESSAGE" \
                   -d "username=$USER" \
                   "https://slack.com/api/chat.postMessage" >& /dev/null &

  fi

  ### Original Actions
  flist=( $(ls /home/pi/sounds/*.wav) )
  key=`expr $RANDOM % ${#flist[*]}`

  aplay ${flist[$key]} & 

  ### Send POST(uutaro-san)
  curl https://yourHost.com/api/ -X "POST" >& /dev/null &

fi
