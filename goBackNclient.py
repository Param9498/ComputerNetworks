import socket
import time

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((socket.gethostname(), 9999))

windowSize = input("Enter the window Size: ")
clientSocket.send(windowSize.encode('ascii'))

numberOfPacketsToBeSent = input("Enter the number of packets to be sent: ")
clientSocket.send(numberOfPacketsToBeSent.encode('ascii'))

withError = input("Do you want to send packets with Error(1) or without Error(0) : ")

packetWithError = int(-1)
endOfFrame = int(numberOfPacketsToBeSent) + 1
errors = []
if int(withError) == 1:
    #packetWithError = int(input("Which packet has error? (enter character to quit)"))
    print("Which packet has error? (enter character to quit)")
    while True:
        val = input()
        if val.isdigit() and int(val) <= int(numberOfPacketsToBeSent) - 1:
            errors.append(int(val))
        else:
            break
    errors.sort()
    tests = errors
    # print(tests)
    # Remove if already in frame
    j = 0
    while j < len(tests):
        frames = []
        last = tests[j] + int(windowSize) - 1
        if last > int(numberOfPacketsToBeSent) - 1:
            last = int(numberOfPacketsToBeSent) - 1
        for i in range(tests[j], last+1):
            frames.append(i)
        skipFirst = 0
        i = 0
        while i < len(tests):
            if tests[i] != frames[0]:
                if tests[i] in frames:
                    tests.remove(tests[i])
                    i = -1
            i += 1
        j += 1

    errors = tests
    errors.sort()

    i = 0
    endOfFrame = [0] * int(numberOfPacketsToBeSent)
    while i < int(numberOfPacketsToBeSent):
        if i + int(windowSize) - 1 <= int(numberOfPacketsToBeSent) - 1:
            endOfFrame[i] = i + int(windowSize) - 1
        else:
            endOfFrame[i] = int(numberOfPacketsToBeSent) - 1
        # print(endOfFrame[i])
        i += 1


def attachMarkerAtEndOfString(packet, packetWithError):
    """test"""
    finalString = str(packet)+"\r\n"+str(packetWithError)+"\r\n"
    return finalString

numberOfTimesError = 1
currentNumberOfTimesError = [0] * int(numberOfPacketsToBeSent)
i = 0
currentErrorFrame = -1
# print(errors)

currentFrameForErrorPackets = [-1] * int(numberOfPacketsToBeSent)
i = 0
while i < int(numberOfPacketsToBeSent):
    # print(i)
    if i in errors:
        for j in range(int(windowSize)):
            # print(i+j)
            if i + j < int(numberOfPacketsToBeSent):
                currentFrameForErrorPackets[i+j] = errors[errors.index(i)]
        i = i + int(windowSize) - 1
    i += 1
# def display():
#     s1 = []
#     for i in range(int(numberOfPacketsToBeSent)):
#         s1.append(i)
#     return s1
#
#
# print(display())

# print(endOfFrame)
# print(currentNumberOfTimesError)
# print(currentFrameForErrorPackets)
i=0
while i < int(numberOfPacketsToBeSent):
    #print("inside")
    if i in errors and currentNumberOfTimesError[i] < numberOfTimesError:
        print("Sending " + str(i))
        clientSocket.send(attachMarkerAtEndOfString(i, 1).encode('ascii'))
        currentNumberOfTimesError[i] = 1
    else:
        print("Sending " + str(i))
        clientSocket.send(attachMarkerAtEndOfString(i, 0).encode('ascii'))

    acknowledgement = int(clientSocket.recv(1024).decode('ascii'))
    if acknowledgement == -1:
        print("Positive Acknowledgement for " + str(i))
        time.sleep(2)

    else:
        print("Negative Acknowledgement for " + str(i))
        time.sleep(2)
        if i >= endOfFrame[currentFrameForErrorPackets[i]]:
            if currentFrameForErrorPackets[i] != -1:
                i = currentFrameForErrorPackets[i] - 1
    i += 1
clientSocket.close()

