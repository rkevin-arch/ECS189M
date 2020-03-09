#include <stdio.h>
#include <string.h>

//gcc -fno-pie -no-pie disable_missile.c -o disable_missile

char translation_table[64] = {48, 44, 1, 17, 29, 6, 9, 13, 36, 63, 2, 62, 18, 16, 53, 7, 27, 43, 50, 24, 46, 56, 37, 31, 41, 59, 52, 38, 19, 8, 4, 14, 39, 55, 49, 25, 28, 3, 54, 47, 23, 5, 34, 42, 0, 12, 60, 57, 51, 20, 32, 21, 33, 30, 45, 10, 22, 11, 35, 58, 15, 40, 26, 61};

int validate(char* code){
    //05 36 12.81335 -01 12 06.9089
    int secrets[]={3509, 13552, 70227, 3146, 90000, 48600, 59823, 33462, 21504, 8000, 28899, 7200, 44217, 2304, 22815, 12600, 5733, 5292, 4400, 4840, 32400, 8192, 2800, 9126, 10125, 1764, 4563, 1800, 2601};
    if(strlen(code)!=29)
        return 0;
    for(int i=strlen(code)-1;i>=0;i--){
        if(code[i]>=64)
            return 0;
        if(translation_table[code[i]]*translation_table[code[i]]*(i+1)!=secrets[strlen(code)-1-i])
            return 0;
    }
    return 1;
}

void print_flag(){
    FILE* f=fopen("/flag","r");
    char flag[100];
    if(!f){
        puts("I would have given you the flag, but I can't open the file.");
        puts("Try entering the same code on twinpeaks to get your flag.");
        return;
    }
    fgets(flag,100,f);
    puts(flag);
}

int main(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    char secretcode[100];
    puts("Enter the right code to force disable the missile launch.");
    fgets(secretcode,100,stdin);
    if(secretcode[strlen(secretcode)-1]=='\n')
        secretcode[strlen(secretcode)-1]='\0';
    if(validate(secretcode)){
        puts("Missile disabled.");
        print_flag();
        return 0;
    }
    puts("Code validation failed.");
    return 0;
}
