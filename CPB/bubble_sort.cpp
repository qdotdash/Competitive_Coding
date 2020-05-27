#include<bits/stdc++.h>

#define loop(i, n) for(int i=0; i<lim; i++)

using namespace std;

int main(){
    int lim, arr[100];
    cin >> lim;
    loop(i, lim){
        cin >> arr[i];
    }


    loop(i, lim){
        loop(j, lim-1){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    loop(i, lim){
        cout << arr[i] << " ";
    }

}