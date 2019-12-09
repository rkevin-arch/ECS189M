import random
import sys
import time
from secret import flag,secret

while True:
    print("Enter password to continue.")
    sys.stdout.flush()
    inp=input()
    #I heard computers can have errors sometimes
    #To make absolutely sure we are checking stuff right,
    #I'm running 100 checks and rejecting if it fails.
    #Can't let any false negatives slip by, can we?
    #Also, to reduce load, I'm making the program take a break
    #between every check.
    len_mismatch=False
    for i in range(100):
        if len(inp)!=len(secret):
            len_mismatch=True
            break
        time.sleep(0.001)
    if len_mismatch:
        print("Password incorrect!")
        sys.stdout.flush()
        continue
    for i in range(len(secret)):
        character_invalid=False
        for j in range(100):
            if inp[i]!=secret[i]:
                character_invalid=True
                break
            time.sleep(0.001)
        if character_invalid:
            print("Password incorrect!")
            sys.stdout.flush()
            break
    else:
        print("Access granted.")
        print("The flag is:",flag)
        sys.stdout.flush()
        exit()

