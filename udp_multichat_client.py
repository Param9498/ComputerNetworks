import socket
import _thread as thread
import time
import sys


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

nickName = input("Enter your nickname for this chatroom : ")
nickName = "$123EncodedSTRING" + nickName

clientSocket.sendto(nickName.encode('ascii'), (socket.gethostname(), 9999))
serverPort = 9999

hasExited = False

def receivingThread():
    global hasExited
    while True:
        data, address = clientSocket.recvfrom(1024)
        message = data.decode('ascii')
        if message == "$123EncodedEXIT":
            print("You have successfully exited the chatroom. You cannot send/receive messages anymore. Restart to join again.")
            hasExited = True
            return
        print(message)

def sendingThread():
    global hasExited
    while True:
        if hasExited:
            sys.exit(0)
        test = input()
        if test == "":
            data = input("Me: ")
            message = data.encode('ascii')
            clientSocket.sendto(message, serverAddress)

data, serverAddress = clientSocket.recvfrom(1024)
message = data.decode('ascii')
print(message)

thread.start_new_thread(receivingThread, ())
thread.start_new_thread(sendingThread, ())
time.sleep(100000)