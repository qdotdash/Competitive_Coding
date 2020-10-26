#include<bits/stdc++.h>

using namespace std;

void swap(int *arr, int index1, int index2){
	int temp = arr[index1];
	arr[index1] = arr[index2];
	arr[index2] = temp;
}

void printarray(int *arr, int size){
	for(int i=0; i<size; i++)
		cout << arr[i] << " ";
}

int main(){
	int size;
	cin >> size;

	int arr[size];
	int swaps = 0;

	for(int i=0; i<size; i++)
		cin >> arr[i];
	
	for(int i=0; i<size; i++){
		while(arr[i]!=i+1){
			swap(arr, i, arr[i]-1);
			swaps++;
		}
	}
	//printarray(arr, size);
	cout << swaps;
}