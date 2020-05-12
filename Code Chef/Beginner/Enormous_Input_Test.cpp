#include<bits/stdc++.h>

using namespace std;

int main(){
    long int number_of_test_cases;
    int divisor;
    long int test_case;
    long int number_of_divisible=0;
    cin >> number_of_test_cases >> divisor;
    for(int i=0; i<number_of_test_cases; i++){
        cin >> test_case;
        if(test_case%divisor==0)
            number_of_divisible++;
    }
    cout << number_of_divisible;

}