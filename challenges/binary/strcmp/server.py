import random
import sys
from secret import flag, password
def strcmp(s1,s2):
    if s1==s2:
        return 0
    if s1>s2:
        return 1
    if s1<s2:
        return -1
print("I have a password that only has lowercase letters and has length 20.")
print("Enter the password to get the flag.")
sys.stdout.flush()
for i in range(99,-1,-1):
    attempt=input()
    result=strcmp(attempt,password)
    if result==0:
        print("Access granted! Here's your flag:")
        print(flag)
        sys.stdout.flush()
        exit()
    print("strcmp returned %d instead of 0!"%result)
    print("You have %d attempts left."%i)
    sys.stdout.flush()
print("Oops, you ran out of attempts. Better luck next time!")
exit()
