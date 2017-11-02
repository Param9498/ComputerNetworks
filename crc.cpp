#include <iostream>
#include <vector>

using namespace std;

int main(){
    cout<<"Enter the Data to be sent: ";
    string data;
    cin>>data;


    vector<int> binaryData;
    vector<int> binaryDataCopy;
    for (int i = 0; i < data.length(); ++i) {
        binaryData.push_back(data[i] - '0');
        binaryDataCopy.push_back(data[i] - '0');
    }


    cout<<"\nEnter the polynomial: ";
    string poly;
    cin>>poly;
    vector<int> polyData;
    for (int i = 0; i < poly.length(); ++i) {
        polyData.push_back(poly[i] - '0');
    }


    int redundantBits = polyData.size()-1;
    for (int i = 0; i < redundantBits; ++i) {
        binaryDataCopy.push_back(0);
    }

    int j, k;
    for (int i = 0; i < binaryData.size(); ++i) {
        if(binaryDataCopy[i] >= polyData[0]){
            for (int j = 0, k = i; j < polyData.size(); ++j, ++k) {
                if(binaryDataCopy[k] == polyData[j]){
                    binaryDataCopy[k] = 0;
                } else{
                    binaryDataCopy[k] = 1;
                }
            }
        }
    }

    for (int i = 0; i < binaryDataCopy.size(); ++i) {
        cout<<" "<<binaryDataCopy[i];
    }
    cout<<endl;
}