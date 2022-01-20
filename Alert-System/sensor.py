#!/usr/bin/python
import time
import RPi.GPIO as GPIO

sound = 17
#GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)

GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=100)  # let us know when the pin goes HIGH or LOW

def callback(sound):
        print("callback")
        if GPIO.input(sound):
            print("Sound Detected!")
        else:
            print("in here")

GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on change

while True:
        time.sleep(1)

GPIO.cleanup()