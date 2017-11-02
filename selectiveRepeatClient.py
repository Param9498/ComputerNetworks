import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((socket.gethostname(), 9999))

windowSize = input("Please Enter the size of window : ")
windowSize = int(windowSize)

numberOfPacketsToBeSent = input("Please enter the number of packets to be sent : ")
numberOfPacketsToBeSent = int(numberOfPacketsToBeSent)

print("Please enter the packets where there will be error in transmission : (enter a character to stop)")
errors = []
while True:
    errorPacket = input()
    print(errorPacket.isdigit())
    if errorPacket.isdigit() is not False and int(errorPacket) <= numberOfPacketsToBeSent - 1:
        errors.append(int(errorPacket))
    else:
        break

print(errors)


def attachDelimiterAtEndOfStrings(packet, packetError):
    string = str(packet) + "\r\n" + str(packetError) + "\r\n"
    return string

maxNumberOfTimesErrorOccurs = 1
errorForEachPacket = [0] * numberOfPacketsToBeSent


i = 0
while i < numberOfPacketsToBeSent:
    if i in errors and errorForEachPacket[i] < maxNumberOfTimesErrorOccurs:
        clientSocket.send(attachDelimiterAtEndOfStrings(i, 1).encode('ascii'))
        time.sleep(3)
        errorForEachPacket[i] += 1
    else:
        clientSocket.send(attachDelimiterAtEndOfStrings(i, 0).encode('ascii'))
        time.sleep(3)

    acknowledgement = clientSocket.recv(1024)
    acknowledgement = acknowledgement.decode('ascii')
    acknowledgement = int(acknowledgement)
    if acknowledgement == -1:
        print("Negative Acknowledgement received for packet " + str(i))
        i -= 1
    else:
        print("Positive Acknowledgement received for packet " + str(i))
    i += 1



clientSocket.close()