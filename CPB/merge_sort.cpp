#include<bits/stdc++.h>

using namespace std;

void merge(int arr[100], int l, int m, int r){
    int i = 0, j = 0;
    int k = l;

    int left[m-l+1], right[r-m];

    for(int f=0; f<m-l+1; f++){
        left[f] = arr[k];
        k++;
    }

    for(int g=0; g<r-m; g++){
        right[g] = arr[k];
        k++;
    }

    k = l;
    while(i < m-l+1 && j < r-m){
        if(left[i] < right[j]){
            arr[k] = left[i];
            i++;
            k++;
        }
        else{
            arr[k] = right[j];
            j++;
            k++;
        }
    }
    while(i < m-l+1){
        arr[k] = left[i];
        i++;
        k++;
    }
    while(j < r-m){
        arr[k] = right[j];
        j++;
        k++;
    }
}

void mergesort(int arr[100], int l, int r){
    if(l<r){
        int mid = (l + r)/2;

        mergesort(arr, l, mid);
        mergesort(arr, mid+1, r);
        merge(arr, l, mid, r);
    }
}

int main(){
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    for(int i=0; i<n; i++){
         cout << arr[i] << " ";
    }

    mergesort(arr, 0, n-1);

    cout << "\n\n";

    for(int i=0; i<n; i++){
         cout << arr[i] << " ";
    }
}