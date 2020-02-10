#include <stdio.h>

//gcc -fno-pie -no-pie xmem.c -o xmem

char flag[61];

int main(){
    puts("I'm going to decrypt the flag into memory...");
    //ECS{P3RP3TU4L_3PH3M3R4L1TY_E6A17148FCCFEC07C01D8EC92223539D}
    int secrets[]={69, 66, 87, 114, 64, 42, 118, 97, 115, 5, 49, 77, 220, 246, 247, 177, 72, 18, 9, 90, 194, 141, 168, 32, 20, 40, 251, 156, 38, 8, 181, 246, 49, 117, 188, 143, 83, 26, 226, 180, 3, 161, 211, 122, 160, 216, 0, 153, 69, 34, 253, 27, 162, 203, 87, 228, 115, 136, 96, 228, 16};
    for(int i=59;i>=0;i--)
        flag[i]=secrets[i]^(i*i%256);
    puts("Tada!");
    for(int i=0;i<61;i++)
        flag[i]='\0';
    puts("Whoops, the flag is now gone!");
}
