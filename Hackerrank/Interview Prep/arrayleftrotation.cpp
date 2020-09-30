#include<bits/stdc++.h>

using namespace std;

int main(){
    int integers, rotation;
    cin >> integers >> rotation;
    int arr[integers], rotatedarr[integers];
    for(int i=0; i<integers; i++){
        cin >> arr[i];
    }
    for(int j=0; j<integers; j++){
        int index = (integers - (rotation%integers) + j)%integers;
        rotatedarr[index] = arr[j];
    }
    
    for(int k=0; k<integers; k++){
        cout << rotatedarr[k] << " ";
    }
}