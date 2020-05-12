#include<iostream>

using namespace std;

long long int Fact(long long int number){
    long long int fact = 1;
    for(int i=number; i>0; i--){
        fact = fact * i;
    }
    return fact;
}

int main(){
    int ntc;
    long long int t;
    cin >> ntc;
    while(ntc--){
         cin >> t;
         cout << Fact(t);
         if(ntc!=0)
            cout << "\n";

    }
}