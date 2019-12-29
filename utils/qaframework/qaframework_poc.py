#!/usr/bin/python3
import os
import sys

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
            print(self.question)
            useranswer=input().strip()
            if useranswer==self.answer:
                return
            print("Sorry that's wrong, try again!")

def chal2handler():
    import psutil
    while True:
        print("Please keep 'sleep 1000' running in the background.")
        input()
        for p in psutil.process_iter(attrs=["cmdline"]):
            if p.info['cmdline']==["sleep", "1000"]:
                return

def chal4handler():
    import signal
    wokenup=False
    def sighandler(sig, frame):
        nonlocal wokenup
        if sig==signal.SIGUSR1:
            print("You did it!")
            wokenup=True
    signal.signal(signal.SIGUSR1, sighandler)
    while not wokenup:
        print("Please send me a SIGUSR1.")
        input()

CONFIG={
    "1":SimpleChallenge("Please enter the string 'My Answer'.", "My Answer", "7a0124d6bcd848d197c7d824777dd2ea"),
    "2":Challenge(chal2handler, "c59b902c74ab4f8cb8eb4abfbc0630ae"),
    "3":SimpleChallenge("Please enter the string 'answer'.", "answer", "ec5c8afe50c5492e91f1c5c45cceb3c4"),
    "4":Challenge(chal4handler, "e953c51310ec461f83704f63ac85cf69")
}

def main():
    if len(sys.argv)!=2 or sys.argv[1] not in CONFIG:
        print("To use this tool: Run `answer x` to answer question x.\nThere are {0} questions in total, from 1 to {0}.".format(len(CONFIG)))
        exit(1)
    challenge=CONFIG[sys.argv[1]]
    if not challenge.solved():
        challenge.handler()
        os.mknod("/tmp/qaframework/%s"%challenge.secret)
    else:
        print("You already solved this challenge!")

    unsolved=[]
    for k,v in CONFIG.items():
        if not v.solved():
            unsolved.append(k)
    if len(unsolved)==0:
        print("You did it! The flag is ECS{FAKEFLAG}.")
    else:
        print("You solved {0} out of {1} challenges! The challenges {2} remain.".format(
                len(CONFIG)-len(unsolved),len(CONFIG),", ".join(unsolved)))

if __name__=="__main__":
    main()
