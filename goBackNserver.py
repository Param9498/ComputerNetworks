import socket
import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((socket.gethostname(), 9999))
serverSocket.listen(10)

while True:
    clientSocket, address = serverSocket.accept()
    print("Received request for sending frames from : %s" % str(address))
    windowSize = clientSocket.recv(1024)
    print("Window size entered by user = " + windowSize.decode('ascii'))
    numberOfPacketsToBeSent = clientSocket.recv(1024)
    print("The client is requesting to send " + numberOfPacketsToBeSent.decode('ascii') + " Packets")
    expectedPacket = 0
    while True:
        packetDetails = clientSocket.recv(1024)
        if not packetDetails:
            break
        data = packetDetails.decode('ascii')
        lines = data.split('\r\n')
        packet = lines[0]
        error = lines[1]
        print(packet)
        #print(error)
        if int(error) == 1 or int(packet) != expectedPacket:
            time.sleep(3)
            clientSocket.send(str(packet).encode('ascii'))
        else:
            time.sleep(3)
            clientSocket.send(str(-1).encode('ascii'))
            expectedPacket += 1
    clientSocket.close()

