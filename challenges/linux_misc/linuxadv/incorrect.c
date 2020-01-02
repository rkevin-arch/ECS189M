#include <unistd.h>
#include <signal.h>
#include <stdio.h>
int main(){
    raise(SIGSTOP);
    puts("You didn't foreground the right process! Now you need to start again.");
    char* argv[]={"/usr/bin/pkill","-9","correct",NULL};
    execve(argv[0],argv,NULL);
    puts("execve failed! This should never happen. Contact Kevin immediately.");
}
