import time
import socket
import RPi.GPIO as GPIO

# Socket Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# localhost
s.bind(("172.16.64.29", 3141))
s.listen(5)
clientsocket, address = s.accept()
print(f"Connection established from {address}")

sound = 17
# GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sound, GPIO.IN)

def callback(sound):
        if GPIO.input(sound):
            global_sound = True
            print("Sound Detected!")
        else:
            global_sound = False
        clientsocket.send(bytes(f"{global_sound}", "utf-8")) ### modified in the raspian

GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=100) # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(sound, callback)  # assign function to GPIO PIN, Run function on change

while True:
    time.sleep(2)

GPIO.cleanup()
