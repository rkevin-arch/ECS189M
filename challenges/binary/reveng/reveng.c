#include <stdio.h>
#include <string.h>

//gcc reveng.c -o reveng

//ECS{R00T_C4U53_EA397D13A6CFBF355207E69631C51D6E}
int validate(char* flag){
    int stored[]={69, 67, 83, 123, 74, 40, 40, 76, 71, 91, 44, 77, 45, 43, 71, 93, 89, 43, 33, 47, 92, 41, 43, 89, 46, 91, 94, 90, 94, 43, 45, 45, 42, 40, 47, 93, 46, 33, 46, 43, 41, 91, 45, 41, 92, 46, 93, 125};
    int key,len,i;
    len=48;
    i=0;
    key=0;
    if(strlen(flag)!=len) return 0;
    while(1){
        if(len<=i) break;
        key+=stored[i];
        i+=1;
    }
    key&=0xFF;
    i=0;
    do {
        if (48<=i){
            return 1;
        }
        if (i<4 || i==47){
            if((int)flag[i]!=stored[i]){
                return 0;
            }
        } else {
            if((int)flag[i]!=(stored[i]^key)){
                return 0;
            }
        }
        i++;
    } while(1);
}

int main(){
    char flag[100];
    printf("Enter your guess for the flag: ");
    fflush(stdout);
    scanf("%90s",flag);
    if(validate(flag))
        puts("That's it! That's the flag!");
    else
        puts("That wasn't right. Better luck next time?");
    return 0;
}
