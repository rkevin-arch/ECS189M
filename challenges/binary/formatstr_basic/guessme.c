#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define MAX_INPUT 1024

unsigned int securerandomnumber(){
    char randdata[sizeof(int)];
    int fd=open("/dev/urandom", O_RDONLY);
    if(fd<0){
        puts("Something went wrong, try again? Sorry.");
        exit(1);
    }
    if(read(fd,randdata,sizeof(int))<0){
        puts("Something went wrong, try again? Sorry.");
        exit(1);
    }
    close(fd);
    return *(int*)randdata;
}
int main(){
    unsigned int inputint;
    char input[MAX_INPUT];
    unsigned int secret=securerandomnumber();
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    puts("Welcome to our limited terminal!");
    puts("For help, enter 'help'.");
    while(1){
        fgets(input, MAX_INPUT, stdin);
        if(strstr(input,"help")==input){
            puts("The following commands are available:");
            puts("help: Prints out this message.");
            puts("echo [YOURSTRING]: Prints out YOURSTRING.");
            puts("shell: Get a shell.");
        } else if(strstr(input,"echo ")==input){
            printf(&(input[5])); //the 5 is to remove the "echo" in the front
        } else if(strstr(input,"shell")==input){
            puts("To verify your identity, tell me the secret:");
            scanf("%u",&inputint);
            if(inputint!=secret){
                puts("Access denied! Get outta here!");
                exit(0);
            }
            puts("Welcome back, admin!");
            system("/bin/bash");
            exit(0);
        }
    }
}