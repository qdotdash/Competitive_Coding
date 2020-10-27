#include<bits/stdc++.h>
#include<time.h>

using namespace std;

int main(){
  clock_t start, end;
  long long int size = 100000000;
  //time1 = clock();
  start = clock();

  for(int i=0; i<size; i++){
  	//do nothing but wait
  }

  end = clock();
  //time2 = clock();
  double time_taken = double(end-start)/double(CLOCKS_PER_SEC);
  cout << "\nElapsed time : " << fixed << time_taken;
}