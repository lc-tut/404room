#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hug
import multiSwitch

# hug -f expr.py

@hug.get('/switch')
def switch(mode, name):
  if mode == "on" or mode == "off":
    if name == "right" or name == "left" or name == "all":
      args = [0, mode, name]
    else:
      return 1

    multiSwitch.Main(args)
  
  else:
    return 1

  return "state: {}, switch: {}".format(mode, name)
