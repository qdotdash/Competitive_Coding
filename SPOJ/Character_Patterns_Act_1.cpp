#include<iostream>

using namespace std;

void printsymbol(int row, int column){
    bool symbol_flag_star = true;
    char star = '*';
    char dot = '.';
    for(int i=0;i<row;i++){
       if(i%2==0)
            symbol_flag_star = true;
        else
            symbol_flag_star = false;
       for(int j=0;j<column;j++){
           if(symbol_flag_star){
                cout << star;
                symbol_flag_star=!symbol_flag_star;
           }
            else{
                cout << dot;
                symbol_flag_star=!symbol_flag_star;
            }
       }
       if(i!=row-1)
            cout << "\n";
   }
}

int main(){
   int test_cases, r, c;
   cin >> test_cases;
   for(int i=0;i<test_cases;i++){
       cin >> r >> c;
       printsymbol(r, c);
       if(i!=test_cases-1)
            cout << "\n\n";
   }
   return 0;
}