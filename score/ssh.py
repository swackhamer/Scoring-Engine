#!/usr/bin/python

import socket

def isSSH(ip, port=22):
    HOST = ip
    PORT = port
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((HOST, PORT))
        data = s.recv(8)
    except:
        return False
        
    if data == "SSH-2.0-":
        return True
    return False

if __name__ == '__main__':
    print isSSH('192.168.1.5')
