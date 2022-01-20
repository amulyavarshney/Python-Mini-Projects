import time
from datetime import datetime
import playsound
import socket

# Local Machine: time = 1sec * 86400 = 86.4K. But for excess space: 100K
MAX_SIZE = 100000

# Socket Setup
#AF_NET = ipv4, SOCK_STREAM = TCP (streaming socket)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.16.64.29", 3141)) # change hostname to the machine's IP

i = 1
LAST_HEARD = datetime.now()
print("Current Timestamp: ", LAST_HEARD)
while True:
    time.sleep(1)
    msg = s.recv(MAX_SIZE) #buffer byte-stream, decoded later
    if(msg.decode("utf-8") == "True"):
	    LAST_HEARD = datetime.now()
	    print("Alert", LAST_HEARD)
	    playsound.playsound("alert.mp3")
    else:
        i+= 1
        if(i%1800 == 0):
            i = 1
            print("last heard: ", LAST_HEARD)