import socket
import time
import _thread
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def receivingThread(clientSocket, address):
    while True:
        try:
            data = clientSocket.recv(1024)
            message = data.decode('ascii')
            print(str(address) + " : " + message)
        except:
            print("exception")
            break


def sendingThread(clientSocket, address):
    while True:
        try:
            test = input()
            if test is "":
                data = input("Me: ")
                if data:
                    message = data.encode('ascii')
                    clientSocket.send(message)
                    # print("Me: " + data)
        except:
            print("exception")
            break

initiateConnection = int(input("Do you want to initiate connection? (1/0)"))
if initiateConnection == 1:
    print("I will be the acting client for our chat! ")
    portToBeConnectedTo= int(input("To which port do you want to chat with? "))
    # clientSocket.connect((socket.gethostname(), portToBeConnectedTo))
    clientSocket.connect((socket.gethostname(), portToBeConnectedTo))

    _thread.start_new_thread(receivingThread, (clientSocket, (socket.gethostname(), portToBeConnectedTo), ))
    _thread.start_new_thread(sendingThread, (clientSocket, (socket.gethostname(), portToBeConnectedTo), ))
    time.sleep(120000)


else:
    print("I will be the acting server for our chat! xD")
    port = 9000
    error = False
    while True:
        try:
            clientSocket.bind((socket.gethostname(), port))
            error = False
        except Exception:
            error = True
        finally:
            if error:
                port += 1
            else:
                print(port)
                break
    clientSocket.listen(10)

    while True:
        requestingSocket, address = clientSocket.accept()
        print("Chatting with : " + str(address))
        _thread.start_new_thread(receivingThread, (requestingSocket, address, ))
        _thread.start_new_thread(sendingThread, (requestingSocket, address, ))
    requestingSocket.close()
