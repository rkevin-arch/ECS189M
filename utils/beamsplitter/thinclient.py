#!/usr/bin/python3
import socket
import os

#used for debug purposes only, can send raw commands to beamsplitter server

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
        sock.sendall(line.encode())
        print(sock.recv(1000).decode())
    finally:
        sock.close()
