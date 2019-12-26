#!/usr/bin/python3
#Beamsplitter client. For details check /root/ecs189/beamsplitter
import socket
import os

def init():
    sockaddr="/var/run/beamsplitter.sock"
    sock=socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect(sockaddr)
    except socket.error as e:
        raise e
    return sock

while True:
    line=input()
    sock=init()
    try:
        sock.sendall(b"R")
        sock.sendall(line.encode())
        print(sock.recv(1000).decode())
    except:
        print("http://localhost:8080/webchal/error.html?")
    finally:
        sock.close()

