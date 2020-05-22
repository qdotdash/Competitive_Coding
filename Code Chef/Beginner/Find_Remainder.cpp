#include<iostream>

using namespace std;

int main(){
    int tc, a, b;
    cin >> tc;
    while(tc--){
        cin >> a >> b;
        cout << a%b;
        if(tc!=0){
            cout << "\n";
        }
    }
}