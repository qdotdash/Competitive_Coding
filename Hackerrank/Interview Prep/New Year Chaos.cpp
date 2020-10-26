//Minimum bribes to get the final state of the queue

#include<bits/stdc++.h>

using namespace std;

void printarray(int *arr, int size){
	for(int i=0; i<size; i++){
		cout << arr[i] << " ";
	}
	cout << "\n";
}


void swap(int *arr, int i, int j){
	int temp = arr[i];
	for(int m=i; m<j; m++){
		arr[m] = arr[m+1];
	}
	arr[j] = temp;
}


int main(){
	int testcase, queue_final[100000], inputs;

	cin >> testcase;

	while(testcase--){
		cin >> inputs;
		for(int i=0; i<inputs; i++)
			cin >> queue_final[i];

		int flag = 0;
		int bribe = 0;

		for(int i=inputs-1; i>=0; i--){
			if(queue_final[i]!=(i+1)){
				if(queue_final[i-1]==(i+1)){
					bribe += 1;
					swap(queue_final, i-1, i);
					//printarray(queue_final, inputs);
				}
				else if(queue_final[i-2]==(i+1)){
					bribe += 2;
					swap(queue_final, i-2, i);
					//printarray(queue_final, inputs);
				}
				else{
					flag = 1;
					break;				}
			}

		}
		//printarray(queue_final, inputs);

		if(flag){
			cout << "Too chaotic";
		}
		else{
			cout << bribe;
		}
		if(testcase!=0)
			cout << "\n";
	}


}