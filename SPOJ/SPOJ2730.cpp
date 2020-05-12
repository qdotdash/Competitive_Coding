#include<iostream>
#include<stdio.h>

using namespace std;

int main(){
    int num;
    cin >> num;
    do{
        cout << num << "\n";
        cin >> num;
        fflush(stdout);
    }while(num!=42);
    cout << num;
    fflush(stdout);
    return 0;
}