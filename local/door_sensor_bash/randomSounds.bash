#!/bin/bash

flist=( $(ls *.mp3 *.wav) )

key=`expr $RANDOM % $(ls *.mp3 *.wav|wc -l)`

# echo ${flist[@]}
echo $key

aplay ${flist[$key]}
