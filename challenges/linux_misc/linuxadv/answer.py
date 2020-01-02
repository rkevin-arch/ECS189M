#!/usr/bin/python3
import os
import sys
import datetime
import stat
import signal

class COLORS:
    PURPLE = '\033[95m%s\033[0m'
    BLUE   = '\033[94m%s\033[0m'
    GREEN  = '\033[92m%s\033[0m'
    YELLOW = '\033[93m%s\033[0m'
    EMPHASIS = '\033[1m\033[4m'

FLAG="ECS{R3D_GR33N_8LU3_A8E848A2EF5876D0CEC2779A8EBC75A7}"

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

class SignalChallenge(Challenge):
    def __init__(self,question,sig,secret):
        self.question=question
        self.sig=sig
        self.secret=secret
    def handler(self):
        wokenup=False
        def sighandler(sig, frame):
            nonlocal wokenup
            if sig==self.sig:
                print(COLORS.GREEN%"You did it! Press enter to continue")
                wokenup=True
        print(COLORS.BLUE%self.question)
        signal.signal(self.sig, sighandler)
        while not wokenup:
            pass

def q4handler():
    print(COLORS.BLUE%"Redirect my standard input to be the contents of /home/user/in.txt")
    if os.fstat(0).st_ino==os.stat("/home/user/in.txt").st_ino:
        return
    print(COLORS.YELLOW%"Sorry, that didn't work. Try again.")
    sys.exit(1)

def q5handler():
    print(COLORS.BLUE%"Redirect my standard error into /dev/null.")
    if os.fstat(2).st_ino==os.stat("/dev/null").st_ino:
        return
    if not sys.stdout.isatty(): #then they probably did >/dev/null instead of 2>/dev/null, print helpful msg
        print(COLORS.YELLOW%"You probably redirected stdout instead of stderr. Check your command again!",file=sys.stderr)
        sys.exit(1)
    print(COLORS.YELLOW%"Sorry, that didn't work. Try again.")
    sys.exit(1)

def q6handler():
    print(COLORS.BLUE%"Cat out the contents of /home/user/in.txt, grep for the lines that contain the lowercase letter 'a', and pipe the result into me.")
    if sys.stdin.isatty():
        print(COLORS.YELLOW%"Sorry, that didn't work. Try again.")
        sys.exit(1)
    try:
        with open("/home/user/in.txt","r") as f:
            for l in f.readlines():
                if "a" in l:
                    if l.strip()!=input():
                        print(COLORS.YELLOW%"Sorry, the input isn't what I'd expect. Double check your command?")
                        sys.exit(1)
    except EOFError:
        print(COLORS.YELLOW%"Sorry, the input isn't what I'd expect. Double check your command?")
        sys.exit(1)
    try:
        s=input()
    except EOFError:
        return
    print(COLORS.YELLOW%"Sorry, the input isn't what I'd expect. Double check your command?")

def q7handler():
    print(COLORS.BLUE%"Run `. spawner` to solve this challenge.")
    sys.exit(1)

CONFIG={
"1": SignalChallenge("Try backgrounding this process and foregrounding it again.",
                     signal.SIGCONT,
                     "de69c0d1ec6680008751436f97e11d99"),
"2": SimpleChallenge("What's my PID? (You're free to background this process, figure out the answer, then foreground it again to answer)",
                     str(os.getpid()),
                     "01db71f7e59479c8998647faf703be66"),
"3": SignalChallenge("Send me a SIGUSR1 signal.",
                     signal.SIGUSR1,
                     "6706038ae52a5ce18d39a9540e568ba7"),
"4": Challenge(q4handler,"348b6f0a3cbe991b5df15d3c36d83c57"),
"5": Challenge(q5handler,"25d112dd48c09d3aedc2aa2e7d610a13"),
"6": Challenge(q6handler,"59b4156f08c83f8e437f4ab7baa3ca9a"),
"7": Challenge(q7handler,"45fd98f0038fcdd95dc182a3e5d37f36"),
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
