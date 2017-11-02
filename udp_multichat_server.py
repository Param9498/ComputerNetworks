import socket
import time
import _thread

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind((socket.gethostname(), 9999))

listOfClientDetails = []

def receivingThread():
    while True:
        data, clientAddress = serverSocket.recvfrom(1024)
        message = data.decode('ascii')
        if message.startswith("$123EncodedSTRING"):
            nickName = message[len("$123EncodedSTRING"):]
            listOfClientDetails.append([clientAddress, nickName])
            message = nickName + " has joined CHATROOM"
            print(message)
            data = message.encode('ascii')
            for cDetail in listOfClientDetails:
                serverSocket.sendto(data, cDetail[0])
        elif message == "EXIT":
            serverSocket.sendto("$123EncodedEXIT".encode('ascii'), clientAddress)
        else:
            for clientDetail in listOfClientDetails:
                if clientDetail[0] == clientAddress:
                    nickName = clientDetail[1]
                    message = nickName + " : " + message
                    print(message)
                    data = message.encode('ascii')
                    for cDetail in listOfClientDetails:
                        if cDetail[0] != clientAddress:
                            serverSocket.sendto(data, cDetail[0])
                    break

print("This is the SERVER")
_thread.start_new_thread(receivingThread, ())
time.sleep(100000)
