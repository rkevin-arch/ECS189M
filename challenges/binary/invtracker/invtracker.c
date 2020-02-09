#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//gcc -fno-pie -no-pie -m32 invtracker.c -o invtracker

char mode[128];

struct Entry{
    int itemcount;
    char* description;
};

#define MAX_ENTRY_COUNT 99
#define MAX_DESCRIPTION_LEN 128

struct Entry* entries[MAX_ENTRY_COUNT+1];
int entrycount=0;


void createEntry(){
    struct Entry *entry=malloc(sizeof(struct Entry));
    char buf[MAX_DESCRIPTION_LEN];
    if(entrycount>=99){
        printf("You have way too many entries!");
        return;
    }
    puts("Enter number of items: ");
    scanf(" %d",&(entry->itemcount));
    puts("Enter item description: ");
    getc(stdin); //eat newline for fgets
    fgets(buf, MAX_DESCRIPTION_LEN, stdin);
    entry->description=malloc(strlen(buf));
    buf[strlen(buf)-1]='\0'; //remove newline
    strcpy(entry->description,buf);
    entrycount++;
    entries[entrycount]=entry;
}

void printEntries(){
    printf("Number of entries: %d\n",entrycount);
    printf("ID\tCount\tDescription\n");
    for(int i=1;i<=entrycount;i++)
        printf("%d\t%d\t%s\n",i,entries[i]->itemcount,entries[i]->description);
}

void changeItemDescription(){
    int id;
    char buf[MAX_DESCRIPTION_LEN];
    puts("Enter entry ID for which you would like to update: ");
    scanf(" %d",&id);
    if(id<1 || id>entrycount){
        puts("Invalid ID.");
        return;
    }
    puts("Enter new item description: ");
    getc(stdin); //eat newline for fgets
    fgets(buf, MAX_DESCRIPTION_LEN, stdin);
    if(strlen(buf)>strlen(entries[id]->description)){
        free(entries[id]->description);
        entries[id]->description=malloc(strlen(buf));
    }
    buf[strlen(buf)-1]='\0'; //remove newline
    strcpy(entries[id]->description,buf);
}

void updateItemCount(){
    int id;
    puts("Enter entry ID for which you would like to update: ");
    scanf(" %d",&id);
    if(id<1 || id>entrycount){
        puts("Invalid ID.");
        return;
    }
    puts("Enter new item count: ");
    scanf(" %d",&(entries[id]->itemcount));
}

void deleteEntry(){
    int id;
    puts("Enter entry ID for which you would like to update: ");
    scanf(" %d",&id);
    if(id<1 || id>entrycount){
        puts("Invalid ID.");
        return;
    }
    free(entries[id]->description);
    free(entries[id]);
    //TODO: remove entry from entries list
}

void admin(){
    if(strcmp(mode, "DEBUG")!=0){
        puts("You must be in DEBUG mode to use this command.");
        printf("Current mode is %s, and the mode is stored at %p.\n",mode,mode);
        return;
    }
    puts("Welcome back, admin!");
    system("/bin/sh");
    exit(0);
}

void menu(){
    char choice='\0';
    puts("----------------MAIN MENU----------------");
    puts("[A]dd a new entry");
    puts("[P]rint all entry information");
    puts("[C]hange item description");
    puts("[U]pdate item count");
    puts("[D]elete entry");
    puts("[E]nter admin mode");
    puts("[Q]uit");
    puts("Enter your selection: ");
    scanf(" %c",&choice);
    switch(choice){
        case 'A':
            createEntry();
            break;
        case 'P':
            printEntries();
            break;
        case 'C':
            changeItemDescription();
            break;
        case 'U':
            updateItemCount();
            break;
        case 'D':
            deleteEntry();
            break;
        case 'E':
            admin();
            break;
        case 'Q':
            exit(0);
            break;
        case '\n':
        case ' ':
            break;
        default:
            puts("Unrecognized option. Try again?");
            break;
    }
}

int main(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    strcpy(mode,"PRODUCTION");
    puts("Welcome to our advanced inventory tracker!");
    puts("Here, you can keep track of how many items you have!");
    while(1)
        menu();
}
