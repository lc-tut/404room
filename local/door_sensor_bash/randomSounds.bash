#!/bin/bash

flist=( $(ls sounds/*.mp3 sounds/*.wav) )

key=`expr $RANDOM % $(ls sounds/*.mp3 sounds/*.wav|wc -l)`

# echo ${flist[@]}
echo $key

afplay ${flist[$key]}
