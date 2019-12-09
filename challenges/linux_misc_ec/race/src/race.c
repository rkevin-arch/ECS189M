#include <stdio.h>
#include <unistd.h>
int main(int argc, char** argv){
    if(argc!=2){
        printf("Usage: %s [filename]\nPrints the contents of the file\n",argv[0]);
        return 1;
    }
    if(access(argv[1],R_OK)){
        printf("You do not have the permission to read the file %s!\n",argv[1]);
        return 1;
    }
    setgid(getegid());
    execl("/bin/cat","/bin/cat",argv[1],NULL);
}
