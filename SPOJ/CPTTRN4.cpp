#include<iostream>

using namespace std;

void printsymbol(int row, int column, int height, int width){
    bool symbol_flag_star = true;
    char star = '*';
    char dot = '.';
    for(int i=0;i<row;i++){
       for(int j=0;j<column;j++){
            if(i==0||i==row-1||j==0||j==column-1)
                symbol_flag_star = true;
            else
                symbol_flag_star = false; 
                
           if(symbol_flag_star){
                cout << star;
           }
            else{
               if(i%(height+1)==0||j%(width+1)==0)
                    cout << star;
                else
                    cout << dot;
            }
       }
       if(i!=row-1)
            cout << "\n";
   }
}

int main(){
   int test_cases, r, c, h, w;
   cin >> test_cases;
   for(int i=0;i<test_cases;i++){
       cin >> r >> c >> h >> w;
       printsymbol(r*h+(r+1), c*w+(c+1), h, w); //To find the r and c of the grid
       if(i!=test_cases-1)
            cout << "\n\n";
   }
   return 0;
}