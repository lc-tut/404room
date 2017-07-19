#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 

args = sys.argv

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
