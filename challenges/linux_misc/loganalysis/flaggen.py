import random
import uuid
import hashlib
import math
import collections
import itertools

allchars=set([chr(i) for i in range(32,127)])
nontailchars=allchars-set([i for i in "0123456789ABCDEF"])
nontxtchars=allchars-set([chr(i) for i in itertools.chain(range(48,58),range(65,91),range(97,123),range(95,96))])

def expo(v,c=16):
    i=int(math.ceil(random.expovariate(1.0/v)))
    if i>c:
        return c
    return i

def gentail():
    u=uuid.uuid4()
    m=hashlib.md5()
    m.update(str(u).encode())
    return m.hexdigest().upper()

def muttail():
    t=gentail()
    return muttxt(t,nontailchars)

def muttaillen():
    t=list(gentail())
    if(random.getrandbits(1)==1):
        dellist=sorted(random.sample(range(len(t)),expo(5,len(t))),reverse=True)
        for i in dellist:
            del t[i]
    else:
        for i in range(expo(5,len(t))):
            t.insert(i,random.choice("0123456789ABCDEF"))

    return "".join(t)

def muttxt(s,sample):
    s=list(s)
    chrs=expo(5,len(s))
    for i in random.sample(range(len(s)),chrs):
        s[i]=random.choice(tuple(sample))
    return "".join(s)

def randstr():
    return "".join([random.choice(tuple(allchars)) for i in range(expo(5,15))])

#true flag:1
print("ECS{N33DL3_1N_H4YST4CK_"+gentail()+"}")
#non ECS{}, valid else: 1000
for i in range(1000):
    print(muttxt("N33DL3_1N_H4YST4CK",allchars)+"_"+gentail())
#nonvalid anything, randchars: 1000
for i in range(1000):
    print("".join([random.choice(tuple(allchars)) for l in range(expo(30,60))]))
#nonvalid tail: 4000
for i in range(4000):
    print("ECS{"+muttxt("N33DL3_1N_H4YST4CK",allchars)+"_"+muttail()+"}")
#nonvalid start: 2000
for i in range(2000):
    print("ECS{"+muttxt("N33DL3_1N_H4YST4CK",nontxtchars)+"_"+gentail()+"}")
#tail length invalid: 1000
for i in range(1000):
    print("ECS{"+muttxt("N33DL3_1N_H4YST4CK",allchars)+"_"+muttaillen()+"}")
#random stuff at beginning or end: 999
for i in range(999):
    print(randstr()+"ECS{"+muttxt("N33DL3_1N_H4YST4CK",allchars)+"_"+gentail()+"}"+randstr())
