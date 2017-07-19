#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

### Set variables
args = sys.argv
gp_out = 17

### Init settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(gp_out, GPIO.OUT)
servo = GPIO.PWM(gp_out, 50) 

### Check parameter settings
try:
  args[1]
except:
  print("Error: Undefined parameter(on/off)")
  sys.exit(1)

### Check parameter strings
if args[1] == "on":
  print("Switch ON")
elif args[1] == "off":
  print("Switch OFF")
else:
  print("Error: Acceptable parameter is only 'off' or 'on'")
  sys.exit(1)

### Main
servo.start(0.0)

nums = {'default': 4.5, 'off': 5.8, 'on': 3.8}

servo.ChangeDutyCycle( nums['default'] )
time.sleep(0.5)

servo.ChangeDutyCycle( nums[ args[1] ] )
time.sleep(0.5)

servo.ChangeDutyCycle( nums['default'] )
time.sleep(0.5)

GPIO.cleanup()

