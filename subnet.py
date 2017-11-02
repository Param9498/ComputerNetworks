import math
import sys
import textwrap

while True:
    stringIPAddress = input("Please Enter an IP address : ")
    ipComponentsString = stringIPAddress.split('.')
    ipComponentsInteger = []

    lengthOfIPComponents = len(ipComponentsString)

    if lengthOfIPComponents != 4:
        print("Please Enter a proper IP address")
        continue

    wrongIP = False
    ipClass = 0
    i = 0
    for component in ipComponentsString:
        if component.isdigit() is False or int(component) > 255 or int(component) < 0:
            wrongIP = True
        else:
            if i == 0:
                if int(component) <= 127:
                    ipClass = 1
                elif int(component) <= 191:
                    ipClass = 2
                elif int(component) <= 223:
                    ipClass = 3
                elif int(component) <= 239:
                    ipClass = 4
                elif int(component) <= 255:
                    ipClass = 5
            ipComponentsInteger.append(int(component))
        i += 1

    if wrongIP is True:
        print("Please Enter a proper IP address")
        continue

    break

stringListOfBinaryIPComponents = []

for component in ipComponentsInteger:
    stringListOfBinaryIPComponents.append("{0:08b}".format(component))

# print(stringListOfBinaryIPComponents)
print("IP address in binary is : " + ".".join(stringListOfBinaryIPComponents))

if ipClass == 4:
    print("No additional Sub Networks can be added")
    print("Subnet Mask is : 255.255.255.255")
    sys.exit(0)

if ipClass == 5:
    print("Sorry this class of IP is reserved for Experimental functions only")
    sys.exit(0)

numberOfExtraSubNetworksToBeAdded = input("Please enter the additional number of Sub Networks : ")

numberOfExtraBitsRequired = math.ceil(math.log(int(numberOfExtraSubNetworksToBeAdded), 2))

print("Number of Extra bits for adding " + numberOfExtraSubNetworksToBeAdded + " sub-networks is : "
      + str(numberOfExtraBitsRequired))

totalNumberOfBitsToBeReservedForSubNetworks = 0
if ipClass == 1:
    totalNumberOfBitsToBeReservedForSubNetworks = 8 + numberOfExtraBitsRequired
elif ipClass == 2:
    totalNumberOfBitsToBeReservedForSubNetworks = 16 + numberOfExtraBitsRequired
elif ipClass == 3:
    totalNumberOfBitsToBeReservedForSubNetworks = 24 + numberOfExtraBitsRequired

string = ""
i = 0
while i < 32:
    if i < totalNumberOfBitsToBeReservedForSubNetworks:
        string = string + "1"
    else:
        string = string + "0"
    i += 1

listOfSubNetMaskComponentsInBinaryString = textwrap.wrap(string, 8)

listOfSubNetMaskComponentsInInteger = []

for string in listOfSubNetMaskComponentsInBinaryString:
    listOfSubNetMaskComponentsInInteger.append(str(int(string, 2)))

print(".".join(listOfSubNetMaskComponentsInBinaryString))
print(".".join(listOfSubNetMaskComponentsInInteger))
