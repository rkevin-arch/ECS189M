#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
int main(){
    raise(SIGSTOP);
    if(system("[ `/bin/grep ^/usr/local/bin/incorrect /proc/*/cmdline | /usr/bin/wc -l` -eq 4 ]")){
        puts("Don't try to trick the system! Follow the prompt!");
        puts("If you're seeing this message when you didn't do anything bad, please let me know.");
        return 1;
    }
    puts("You did it! Run `answer 7` again if this is the last challenge you need to solve.");
    if(close(open("/tmp/qaframework/45fd98f0038fcdd95dc182a3e5d37f36",O_WRONLY|O_CREAT,S_IRUSR|S_IWUSR)))
        puts("WARNING: Write challenge progress failed! This should never happen.");
}
