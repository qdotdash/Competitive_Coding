#include<bits/stdc++.h>

using namespace std;

int main(){

    int size;
    int arr[100];
    cin >> size;


    for(int i=0; i<size; i++){
        cin >> arr[i];
    }

    sort(arr, arr + size, greater<int>());

    for(int i=0; i<size; i++){
        cout << arr[i];
    }

    string s = "monkey";
    sort(s.begin(), s.end());
    cout << "\n" << s;
}