#include<iostream>

using namespace std;

const int MAX = 100000;

void factorial(int num){
    int size_of_array = 0;
    int res[MAX];
    int temp = num;
    int iter = 0;


    while(temp>0){
        res[iter] = temp%10;
        size_of_array++;
        temp = temp/10;
        iter++;
    }

    int temp_size_of_array = size_of_array;
    for(int i=num-1; i>=2; i--){
        int carry = 0;
        for(int j=0; j<size_of_array; j++){
            int product = res[j] * i + carry;
            res[j] = product%10;
            carry = product/10;
            if(j==size_of_array-1&&carry>0){
                while(carry>0){
                    j++;
                    res[j] = carry%10;
                    carry = carry/10;
                }
                temp_size_of_array = j+1;
            } 
        }
        size_of_array = temp_size_of_array;

    }

    for(int m=size_of_array-1; m>=0; m--){
        cout << res[m];
    }
}



int main(){
    int num, tc;
    cin >> tc;
    while(tc--){
        cin >> num;
        factorial(num);
        if(tc!=0){
            cout << "\n";
        }
    }
}