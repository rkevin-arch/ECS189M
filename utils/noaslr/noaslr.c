#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/personality.h>
#include <errno.h>

// This program is used for the memory corruption challenges
// to ensure a uniform stack. This disables ASLR and destroys
// all environment variables to make sure the stack addresses
// never change. To use, run ./noaslr ./program_you_want_to_run

//To compile this, just do gcc noaslr.c -o noaslr

int main(int argc,char** argv)
{
    if (argc<2){
        puts("Usage: noaslr PROGRAM [args]");
        exit(1);
    }
    unsigned int personality_flags=personality(0xffffffff);
    if(!(personality_flags&ADDR_NO_RANDOMIZE)){
        personality(personality_flags|ADDR_NO_RANDOMIZE);
    }
    execve(argv[1],argv+1,NULL);
}
