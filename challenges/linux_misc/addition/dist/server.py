from timeout_decorator import *
from subprocess import call
import random
import sys
import os

@timeout(10)
def questions():
    for i in range(50):
        a=random.randint(1,999999999)
        b=random.randint(1,999999999)
        print("Question",i,":",a,"+",b)
        print("Your answer:")
        sys.stdout.flush()
        c=input()
        try:
            c=int(c)
        except:
            print("Hey! Numbers only! The teacher is not amused.")
            sys.stdout.flush()
            exit()
        if(c!=a+b):
            print("Wrong! Go back to grade school and learn your addition!")
            sys.stdout.flush()
            exit()

print("John just noticed his homework is due in 10 seconds!")
print("Help him finish his homework, which contains 50 additions.")
try:
    questions()
    print("You did it! John would like to reward you with a shell.")
    print("Find the flag there!")
    sys.stdout.flush()
    call("/bin/bash")
except TimeoutError:
    print("You took too much time! The homework was collected and John is now a very sad kid.")

