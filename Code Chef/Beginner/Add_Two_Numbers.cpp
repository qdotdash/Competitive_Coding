#include<bits/stdc++.h>

using namespace std;

int main(){
    int number_of_test_cases;
    int a, b;
    cin >> number_of_test_cases;
    for(int i=0; i<number_of_test_cases; i++){
        cin >> a >> b;
        cout << a + b;
        if(i!=number_of_test_cases-1)
            cout << "\n";   
    }
}