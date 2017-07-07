#!/bin/bash

### Sensor PIN
pinNum=4

### Enable PIN
sudo echo $pinNum > /sys/class/gpio/export

### Set in-mode
sudo echo in > /sys/class/gpio/gpio$pinNum/direction 

### Set variables
count=0
day=0

while true
do

  ### Sensor State
  result=$(sudo cat /sys/class/gpio/gpio$pinNum/value)
  # echo DoorState: $result

  ### Check Door State
  if [ $result = "0" ]
  then

    ### Door OPEN
    echo "Door OPEN"
    let count++

  else

    ### Door CLOSE
    echo "Door CLOSE"
    count=0

  fi

  ### Door OPEN
  if [ $count = "1" ]
  then

    ### Check first OPEN on day
    if [ $day != "$(date +'%y%m%d')" ]
    then

      echo "First OPEN"

      ### Re-set day
      day="$(date +'%y%m%d')"

      ### Post to Slack
      TOKEN=''
      USER='DoorBot'
      CHANNEL='random'
      MESSAGE="The door was opened at $(date +'%H:%M:%S')"

      #curl -s -XPOST -d "token=$TOKEN" \
      #               -d "channel=#$CHANNEL" \
      #               -d "text=$MESSAGE" \
      #               -d "username=$USER" \
      #               "https://slack.com/api/chat.postMessage" >& /dev/null &

    fi

    ### Original Actions
    flist=( $(ls /home/pi/sounds/*.wav) )
    key=`expr $RANDOM % ${#flist[*]}`

    aplay ${flist[$key]}

  ### Door CLOSE
  elif [ $count = "0" ]
  then

    # handle
    :

  fi
  
  sleep 1

done
