from socket import *
import os
host = "192.168.0.4"  #Ip Of Attacker or WAN ip if on wan
port = 2122
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.connect((host,port))
while True:
    msg = input("First:")
    #s.send(msg)
    s.sendall(msg.encode('utf-8'))
    print("Awaiting Reply.......")
    reply = s.recv(1024)
    print("Mukul:" , repr(reply))
s.close()
