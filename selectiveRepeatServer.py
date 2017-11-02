import socket
import time

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

serverSocket.bind((host, port))
serverSocket.listen(10)

while True:
    clientSocket, address = serverSocket.accept()
    expectedPacket = 0
    while True:
        packetDetails = clientSocket.recv(1024)
        if not packetDetails:
            break;
        data = packetDetails.decode('ascii')
        lines = data.split('\r\n')
        packet = int(lines[0])
        error = int(lines[1])
        if error == 0:
            clientSocket.send(str(packet).encode('ascii'))
            expectedPacket += 1
        elif error == 1 or packet != expectedPacket:
            clientSocket.send("-1".encode('ascii'))

    clientSocket.close()

