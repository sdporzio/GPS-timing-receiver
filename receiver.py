import socket

## OPEN SOCKET FOR UDP COMMUNICATION
UDP_IP = "130.92.128.187"  # argoncube27.aec.unibe.ch
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

# Set up destination
dest = "/dev/shm/"

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    f = open(dest+data, 'w+')
    f.close()
    # print("received message: %s" % data)
