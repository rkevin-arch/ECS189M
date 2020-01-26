#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <err.h>
#include <errno.h>
int main(){
    puts("Hey there!");
    puts("Give me the input 'Open Sesame' and I'll give you the flag!");
    int flags=fcntl(0,F_GETFL);
    if(flags<0)
        err(1,"Get stdin flags failed! This should never happen. Contact Kevin.");
    if(fcntl(0,F_SETFL,flags|O_NONBLOCK)==-1)
        err(1,"Set stdin flags failed! This should never happen. Contact Kevin.");
    char input[15];
    size_t n=read(0,input,15);
    if(n==-1 && errno==EAGAIN){
        puts("I didn't get any input. Closing.");
        return 0;
    }
    if(n==-1)
        err(1,"Read stdin failed! This should never happen. Contact Kevin.");
    input[n]='\0';
    char* eol=strchr(input,'\n');
    if(eol)
        *eol='\0';
    if(!strcmp("Open Sesame",input))
        puts("Your flag is: ECS{D00R_W1D3_0P3N_70B35DC02FD4F609EF7B76AC3875C5CE}");
    else{
        puts("Your input was incorrect!");
        //puts(input);
    }
    return 0;
}
