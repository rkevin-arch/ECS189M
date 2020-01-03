#!/usr/bin/python3
'''
- What's your cwd?
- Determine filesize and modification date
- Whether a given user and group can access the file?
- Use /etc/groups and /etc/passwd to determine others that can access file
- Determine filetype (use no/renamed/fake extension)
- Chown so that given a usecase of users and group to have access.
- Find a certain command using apropos
- Find the argument given an option.
'''
import os
import sys
import datetime
import stat

class COLORS:
    PURPLE = '\033[95m%s\033[0m'
    BLUE   = '\033[94m%s\033[0m'
    GREEN  = '\033[92m%s\033[0m'
    YELLOW = '\033[93m%s\033[0m'
    EMPHASIS = '\033[1m\033[4m'

FLAG="ECS{3X4M1N3_3XTR4CT_3XTR4P0L4T3_3A7FB33B1BE13E7AC844524F94C4A6EE}"

class Challenge:
    def __init__(self,handler,secret):
        self.handler=handler
        self.secret=secret
    def solved(self):
        return os.access("/tmp/qaframework/%s"%self.secret,os.F_OK)

class SimpleChallenge(Challenge):
    def __init__(self,question,answer,secret):
        self.question=question
        self.answer=answer
        self.secret=secret
    def handler(self):
        while True:
            print(COLORS.BLUE%self.question)
            useranswer=input().strip()
            if useranswer==self.answer:
                return
            print(COLORS.YELLOW%"Sorry that's wrong, try again!")

CONFIG={
"1": SimpleChallenge("How many lines are in access.log?",
                     "3277",
                     "2846fc7605602d66ac1225b6de34d663"),
"2": SimpleChallenge("Using access.log, which IP tried to find information about Siemens?",
                     "37.49.231.173",
                     "275e611ba25c9add10c938da1829f942"),
"3": SimpleChallenge("Using access.log, how many requests claim to be from a Windows 10 machine?",
                     "224",
                     "a103aabc27dda38d93c5d98edd513820"),
"4": SimpleChallenge("Using access.log, how many unique IP made requests to the server?",
                     "485",
                     "41f9c5abbc3dc1fd762b6b8ddf4aea78"),
"5": SimpleChallenge("Using access.log, which IP made the most requests to the webserver?",
                     "203.57.230.249",
                     "22699faecf05a422fae754349db72d4d"),
"6": SimpleChallenge("Using auth.log, which IP is the most common in the file?",
                     "185.153.196.22",
                     "55b79d83e74a84a78c5fa9cdcee690e9"),
"7": SimpleChallenge("Find the right flag in flags.txt. The flag should look like `ECS{START_TAIL}`, where `START` only contains uppercase letters, numbers and underscores. `TAIL` is 32 characters long and only contains numbers and the upper case letters A-F. There should be no characters before or after the flag.",
                     "ECS{N33DL3_1N_H4YST4CK_04DBD988295DB3B86097037AEE270C28}",
                     "134e52abb8a44fb579d8eb284ebc3be1")
}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in CONFIG:
        print("To use this tool: Run `answer x` to answer question x.\nThere are {0} questions in total, from 1 to {0}.".format(len(CONFIG)))
        sys.exit(1)
    challenge=CONFIG[sys.argv[1]]
    if not challenge.solved():
        challenge.handler()
        os.mknod("/tmp/qaframework/%s"%challenge.secret)
    else:
        print(COLORS.YELLOW%"You already solved this challenge!")

    unsolved=[]
    for k,v in CONFIG.items():
        if not v.solved():
            unsolved.append(k)
    if len(unsolved)==0:
        print(COLORS.GREEN%("You did it! The flag is "+COLORS.EMPHASIS+FLAG+"."))
    else:
        print(COLORS.PURPLE%("You solved {0} out of {1} challenges! The challenge{3} {2} remain.".format(
                len(CONFIG)-len(unsolved),len(CONFIG),", ".join(unsolved),"" if len(unsolved)==1 else "s")))

if __name__=="__main__":
    main()
