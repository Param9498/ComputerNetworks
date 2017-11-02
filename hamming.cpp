#include <iostream>
#include <cstring>
#include <vector>
#include <math.h>

using namespace std;

int main() {
    string binaryString;
    vector<char> v;
    while (true) {
        cout << "Enter the Binary Number to be transmitted: ";
        cin >> binaryString;
        copy(binaryString.begin(), binaryString.end(), back_inserter(v));
        int wrongBinary = 0;
        for (int i = 0; i < v.size(); ++i) {
            if (isdigit(v[i]) && ((v[i] - '0') == 0 || (v[i] - '0') == 1)) {
                continue;
            } else {
                wrongBinary = 1;
                break;
            }
        }
        if (wrongBinary == 1) {
            cout<<"Please enter a proper Binary Number to be sent"<<endl;
            continue;
        } else {
            break;
        }
    }

    int initialSizeOfBinary = v.size();

    int lastUsedPowerOfTwo = pow(2,0);

    int finalSizeOfBinary;
    int extrabits = 0;

    int i = 1;
    while(initialSizeOfBinary>0){
        int currentlyUsedPowerOfTwo = pow(2, i);
        int difference = currentlyUsedPowerOfTwo - lastUsedPowerOfTwo;
        extrabits++;
        if(difference-1 <= initialSizeOfBinary){
            initialSizeOfBinary = initialSizeOfBinary - (difference - 1);
            if(initialSizeOfBinary>0)
                //finalSizeOfBinary++;
                lastUsedPowerOfTwo = currentlyUsedPowerOfTwo;
        }
        else{
            //finalSizeOfBinary = finalSizeOfBinary + initialSizeOfBinary;
            break;
        }
        i++;
    }
//    cout<<"Initial Size: "<<v.size()<<endl;
//    cout<<"Final Size: "<<extrabits+v.size()<<endl;
//    cout<<"Last Used Power of two : "<<lastUsedPowerOfTwo<<endl;

    finalSizeOfBinary = extrabits + v.size();
    int finalBinaryData[finalSizeOfBinary];

    i = 0;
    int index2 = 0;
    while(i<finalSizeOfBinary){
        int j = 0;
        int powersOfTwo = 0;
        int isIndexEqualPower = 0;
        while(powersOfTwo<=lastUsedPowerOfTwo){
            powersOfTwo = pow(2, j);
            if(i+1 == powersOfTwo){
                isIndexEqualPower = 1;
                break;
            }
            j++;
        }
        if(isIndexEqualPower == 1){
            finalBinaryData[i] = -1;
        } else{
            finalBinaryData[i] = v[index2] - '0';
            index2++;
        }
        i++;
    }

//    for (int k = 0; k < finalSizeOfBinary; ++k) {
//        cout<<finalBinaryData[k]<<endl;
//    }

    int powersOfTwo = pow(2, 0);
    int j = 0;
    while(powersOfTwo<=lastUsedPowerOfTwo) {
        int incrementBy = pow(2, j+1);
        int startOfBlock = powersOfTwo - 1;
        int parityBit = 0;
        for (int k = 0; k < powersOfTwo; ++k) {
            for (int l = startOfBlock; l < finalSizeOfBinary; l = l + incrementBy) {
                if(finalBinaryData[l] != -1){
                    parityBit = parityBit ^ finalBinaryData[l];
                }
            }
            startOfBlock++;
        }
        finalBinaryData[powersOfTwo - 1] = parityBit;
        j++;
        powersOfTwo = pow(2, j);
    }

    cout<<"Final data: "<<endl;
    for (int m = 0; m < finalSizeOfBinary; ++m) {
        cout<<finalBinaryData[m]<<" ";
    }

    vector<char> v2;
    vector<int> binaryInInteger;
    while (true) {
        cout<<"Please enter what you received : ";
        cin >> binaryString;
        copy(binaryString.begin(), binaryString.end(), back_inserter(v2));
        int wrongBinary = 0;
        for (int i = 0; i < v2.size(); ++i) {
            if (isdigit(v2[i]) && ((v2[i] - '0') == 0 || (v2[i] - '0') == 1)) {
                binaryInInteger.push_back(v2[i] - '0');
                continue;
            } else {
                wrongBinary = 1;
                break;
            }
        }
        if (wrongBinary == 1) {
            cout<<"Please enter a proper Binary Number to be sent"<<endl;
            continue;
        } else {
            break;
        }
    }

    int index = 0;
    powersOfTwo = pow(2, 0);
    int indexAtWhichError = -1;
    while(powersOfTwo < binaryInInteger.size()){

        int incrementBy = pow(2, index+1);
        int startOfBlock = powersOfTwo - 1;
        int parityBit = 0;
        for (int k = 0; k < powersOfTwo; ++k) {
            for (int l = startOfBlock; l < binaryInInteger.size(); l = l + incrementBy) {
                parityBit = parityBit ^ binaryInInteger[l];
            }
            startOfBlock++;
        }

        if(parityBit == 1){
            indexAtWhichError = indexAtWhichError + powersOfTwo;
        }

        index++;
        powersOfTwo = pow(2,index);
    }

    if(indexAtWhichError == -1){
        cout<<"No error in transmission"<<endl;
    } else{
        cout<<"Error is at bit number "<<indexAtWhichError;
    }

    return 0;


}