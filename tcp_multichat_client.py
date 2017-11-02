import socket
import time
import _thread as thread
import sys

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((socket.gethostname(), 9999))

nickName = input("Please enter your nickname for this chat room: ")
clientSocket.send(nickName.encode('ascii'))

isWorking = True

def sendingThread():
    global isWorking
    while True:
        test = input()
        if test is "":
            data = input("Me: ")
            message = data
            message = message.encode('ascii')
            clientSocket.send(message)
            if data == "EXIT":
                isWorking = False
                return

def receivingThread():
    global isWorking
    while True:
        if isWorking is False:
            return
        data = clientSocket.recv(1024)
        message = data.decode('ascii')
        print(message)


thread.start_new_thread(sendingThread, ())
thread.start_new_thread(receivingThread, ())
time.sleep(10000)