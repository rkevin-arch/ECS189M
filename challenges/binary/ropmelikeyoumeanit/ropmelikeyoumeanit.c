#include <stdio.h>

//gcc -fno-pie -no-pie -Wno-implicit-function-declaration -fno-stack-protector ropmelikeyoumeanit.c -static -o ropmelikeyoumeanit

int vuln(){
    char buf[16];
    gets(buf);
    return 0;
}

int main(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    puts("Gimme some data!");
    fflush(stdout);
    vuln();
    puts("Failed... :(");
}
