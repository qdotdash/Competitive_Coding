#include<iostream>

using namespace std;
//Mission : to multiply two numbers in array

int main(){

    int arr1[200], arr2[200], arr3[200];
    int prod_arr[200];
    int flag[200];

    for(int i=0; i<200; i++){
        arr1[i] = arr2[i] = arr3[i] = flag[i] = -1;
        prod_arr[i] = 0;
    }


    int num1, num2;
    cin >> num1 >> num2;

    if(num1>num2){
        int temp = num2;    //Switching for multiplication
        num2 = num1;
        num1 = temp;
    }



    int indexvar=199;
    int tempvar = num1;
    while(tempvar!=0){
        arr1[indexvar] = tempvar%10;        //Extracting digits and assigining to array
        tempvar = tempvar/10;
        indexvar--;
    }
    indexvar = 199;
    tempvar = num2;
    while(tempvar!=0){
        arr2[indexvar] = tempvar%10;
        tempvar = tempvar/10;
        indexvar--;
    }



    //  for(int i=0; i<200; i++){
    //     if(arr2[i]!=-1)                     //Printing arr2
    //         cout << arr2[i];
    // }
    // cout << "\n";
    // for(int i=0; i<200; i++){
    //     if(arr1[i]!=-1)                     //Printing arr1
    //         cout << arr1[i];
    // }

    int multindex = 199;
    int number_of_zeroes = 0;

    for(int i=199; arr1[i]!=-1; i--){

        int carry = 0;

        for(int j=199; arr2[j]!=-1; j--){

            int product = 1; int ones = 0; int tens = 0;

            product = arr1[i] * arr2[j] + carry;
            
            if(arr2[j-1]==-1){

                if(product>9){
                    ones = product%10;
                    tens = product/10;
                    arr3[multindex] = ones;
                    multindex--;
                    arr3[multindex] = tens;
                    multindex--;
                }
                else{
                    arr3[multindex] = product;
                    multindex--;
                }
                flag[multindex + 1] = 2;
            }
            else{

                if(product>9){
                    ones = product%10;
                    tens = product/10;
                    arr3[multindex] = ones;
                    multindex--;
                    carry = tens;
                }
                else{
                    arr3[multindex] = product;
                    multindex--;
                    carry = 0;
                }
            }
        }

        number_of_zeroes++;
        if(arr1[i-1]!=-1){                  
            int tempzeroes = number_of_zeroes;
            while(tempzeroes--){                        //adding the place value zeroes
                arr3[multindex] = 0;
                multindex--;
            }
        }


    }   

    int sum_iteration = 0;
    int product_array_size = 0;
    for(int n = 199; n > multindex; n--){
        prod_arr[sum_iteration] = prod_arr[sum_iteration] + arr3[n];
        sum_iteration++;
         if(flag[n]==2){
             if(sum_iteration > product_array_size){
                 product_array_size = sum_iteration;
             }
            sum_iteration = 0;
        }
    }

    for(int f = 0; f < product_array_size; f++){
        
        if(prod_arr[f] > 9){
            int temp = prod_arr[f];
            prod_arr[f+1] = prod_arr[f+1] + temp/10;
            prod_arr[f] = temp%10;
        }
       
    }

    if(prod_arr[product_array_size]!=0){
        product_array_size++;
    }

    for(int f = product_array_size - 1; f >= 0; f--){
        for(int i=0; i<200; i++){
            arr1[i] = arr2[i] = arr3[i] = flag[i] = -1;
            prod_arr[i] = rem[i] = 0;
        }
    }


     

    // for(int m=185; m<200; m++){
    //         cout << arr3[m];
    //     }
    //     cout << "\n";
    // for(int m=185; m<200; m++){
    //         cout << flag[m];
    //     }

   


}   