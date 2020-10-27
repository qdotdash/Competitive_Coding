#include<bits/stdc++.h>

using namespace std;

double birthdayProbability(int number){
	double probability = 1;
	for(int i=1; i<number; i++){
		probability = probability*(365-i)/365;
	}
	probability = 1 - probability;
	return probability;
}

int main(){
	int number;
	double probability_of_collision;
	cin >> number;
	probability_of_collision = birthdayProbability(number);
	cout << "Probability of having a birthday collision in " << number << " people : " << fixed << probability_of_collision;
}