#!/usr/bin/env python
import RPi.GPIO as GPIO
import syslog
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

checker = False

while True:
 channel = GPIO.wait_for_edge(13, GPIO.BOTH, timeout=500)
 if channel is None:
  print("Timeout")
  if checker:
   checker = False
   GPIO.output(17, GPIO.HIGH)
  else:
   GPIO.output(17, GPIO.LOW)
   checker = True
 else:
  syslog.syslog("Button pressed")
  print("Button pressed")
  os.system("sudo shutdown -h now")
GPIO.cleanup()

