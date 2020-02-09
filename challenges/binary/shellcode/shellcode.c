#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//gcc shellcode.c -z execstack -o shellcode

unsigned char code[500];

int main(){

    setbuf(stdin,NULL);
    setbuf(stdout,NULL);

    puts("I'll execute any shellcode you may have!");
    puts("How big is your shellcode?");
    char size_str[10];
    fgets(size_str, 10, stdin);
    int size = atoi(size_str);
    if(size>500 || size<1){
        puts("Invalid size for shellcode!");
        return 1;
    }
    puts("Give me your shellcode now!");
    read(STDIN_FILENO, code, size);
    ((void(*)())code)(); //run shellcode
    return 0;
}
