#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <dirent.h>
#include <errno.h>
#include <fcntl.h>
char* FIRST_FLAG="placeholder_first_flag";

void print_menu(){
    puts("=================================");
    puts("|        Missile Control        |");
    puts("=================================");
    puts("|                    |    /\\    |");
    puts("|  1. Arm missile    |   /  \\   |");
    puts("|  2. Disarm missile |   |  |   |");
    puts("|  3. View changelog |   |  |   |");
    puts("|  4. Exit           |  / == \\  |");
    puts("|                    |  |/**\\|  |");
    puts("=================================");
}

void print_changelog(){
    DIR *dirp=opendir("changelog/");
    if(dirp==NULL){
        puts("No entries in changelog!");
        return;
    }
    puts("The following changelogs are found:");
    struct dirent *ent;
    while(ent=readdir(dirp)){
        if(ent->d_type==DT_REG)
            puts(ent->d_name);
    }
    closedir(dirp);
    puts("Which changelog should be shown?");
    char buf[1024]="changelog/";
    scanf("%s",buf+strlen(buf));
    int fd=open(buf,O_RDONLY);
    if(fd==-1){
        printf("Error: %s\n",strerror(errno));
        return;
    }
    int n;
    while(n=read(fd,buf,1024),n>0)
        write(STDOUT_FILENO,buf,n);
    close(fd);
    return;
}
int main(){
    print_menu();
    puts("Which option do you want to choose?");
    while(1){
        switch(getchar()){
            case '1':
                puts("The missile is already armed!");
                break;
            case '2':
                puts("You aren't allowed to make that change!");
                break;
            case '3':
                print_changelog();
                break;
            case '4':
            case EOF:
                return 0;
            default:
                continue;
        }
        puts("Which option do you want to choose?");
    }
}
