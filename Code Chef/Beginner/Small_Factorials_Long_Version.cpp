#include<iostream>

using namespace std;

    
void multiply_two(int num1, int ar2[200]){
	
	
int arr1[200], arr2[200], arr3[200];
    int prod_arr[200];
    int flag[200];
    

    for(int i=0; i<200; i++){
        arr2[i] = ar2[i];
        arr1[i] = arr3[i] = flag[i] = -1;
        prod_arr[i] = 0;
    }

    int indexvar=199;
    int tempvar = num1;
    while(tempvar!=0){
        arr1[indexvar] = tempvar%10;        //Extracting digits and assigining to array
        tempvar = tempvar/10;
        indexvar--;
    }

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

    for(int i=0; i<200; i++){
        arr2[i] = -1;
        arr1[i] = arr3[i] = flag[i] = -1;
    }

    int iter = 199;
    for(int h=0; h<product_array_size; h++){
        
        arr2[iter] = prod_arr[h];
        iter--; 

    }


    if(num1==1){
        for(int g=0; g<200; g++){
           if(arr2[g]!=-1){
               cout << arr2[g];
           }
        }
    }
    else{
        multiply_two(num1-1, arr2);
    }

}



int main(){
    
    int num1, num2, arr[200];
    cin >> num1;
    num2 = num1;
    num1 = num1 - 1;

     for(int i=0; i<200; i++){
        arr[i] = -1;
    } 

    
    int indexvar = 199;
    int tempvar = num2;
    while(tempvar!=0){
        arr[indexvar] = tempvar%10;
        tempvar = tempvar/10;
        indexvar--;
    }

    multiply_two(num1, arr);

}   
