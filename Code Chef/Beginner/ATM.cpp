#include<iostream>
#include<math.h>
#include<bits/stdc++.h>

using namespace std;

int main(){
    float withdrawal, initial_balance, final_balance;
    cin >> withdrawal >> initial_balance;
    final_balance = initial_balance;
    if(fmod(withdrawal, 5)==0&&withdrawal+0.5 < initial_balance){
        final_balance = initial_balance - 0.5 - withdrawal;
    }
    cout << fixed << setprecision(2) << final_balance;
}