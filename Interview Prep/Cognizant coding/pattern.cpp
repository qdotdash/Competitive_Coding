#include<bits/stdc++.h>

using namespace std;

void pattern(int n){
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++){
			if(i==0||j==0||i==n-1||j==n-1){
				cout << "1";
			}
			else{
				cout << " ";
			}
			
		}
		if(i!=n-1){
		cout << "\n";
	}
	}
}

int main(){
	int n;
	cin >> n;
	pattern(n);
}