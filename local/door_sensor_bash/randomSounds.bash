#!/bin/bash

flist=( $(ls /home/pi/sounds/*.wav) )

key=`expr $RANDOM % ${#flist[*]}`

echo ${flist[@]}
echo $key

aplay ${flist[$key]}
