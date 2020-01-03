#!/usr/bin/python
from timeout_decorator import *
from subprocess import call
import random
import sys
import os
import struct

@timeout(10)
def questions():
    for i in range(50):
        a=random.randint(1,2147483647)
        b=random.randint(1,2147483647)
        sys.stdout.buffer.write(b"Question %d : "%i)
        sys.stdout.buffer.write(struct.pack("I",a))
        sys.stdout.buffer.write(b" + ")
        sys.stdout.buffer.write(struct.pack("I",b))
        sys.stdout.buffer.write(b"\n")
        sys.stdout.buffer.flush()
        c=sys.stdin.buffer.read(4)
        c=int(struct.unpack("I",c)[0])
        if(c!=a+b):
            print("Wrong! Go back to grade school and learn your addition!")
            sys.stdout.buffer.flush()
            sys.exit()

#os.chdir("/home/hal")

print("John just noticed his homework is due in 10 seconds!")
print("Help him finish his homework, which contains 50 additions.")
print("However, his teacher is a computer! Hal is giving his homework in binary.")
print("You have to answer the question in binary too.")
print('The format is "Question x : num + num", where num is a 4 byte little endian integer.')
print("Your answer should be another 4 byte little endian integer, with no newlines at the end.")
print("Ready? Go!")
sys.stdout.flush()
try:
    questions()

    print("You did it! John would like to reward you with a shell.")
    print("Find the flag there!")
    sys.stdout.buffer.flush()
    call("/bin/bash")
except TimeoutError:
    print("You took too much time! The homework was collected and John is now a very sad kid.")

