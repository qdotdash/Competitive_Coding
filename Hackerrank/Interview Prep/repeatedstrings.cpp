#include<bits/stdc++.h>

using namespace std;

int main(){
    string s;
    cin >> s;
    long  num;
    cin >> num;
    long  unitcount = 0;
    long  totalcount = 0;
    long  remcount = 0;
    for(int i=0; i<s.length(); i++){
        if(s[i]=='a'){
            unitcount++;
            if(i<num%(s.length()))
                remcount++;
        }   
    }
    totalcount = unitcount * (num/(s.length())) + remcount;
    cout << totalcount;
}
