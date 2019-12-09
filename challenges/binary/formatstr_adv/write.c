#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 1024
int is_admin=0;

int main(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    char input[MAX_INPUT];
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
            if(is_admin==0){
                puts("You are not an admin!");
                printf("The is_admin variable at %p must be nonzero.\n", &is_admin);
            } else {
                puts("Welcome back, admin!");
                system("/bin/bash");
                exit(0);
            }
        }
    }
}
