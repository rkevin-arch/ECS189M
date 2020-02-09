#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/random.h>

//gcc -fno-pie -no-pie -m32 guessme.c -Wno-format-security -o guessme

#define MAX_INPUT 1024

unsigned int securerandomnumber(){
    char randdata[sizeof(unsigned int)];
    getrandom(randdata,sizeof(unsigned int),0);
    return *(unsigned int*)randdata;
}
int main(){
    unsigned int inputsecret;
    unsigned int secret=securerandomnumber();
    char input[MAX_INPUT];
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    puts("Welcome to our limited terminal!");
    puts("For help, enter 'help'.");
    while(1){
        if(fgets(input, MAX_INPUT, stdin)==NULL) //EOF
            return 0;
        if(strstr(input,"help")==input){
            puts("The following commands are available:");
            puts("help: Prints out this message.");
            puts("echo [YOURSTRING]: Prints out YOURSTRING.");
            puts("shell: Get a shell.");
        } else if(strstr(input,"echo ")==input){
            printf(&(input[5])); //the 5 is to remove the "echo" in the front
        } else if(strstr(input,"shell")==input){
            puts("To verify your identity, tell me the secret:");
            scanf("%u",&inputsecret);
            if(inputsecret!=secret){
                puts("Access denied! Get outta here!");
                exit(0);
            }
            puts("Welcome back, admin!");
            system("/bin/bash");
            exit(0);
        }
    }
}
