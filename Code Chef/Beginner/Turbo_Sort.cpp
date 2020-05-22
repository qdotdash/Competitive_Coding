#include<iostream>

using namespace std;

const int ARRAY_SIZE = 100;

void shift(int &arr_size, int arr[ARRAY_SIZE], int index){
    for(int i = arr_size; i>index; i--){
        arr[i] = arr[i-1];
    }
}

void sort_into(int &arr_size, int num, int arr[ARRAY_SIZE]){

  int left = 0;
  int right = arr_size-1;
  int mid = (left + right)/2;
  bool flag = false;

  if(arr_size==0){
      arr[0] = num;
  }
  else{
      if(num >= arr[arr_size-1]){
          arr[arr_size] = num;
      }
      else if(num <= arr[0]){
          shift(arr_size, arr, 0);
          arr[0] = num;
      }
      else{
          while(left!=right){
              if(num==arr[mid]){
                 shift(arr_size, arr, mid);
                 arr[mid] = num;
                 flag = true;
                 break;
              }
              else if(num>arr[mid]){
                  left = mid+1;
                  mid = (left + right)/2;
              }
              else{
                  right = mid+1;
                  mid = (left + right)/2;
              }
          }
          if(flag=false){
            shift(arr_size, arr, left);
            arr[left] = num;
          }
      }
  }

    for(int i=0; i<arr_size+1; i++){
        cout << arr[i];
        if(i!=arr_size){
            cout << " ";
        }
    }

}



int main(){
    int num;
    int tc;
    int arr_size=0;
    int arr[ARRAY_SIZE];

    cin >> tc;

    while(tc--){
        cin >> num;
        sort_into(arr_size, num, arr);
        arr_size++;
    }

    
    
}