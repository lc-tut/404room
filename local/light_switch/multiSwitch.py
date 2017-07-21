#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

if __name__ == "__main__":

  ### Set variables
  args = sys.argv
  # outPins = [17, 26]
  outPins = {"right": 17, "left": 26}
  servo = []

  ### Check parameter settings
  try:
    args[1]
  except:
    print("Error: Undefined parameter(on/off)")
    sys.exit(1)
  else:
    if args[1] != "on" and args[1] != "off":
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
  for key,val in outPins.items():
    GPIO.setup(val, GPIO.OUT)
    handle= GPIO.PWM(val, 50)
    servo.append( handle )

  ### Change switch status
  def lightChange(servos, modes):

    servoSpeeds = {'default': 4.5, 'off': 5.8, 'on': 3.8}

    for i in range(0, len(servos)):
      servos[i].start(0.0)

    for i in range(0, len(servos)):
      servos.ChangeDutyCycle( servoSpeeds['default'] )

    time.sleep(0.5)

    for i in range(0, len(servos)):
      servos[i].ChangeDutyCycle( servoSpeeds[ modes[i] ] )

    time.sleep(0.5)

    for i in range(0, len(servos)):
      servos.ChangeDutyCycle( servoSpeeds['default'] )

    time.sleep(0.5)

  ### Reverse set value(on/off)
  def revVal(state):
    if state == "on":
      return "off"
    elif state == "off":
      return "on"
    else:
      return None

  ### Main
  if args[2] == "right":
    modes = {"right": args[1], "left": revVal(args[1])}
  elif args[2] == "left":
    modes = {"right": revVal(args[1]), "left": args[1]}
  elif args[2] == "all":
    modes = {"right": args[1], "left": args[1]}
  
  lightChange(servos, modes)

