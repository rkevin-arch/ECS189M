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

def chmodhandler():
    print(COLORS.BLUE%"Change the ownership and permissions of /home/user/chme, so that you have full read-write-execute permissions, jade and rose can read the file only, and john cannot read write or execute the file.")
    s=os.stat("/home/user/chme")
    if s.st_gid=="1337" and stat.S_IMODE(s.st_mode)==0b111100000:
        print(COLORS.GREEN%"You did it!")
        return
    print(COLORS.YELLOW%"The ownership and permissions aren't quite right yet. Run me again once you made all the changes correctly.")
    exit(0)

FLAG="ECS{M45T3R1NG_TH3_8451C5_29D681ECC64D3BF68DCABFA2D24270DD}"
HIDDENFLAG="ECS{D1D_Y0U_U53_PTR4C3_PL3453_L3T_M3_KN0W_0292EA3496F29E820FA611ED1D6E96E6}"

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
"1": SimpleChallenge("What's your current working directory?",
                     os.getcwd(),
                     "ac3ecd705892576379c11be4540e79e4"),
"2": SimpleChallenge("Search the man pages. What command would you use to generate random permutations?",
                     "shuf",
                     "4c0d80eca2683d55e5bc972ca78268de"),
"3": SimpleChallenge("On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31",
                     datetime.date.fromtimestamp(os.stat("/home/user/myfile.txt").st_mtime).isoformat(),
                     "ef0de16e3533db9df0e1dee1affa0def"),
"4": SimpleChallenge("How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number.",
                     str(round(os.stat("myfile.txt").st_size/1024.0)),
                     "b62aea63c8cdade52a5fb18a5b66365a"),
"5": SimpleChallenge("What user owns the file /home/user/myfile.txt?",
                     "root",
                     "b1ca704d15b63343965839fff7f323aa"),
"6": SimpleChallenge("What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g 777)",
                     "754",
                     "f0a96512c47f6a7466f10d89aa08d596"),
"7": SimpleChallenge("What is the user id of 'admin'?",
                     "1338",
                     "5f175a61bf6b509a1e374d998f1ca368"),
"8": SimpleChallenge("There's a user 'john' on the system. Can he write to /home/user/myfile.txt?",
                     "no", #create john, in admin group
                     "45fad0ab4fc449c8c70cf35bf5b55587"),
"9": SimpleChallenge("Can the 'admin' user execute /home/user/myfile.txt",
                     "yes",
                     "5b9dafd71e1ecaeec2479f48ff779cd9"),
"10":SimpleChallenge("Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?",
                     "rose", #create dave not in admin group, rose in user and admin group, jade in user group (not in admin group)
                     "c90556fd2eae3acf81e9acd443a5d2d0"),
"11":SimpleChallenge("/home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?",
                     "jpeg",
                     "69afff61f7005f94203d7423ea4623c2"),
"11":Challenge(chmodhandler, "3dbd152de50179208711f8e02966a0b4")
}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in CONFIG:
        print("To use this tool: Run `answer x` to answer question x.\nThere are {0} questions in total, from 1 to {0}.".format(len(CONFIG)))
        os.exit(1)
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
