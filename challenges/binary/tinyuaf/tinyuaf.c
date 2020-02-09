#include <stdio.h>
#include <stdlib.h>

//gcc -fno-pie -no-pie tinyuaf.c -o tinyuaf

int isWinner = 0;
struct Lame {
    int x;
} Lame;

struct Uaf
{
    int * x;
} Uaf;

int main() {
   setbuf(stdin,NULL);
   setbuf(stdout,NULL);
   struct Uaf * currentStruct = malloc(sizeof(struct Uaf));
   free(currentStruct);
   struct Lame * lameStruct = malloc(sizeof(struct Lame));
   while(!isWinner) {
      printf("You aren't an admin. What would you like to do?\n");
      printf("Admin variable address: %p\n", (void *) &isWinner);
      printf("Admin: %d\n", isWinner);
      int choice = 0;
      scanf("%d", &choice);
      switch(choice) {
         case 0:
            scanf("%d", &(lameStruct->x));
            break;
         case 1:
            *(currentStruct->x) = 1;
            break;
         default:
            break;
      }
   }
   printf("Welcome, admin!\n");
   system("/bin/sh");
}

