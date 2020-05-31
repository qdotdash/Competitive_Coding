#include<bits/stdc++.h>

using namespace std;

int main(){
    struct P{
        int x, y;
        bool operator<(const P &p){
            if(y!=p.y) return y<p.y;
            else return x<p.x;
        }
    };

    struct P a, b;
    a.x = 3;
    a.y = 4;
    b.x = 1;
    b.y = 5;
    if(a<b){
        cout << "a";
    }
    else{
        cout << "b";
    }

    //should print a because a<b because a.y = 4 < b.y = 5 even though a.x = 3 > b.x = 1. my function prioritises y cordinate
}