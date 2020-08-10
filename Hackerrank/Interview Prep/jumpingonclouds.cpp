    #include<bits/stdc++.h>

    using namespace std;



    int main(){
        int clouds;
        cin >> clouds;
        int temp = clouds;
        int cloudsarr[clouds];
        int minsteps = 0;
        for(int i=0; i<temp; i++){
            cin >> cloudsarr[i];
        }

        temp = clouds;
        int i = 0;
    while(temp--&&i!=clouds-1){
            if(cloudsarr[i+2]==0){
                i = i + 2;
                minsteps++;
            }
            else{
                i = i + 1;
                minsteps++; 
            }
        }
        cout << minsteps;
    }