#include<iostream>

using namespace std;

int main(){
   int a, b;
   cin >> a >> b;
   bool symbol_flag_star = true;
   char star = '*';
   char dot = '.';
   for(int i=0;i<a;i++){
       if(i%2==0)
            symbol_flag_star = true;
        else
            symbol_flag_star = false;
       for(int j=0;j<b;j++){
           if(symbol_flag_star){
                cout << star;
                symbol_flag_star=!symbol_flag_star;
           }
            else{
                cout << dot;
                symbol_flag_star=!symbol_flag_star;
            }
       }
       cout << "\n";
   }
}