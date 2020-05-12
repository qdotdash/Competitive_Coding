/*
Output

3
3 1 2 1
.|.
.|.
-+-
.|.
.|.
-+-
.|.
.|.
-+-
.|.
.|.

4 4 1 2
..|..|..|..|..
--+--+--+--+--
..|..|..|..|..
--+--+--+--+--
..|..|..|..|..
--+--+--+--+--
..|..|..|..|..
--+--+--+--+--
..|..|..|..|..

2 5 3 2
..|..|..|..|..|..
..|..|..|..|..|..
..|..|..|..|..|..
--+--+--+--+--+--
..|..|..|..|..|..
..|..|..|..|..|..
..|..|..|..|..|..
--+--+--+--+--+--
..|..|..|..|..|..
..|..|..|..|..|..
..|..|..|..|..|..
*/




#include<iostream>

using namespace std;

void printgrid(int row, int column, int height, int width){
    char dot = '.';
    char pipe = '|';
    char plus = '+';
    char minus = '-';
    int recurrencerow = 1;
    int recurrencecolumn = 1;
    for(int i=0;i<row;i++){
        for(int j=0;j<column;j++){
            if((j%(width+1)==width||i%(height+1)==height)&&recurrencerow!=0){
                cout << pipe;
            }
            else if(recurrencerow==0&&recurrencecolumn==0){
                cout << plus;
            }
            else if(recurrencerow==0){
                cout << minus;
            }
            else{
                cout << dot;
            }
            recurrencecolumn++;
            recurrencecolumn = recurrencecolumn%(width+1);
        }
        recurrencecolumn = 1;
        recurrencerow++;
        
        recurrencerow = recurrencerow%(height+1);
         if(i!=row-1)
            cout << "\n";
    }
}

int main(){
    int testcases, r, c, h, w;
    cin >> testcases;
    for(int i=0; i<testcases; i++){
        cin >> r >> c >> h >> w;
        printgrid((r+1)*h + r, (c+1)*w + c, h, w); //Modify r and c to get the total rows and columns in the grid
        if(i!=testcases-1)
            cout << "\n\n";
    }

    return 0;
}