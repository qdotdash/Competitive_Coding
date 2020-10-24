#include<bits/stdc++.h>

using namespace std;

int dec_to_bin(int n){
	long long int binary_number = 0;
	int rem = 0;
	int counter = 0;
	while(n!=0){
		rem = n%2;
		binary_number += rem*pow(10,counter);
		n /= 2;
		counter++;
	}
	return binary_number;	
}

int main(){
	int n;
	cin >> n;
	cout << dec_to_bin(n);
}