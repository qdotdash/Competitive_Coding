/*
Output

1
2 5 3
+++++++++++++++++++++           
+\..+../+\..+../+\..+
+.\.+./.+.\.+./.+.\.+
+..\+/..+..\+/..+..\+
+++++++++++++++++++++
+../+\..+../+\..+../+
+./.+.\.+./.+.\.+./.+
+/..+..\+/..+..\+/..+
+++++++++++++++++++++

Printed the border + and the rest with . -- now aiming for \.. in all the ELEMENTS.
Now for positions having  \, the value of j%(size+1) = i for the first element. this pattern
is maintained using the reccurence variable which resets when i becomes > 3. 
Using two flags flagfs and row_flagfs, I switch the forward and reverse slashes in each element.
row_flagfs resets after each row ELEMENT and flag_fs resets after each column flag ELEMENT


*/
#include<iostream>

using namespace std;

void printsymbol(int row, int column, int size){
    bool symbol_flag_star = true;
    char star = '*';
    char dot = '.';
    char backslash = '/';
    char forwardslash = '\\';
    int recurrencefs = 0;
    int recurrencebs = size+1;
    bool flagfs = true;
    bool row_flagfs = true;
    for(int i=0;i<row;i++){
        if(i%(size+1)==0&&i!=0) 
            row_flagfs = !row_flagfs;

        flagfs = row_flagfs;
       for(int j=0;j<column;j++){
            if(i==0||i==row-1||j==0||j==column-1||i%(size+1)==0||j%(size+1)==0)
                symbol_flag_star = true;
            else
                symbol_flag_star = false;   

            if(j%(size+1)==0&&j!=0){
                flagfs=!flagfs;
            }
            
            if(symbol_flag_star){
                cout << star;
           } 
            else{
                    if(j%((size+1))==recurrencefs&&flagfs){ 
                         cout << forwardslash;
                     }
                     else if(j%((size+1))==recurrencebs&&!flagfs){
                         cout << backslash;
                     }
                    else{
                        cout << dot;
                    }
                    
            }
       }
        recurrencefs++;
       recurrencefs = recurrencefs%(size+1);
        recurrencebs = size+1-recurrencefs;
       if(i!=row-1)
            cout << "\n";
   }
}

int main(){
   int test_cases, r, c, s;
   cin >> test_cases;
   for(int i=0;i<test_cases;i++){
       cin >> r >> c >> s;
       printsymbol(r*s+(r+1), c*s+(c+1), s); 
       if(i!=test_cases-1)
            cout << "\n\n";
   }
   return 0;
}