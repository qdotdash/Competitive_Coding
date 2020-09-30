#include<stdio.h>
#include<stdlib.h>

int power(int num, int raisedto){
    int temp = num;
    for(int i=0; i<raisedto-1; i++)
        temp *= num;
    return temp;
}

int digitCount(int num){
    int digitcount = 0;
    if(num==0){
        return 1;
    }
    else{
        int temp = num;
        while(temp>=1){
            temp = temp/10;
            digitcount++;
        }
        return digitcount;
    }
}

void isArmstrong(int num){
    if(num==0){
        printf("Is Armstrong");
    }
    else{
        int temp = num;
        int sum = 0;
        while(temp>=1){
            sum = sum + power(temp%10, digitCount(num));
            temp = temp/10;
        }
        if(sum==num){
            printf("Is Armstrong");
        }
        else{
            printf("Not Armstrong");
        }
    }
}

void main(){
    int testcase;
    scanf("%d", &testcase);
    isArmstrong(testcase);
}