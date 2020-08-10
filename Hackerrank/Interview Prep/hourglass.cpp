#include<bits/stdc++.h>

using namespace std;

int main(){

    int maxhourglasssum = -999;

    int arr[6][6];
    for(int i=0; i<6; i++){
        for(int  j=0; j<6; j++)
            cin >> arr[i][j];
    }

    for(int i=0; i<4; i++){
        for(int j=1; j<5; j++){
            int tempsum = 0;
            tempsum = arr[i][j] + arr[i][j-1] + arr[i][j+1] + arr[i+1][j] + arr[i+2][j] + arr[i+2][j-1] + arr[i+2][j+1];
            if(tempsum>maxhourglasssum)
                maxhourglasssum = tempsum;
        }
    }
    cout << maxhourglasssum;
}