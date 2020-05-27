#include<bits/stdc++.h>

using namespace std;

int main(){
    
    int arr[100];
    int limit;
    cout << "Enter limit : ";
    cin >> limit;
    cout << "\n";
    for(int i=0; i<limit; i++){
        cin >> arr[i];
    }

    cout << "\n";

    cout << "1 : O(n3)\n2 : O(n2)\n3 : O(n)\n";
    int choice;
    cin >> choice;
    int maximum = 0;

    if(choice==1){
        for(int i=0; i<limit; i++){
            for(int j=i; j<limit; j++){
                int sum = 0;
                for(int k=i; k<=j; k++){
                    sum = sum + arr[k];  
                    maximum = max(sum, maximum);
                }
            }
        }

        cout << maximum;
    }

    if(choice==2){
        for(int i=0; i<limit; i++){
            int sum = 0;
            for(int j=i; j<limit; j++){
                sum = sum + arr[j];
                maximum = max(sum, maximum);
            }
        }

        cout << maximum;
    }

    if(choice==3){
        int sum=0;
        for(int i=0; i<limit; i++){
            sum = sum + arr[i];
            sum = max(arr[i], sum);
            maximum = max(maximum, sum);
        }

        cout << maximum;
    }



}