import socket
import time
import _thread as thread

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), 9999))

listOfClientsConnected = []

serverSocket.listen(10)

def receiveThread(clientSocket, address, nickName):
    once = False
    while True:
        if once is False:
            entered = nickName + " HAS ENTERED CHAT ROOM"
            print(entered)
            for clientDetails in listOfClientsConnected:
                clientDetails[0].send(entered.encode('ascii'))
            once = True
        data = clientSocket.recv(1024)
        if data:
            message = data.decode('ascii')
            print(message)
            if message.strip() == "EXIT":
                left = nickName + "HAS LEFT CHAT ROOM"
                print(left)
                for clientDetails in listOfClientsConnected:
                    clientDetails[0].send(left.encode('ascii'))
                thread.exit()
            message = nickName + " : " + message
            print(message)
            for clientDetails in listOfClientsConnected:
                if clientDetails[1] is not nickName:
                    clientDetails[0].send(message.encode('ascii'))

while True:
    clientSocket, address = serverSocket.accept()
    nName = clientSocket.recv(1024)
    nickName = nName.decode('ascii')
    client = [clientSocket, nickName]
    listOfClientsConnected.append(client)
    thread.start_new_thread(receiveThread, (clientSocket, address, nickName))
