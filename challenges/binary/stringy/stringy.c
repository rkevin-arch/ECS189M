#include <stdio.h>
#include <string.h>

//gcc -fno-pie -no-pie stringy.c -o stringy

int main(){
    char flag[200];
    puts("Enter your guess for the flag!");
    fgets(flag, 200, stdin);
    char* pos=strchr(flag,'\n');
    if(pos)
        *pos='\0';
    if(strcmp(flag,"ECS{5TR1NGY_81T_0F_TH3_80W_B82B2D82E38B6250566C342A817052CD}"))
        puts("Incorrect, try again.");
    else
        puts("That's it! That's the flag!");
    return 0;
}
