import socket
import pyfiglet
import sys
from datetime import datetime

banner = pyfiglet.figlet_format("port scanner")
print(banner)

target = input("Please enter the target name")
host = socket.gethostbyname(target)

for port in range(1, 1025):
    #socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #attempt to connect the socket to a specified host and port
    result = sock.connect_ex((host, port))
    sock.settimeout(1)
    if result == 0:
        print("port no : {} open".format(port))
    #else:
        #print("port no : {} closed".format(port))
        







