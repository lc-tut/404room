#!/bin/bash

### Sensor PIN
pinNum=4

### Enable PIN
sudo echo $pinNum > /sys/class/gpio/export

### Set in-mode
sudo echo in > /sys/class/gpio/gpio$pinNum/direction 

### Set variables
count=0
slack=0

while true
do
  ### Sensor State
  result=$(sudo cat /sys/class/gpio/gpio$pinNum/value)
  echo DoorState: $result

  ### Check Door State
  if [ $result = "0" ]
  then

    ### Door OPEN
    count=$(expr $count + 1)

  else

    ### Door CLOSE
    count=0

  fi

  ### Door Open
  if [ $count = "1" ]
  then

    if [ $slack = 0 ]
    then

      $slack=1
      echo "First OPEN"

      ### First OPEN on day
      TOKEN='YourTOKEN'
      USER='doorBot'
      CHANNEL='random'
      MESSAGE='Door Opened DATE'

    curl -XPOST -d "token=$TOKEN" \
                -d "channel=#$CHANNEL" \
                -d "text=$MESSAGE" \
                -d "username=$USER" \
                "https://slack.com/api/chat.postMessage" &

    fi

    mpg321 -g 1000 Anal/push.mp3 2>&1 > /dev/null
    mpg321 -g 1000 Anal/suiso.mp3 2>&1 > /dev/null

  fi
  
  sleep 1

done


