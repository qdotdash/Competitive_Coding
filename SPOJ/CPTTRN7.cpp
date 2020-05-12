/*
the starting postition of the / is given by size/2 and then size + 2 progression 

Output :
3
3 1 2
4 4 1
2 5 2

./\.
/..\
\../
.\/.
./\.
/..\
\../
.\/.
./\.
/..\
\../
.\/.

/\/\/\/\
\/\/\/\/
/\/\/\/\
\/\/\/\/
/\/\/\/\
\/\/\/\/
/\/\/\/\
\/\/\/\/

./\../\../\../\../\.
/..\/..\/..\/..\/..\
\../\../\../\../\../
.\/..\/..\/..\/..\/.
./\../\../\../\../\.
/..\/..\/..\/..\/..\
\../\../\../\../\../
.\/..\/..\/..\/..\/.



    

*/



#include<iostream>

using namespace std;

void printgrid(int row, int column, int size){
    char dot = '.';
    char forwardslash = '/';
    char backslash = '\\';  
    int fspos = size/2;
    int fspostemp = fspos;
    int bspos = size/2 + 1;
    int bspostemp = bspos;
    int addpos = size + 2;
    char sign1 = forwardslash;
    char sign2 = backslash;
    int firsthalf = true;

    for(int i=0; i<row; i++){
        for(int j=0; j<column; j++){
            if(j==fspostemp){
                cout << sign1;
                fspostemp = fspostemp + addpos;
            }
            else if(j==bspostemp){
                cout << sign2;
                bspostemp = bspostemp + addpos;
            }
            else{
                cout << dot;
            }

        }
        if(fspos==0&&sign1==forwardslash){
            firsthalf=false;
            sign2 = forwardslash;
            sign1 = backslash;
            fspos--;
            bspos++;
        }
        else if(fspos==size/2&&i!=0&&sign1==backslash){
            firsthalf=true;
            sign1 = forwardslash;
            sign2 = backslash;
            fspos++;
            bspos--;
        }

        if(firsthalf){
            fspos = fspos-1;
            bspos = bspos+1;
            fspostemp = fspos;
            bspostemp = bspos;
        }
        else{
            fspos = fspos+1;
            bspos = bspos-1;
            fspostemp = fspos;
            bspostemp = bspos;
        }
        if(i!=row-1)
            cout << "\n";
    }
}

int main(){
    int testcases, r, c, s;
    cin >> testcases;
    for(int i=0; i<testcases;i++){
        cin >> r >> c >> s;
        s = s * 2  - 2; //converting the number of lines in diamond input to width in my program
        printgrid(r*(s+2), c*(s+2), s);
        if(i!=testcases-1)
            cout << "\n\n";
    }
}