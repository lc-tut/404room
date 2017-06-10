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
    count=$(expr $count + 1)

  else

    ### Door CLOSE
    count=0

  fi

  ### Door OPEN
  if [ $count = "1" ]
  then

    ### Debug
    echo "Door OPEN"

    ### Check first OPEN on day
    if [ $day != "$(date +'%y%m%d')" ]
    then

      echo "First OPEN"

      ### Re-set day
      day="$(date +'%y%m%d')"

      ### Post to Slack
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

    ### Original Actions
    mpg321 -g 1000 Anal/push.mp3 2>&1 > /dev/null
    mpg321 -g 1000 Anal/suiso.mp3 2>&1 > /dev/null

  ### Door CLOSE
  else

    echo "Door CLOSE"

  fi
  
  sleep 1

done
