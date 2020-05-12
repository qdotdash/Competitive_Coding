#include<iostream>

using namespace std;

int sum_of_digits(int number){
    int temp = number;
    int sum=0;
    while(temp!=0){
        sum = sum + temp%10;
        temp = temp/10;
    }
    return sum;
}

int main(){
    int t, n;
    cin >> t;
    while(t--){
        cin >> n;
        cout << sum_of_digits(n);
        if(t!=0)
            cout << "\n";
    }
}