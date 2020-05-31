#include<bits/stdc++.h>

using namespace std;

int main(){
    int a=0, b=9;
    int mid;
    int arr[10] = {0,1,2,3,4,5,6,7,8,9};
    int num = 43;
    //find 7
    while(abs(a-b)!=1){
        mid = (a+b)/2;
        if(arr[mid]==num){
            cout << mid;
            break;
        }
        else if(num>arr[mid]){
            a = mid+1;
        }
        else{
            b = mid-1;
        }
    }
}