import socket
import os
import glob

## OPEN SOCKET FOR UDP COMMUNICATION
UDP_IP = "130.92.128.187"  # argoncube27.aec.unibe.ch
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

# Set up destination
dest = "/dev/shm/utc_timestamps/"

while True:
    # Receive timestamp from argoncube03
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    # Open and save new file, with filename equal to current timestamp
    f = open(dest+data.decode('utf8'), 'w+')
    f.close()
    # Look for any other timestamp file in /dev/shm which is not the current one and delete it
    for file in os.scandir(dest):
        if file.name!=data.decode('utf8'):
            os.remove(file.path)
    # Confirmation message
    print("received message: %s" % data)
