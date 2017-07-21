#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

### Set variables
args = sys.argv
outPins = [17, 26]
servo = []

### Check parameter settings
try:
  args[1]
except:
  print("Error: Undefined parameter(on/off)")
  sys.exit(1)
else:
  if args[1] == "on" or args[1] == "off":
    print("Switch "+args[1])
  else:
    print("Error: Acceptable parameter is only 'off' or 'on'")
    sys.exit(1)

try:
  args[2]
except:
  args.append("all")
else:
  if args[2] == "right" or args[2] == "left":
    print("Switch "+args[1]+"("+args[2]+")")
  else:
    print("Error: Acceptable perameter is only 'right' or 'left'")

### Init settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

### Set sensors
for i in range(0, len(outPins)):
  GPIO.setup(outPins[i], GPIO.OUT)
  handle= GPIO.PWM(outPins[i], 50)
  servo.append( handle )

### Change switch status
def lightChange(mode, servo):

  if mode == "on" or mode == "off":
    print("Switch "+mode)
  else:
    print("Error: invalid parameter on lightChange()")
    return None

  nums = {'default': 4.5, 'off': 5.8, 'on': 3.8}

  servo.start(0.0)

  servo.ChangeDutyCycle( nums['default'] )
  time.sleep(0.5)

  servo.ChangeDutyCycle( nums[mode] )
  time.sleep(0.5)

  servo.ChangeDutyCycle( nums['default'] )
  time.sleep(0.5)

### Main
if args[2] == "right":
  lightChange(args[1], servo[1])
elif args[2] == "left":
  lightChange(args[1], servo[0])
elif args[2] == "all":
  for i in range(0, len(outPins)):
    lightChange(args[1], servo[i])
