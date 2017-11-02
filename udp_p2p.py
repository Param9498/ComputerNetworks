import socket
import _thread as thread
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

initiateConnection = int(input("Do you want to initiate connection? (1/0) "))
port = 9000


def receivingThread(address):
    while True:
        data, address = clientSocket.recvfrom(1024)
        message = data.decode('ascii')
        print(str(address) + " : " + message)


def sendingThread(address):
    while True:
        test = input()
        if test == "":
            data = input("Me: ")
            message = data.encode('ascii')
            clientSocket.sendto(message, address)

if initiateConnection == 0:
    isPortFound = False
    while True:
        try:
            clientSocket.bind((socket.gethostname(), port))
            isPortFound = True
        except:
            isPortFound = False
        finally:
            if isPortFound is False:
                port += 1
            else:
                break
    print(port)
    message, clientAddress = clientSocket.recvfrom(1024)
    thread.start_new_thread(receivingThread, (clientAddress, ))
    thread.start_new_thread(sendingThread, (clientAddress, ))
    time.sleep(100000)

else:
    portToChatWith = int(input("What port do you want to chat with? "))
    serverAddress = (socket.gethostname(), portToChatWith)
    clientSocket.sendto("Establishing Connection".encode('ascii'), (socket.gethostname(), portToChatWith))
    thread.start_new_thread(receivingThread, (serverAddress, ))
    thread.start_new_thread(sendingThread, (serverAddress, ))
    time.sleep(100000)
