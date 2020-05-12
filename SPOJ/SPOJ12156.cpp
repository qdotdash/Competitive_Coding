#include<iostream>

using namespace std;

int main(){
    char line[210];
    int test_cases;
    cin >> test_cases; //when the number is read the cursor is at the same line,
                       //if not moved getline reads blank spaces
    cin.getline(line, 100); //to move the input to next line
    for(int i=0;i<test_cases;i++){
        int array_length,k=0;
        fflush(stdin);
        cin.getline(line, 205);
        while(line[k]!='\0')
            k++;
        array_length = k;
        for(int j=0;j<array_length/2;j++){
            if(j%2==0)
                cout << line[j];
                
        }
        if(i!=test_cases-1)
            cout  << "\n";
    }
    return 0;
}