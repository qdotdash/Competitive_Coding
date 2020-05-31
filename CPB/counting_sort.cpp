#include<bits/stdc++.h>

using namespace std;

int main(){
    int size;
    cin >> size;
    int llim, ulim;
    cin >> llim >> ulim;
    if(ulim==llim){
        return 0;
    }
    if(ulim<llim){
        int temp;
        temp = ulim;
        ulim = llim;
        llim = temp;
    }

    int arr[size];
    int output[size] = {0};
    int num;

    for(int i=0; i<size; i++){
        cin >> num;
        if(num>=llim && num<=ulim){
            arr[i] = num;
        }
        else{
            cout << "Unchartred territory\n";
            i--;
        }
    }
    
    cout << "\nEntered array\n";

    for(int i=0; i<size; i++){
        cout << arr[i] << " ";
    }
    cout << "\n";

    int barr[ulim-llim+1] = {0};

    for(int i=0; i<size; i++){
        barr[arr[i]-llim]++;
    }

    cout << "\nBarray\n";

    for(int i=0; i<ulim-llim+1; i++){
        cout << barr[i] << " ";
    }
    cout << "\n";

    for(int i=1; i<ulim-llim+1; i++){
        barr[i] += barr[i-1];
    }

    cout << "\nBarray after adding\n";

    for(int i=0; i<ulim-llim+1; i++){
        cout << barr[i] << " ";
    }
    cout << "\n";

    for(int i=ulim-llim; i>0; i--){
        barr[i] = barr[i-1];       
    }
    barr[0] = 0;

    cout << "\nBarray after shifting\n";

    for(int i=0; i<ulim-llim+1; i++){
        cout << barr[i] << " ";
    }
    cout << "\n";

    for(int i=0; i<size; i++){  
        output[barr[arr[i]-llim]] = arr[i];
        barr[arr[i]-llim]++;
    }

    cout << "\nSorted array\n";

    for(int i=0; i<size; i++){
       cout << output[i] << " ";
    }
}