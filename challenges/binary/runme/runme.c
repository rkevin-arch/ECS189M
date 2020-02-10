#include <stdio.h>
#include <stdlib.h>

//gcc -fno-pie -no-pie runme.c -o runme

char* getflag(){
    char* flagarr=malloc(57);
    flagarr[0]='E';
    flagarr[1]='C';
    flagarr[2]='S';
    flagarr[3]='{';
    flagarr[4]='T';
    flagarr[5]='H';
    flagarr[6]='3';
    flagarr[7]='R';
    flagarr[8]='3';
    flagarr[9]='_';
    flagarr[10]='1';
    flagarr[11]='5';
    flagarr[12]='_';
    flagarr[13]='N';
    flagarr[14]='0';
    flagarr[15]='_';
    flagarr[16]='3';
    flagarr[17]='5';
    flagarr[18]='C';
    flagarr[19]='4';
    flagarr[20]='P';
    flagarr[21]='3';
    flagarr[22]='_';
    flagarr[23]='8';
    flagarr[24]='C';
    flagarr[25]='3';
    flagarr[26]='9';
    flagarr[27]='F';
    flagarr[28]='7';
    flagarr[29]='C';
    flagarr[30]='E';
    flagarr[31]='6';
    flagarr[32]='2';
    flagarr[33]='8';
    flagarr[34]='3';
    flagarr[35]='4';
    flagarr[36]='9';
    flagarr[37]='9';
    flagarr[38]='E';
    flagarr[39]='6';
    flagarr[40]='8';
    flagarr[41]='F';
    flagarr[42]='D';
    flagarr[43]='6';
    flagarr[44]='F';
    flagarr[45]='4';
    flagarr[46]='8';
    flagarr[47]='5';
    flagarr[48]='6';
    flagarr[49]='A';
    flagarr[50]='9';
    flagarr[51]='5';
    flagarr[52]='A';
    flagarr[53]='9';
    flagarr[54]='4';
    flagarr[55]='}';
    flagarr[56]='\0';
    return flagarr;
}

int main(){
    puts("Thanks for running this program!");
    puts("Unfortunately, the flag you're looking for is in another castle.");
    return 0;
}
