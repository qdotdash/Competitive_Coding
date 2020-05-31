#include<bits/stdc++.h>

using namespace std;

bool comp(int a, int b){
    if(a!=b){
        return a>b;
    }   
    return true;
}

int main(){
    int arr[100] = {1,2,3,4,5};
    sort(arr, arr + 5, comp);
    for(int i=0; i< 5; i++){
        cout << arr[i];
    }
}