#include <stdio.h>
#include <string.h>

//gcc -fno-pie -no-pie trace.c -o trace

int main(){
    char flag[200];
    //ECS{C0NT41N5_TR4C35_0F_NUT5_CFB3076617138AD73D982181DF99C0B4}
    char trueflag[62]={24, 39, 25, 104, 13, 37, 29, 46, 43, 3, 30, 12, 82, 57, 76, 45, 41, 4, 53, 45, 11, 60, 43, 35, 54, 29, 36, 35, 31, 54, 45, 12, 34, 20, 14, 32, 7, 37, 24, 27, 12, 50, 12, 53, 31, 65, 0, 51, 46, 20, 24, 41, 9, 19, 23, 27, 55, 25, 13, 19, 124};
    int nextloc[]={9, 49, 52, 44, 25, 56, 19, 31, 21, 17, 6, 36, 32, 1, 15, 51, 13, 10, 60, 53, 7, 5, 58, 40, 50, 42, 37, 27, 20, 26, 35, 34, 41, 28, 11, 57, 23, 3, 16, 38, 0, 29, 46, 45, 30, 48, 2, 14, 47, 55, 59, 8, 27, 22, 33, 24, 12, 39, 4, 54, 43};
    puts("Enter your guess for the flag!");
    fgets(flag, 200, stdin);
    char* pos=strchr(flag,'\n');
    if(pos)
        *pos='\0';

    int loc=18;
    for(int key=0;key<61;key++){
        trueflag[loc]+=key;
        loc=nextloc[loc];
    }

    if(strcmp(flag,trueflag))
        puts("Incorrect, try again.");
    else
        puts("That's it! That's the flag!");
    return 0;
}
