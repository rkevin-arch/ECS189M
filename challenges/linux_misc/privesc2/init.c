#define _GNU_SOURCE
#include <unistd.h>
#include <err.h>
#include <signal.h>
int main(int _dontcare, char** _dontcare2, char** orig_envp){
    pid_t p=fork();
    if(p){//parent, replace with bash
        if(setresuid(1337,1337,1337))
            err(1,"Parent setresuid failed! Please contact Kevin immediately.");
        char* argv[]={"/bin/bash",NULL};
        execve(argv[0],argv,orig_envp);
        err(1,"Parent execve failed! Please contact Kevin immediately.");
    }
    sigset_t set;
    sigfillset(&set);
    sigdelset(&set,SIGTERM);
    sigdelset(&set,SIGCHLD);
    if(sigprocmask(SIG_BLOCK, &set, NULL))
        err(1,"Child sigprocmask failed! Please contact Kevin immediately.");
    //child, replace with cron
    //if(setresgid(1338,1338,1338))
    //    err(1,"Child setresgid failed! Please contact Kevin immediately.");
    //if(setresuid(1338,1338,1338))
    //    err(1,"Child setresuid failed! Please contact Kevin immediately.");
    char* argv[]={"/usr/sbin/cron","-f",NULL};
    execve(argv[0],argv,argv+2);
    err(1,"Child execve failed! Please contact Kevin immediately.");
}
