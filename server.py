#!/usr/bin/python3
import socket

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

serverSocket.bind((host,port))

serverSocket.listen(3)

while True:
    clientSocket,address = serverSocket.accept()

    print("Receive Connetion from " % str(address))
    msg = "Hello You are  Connected"
    clientSocket.send(msg)
    clientSocket.close()

