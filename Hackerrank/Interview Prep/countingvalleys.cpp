#include<bits/stdc++.h>

using namespace std;

int countvalleys(int steps, string s){
    int nvalleys = 0;
    int val = 0;
    int flag = 0;
    for(int i=0; i<steps; i++){
        if(s[i]=='U')
            val++;
        else
            val--;

        if(val==0){
            flag = 0;
        }  

        if(val==-1&&flag==0){
            flag = 1;
            nvalleys++;
        }
    }
    return nvalleys;

}

int main(){
    int steps;
    string s;
    cin >> steps;
    cin.ignore(1, '\n');
    getline(cin, s, '\0');
    int nvalleys = countvalleys(steps, s);
    cout << nvalleys;
}  