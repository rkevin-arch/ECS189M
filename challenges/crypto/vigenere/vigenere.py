import sys
import random
import collections

key="mykey"
startline="Again, same drill as the last challenge. If you haven't solved that one yet, I'm not sure how you got here. Use the path \"pager_doormat_decimeter_ravage_unlinked\" as the path that you enter in your browser. Now, for a list of randomly generated words to fill this space without me having to copy the entirety of Homestuck into this text document."

with open("words_sanitized.txt","r") as f:
    words=f.read().splitlines()

def genline():
    return " ".join([random.choice(words) for _ in range(500)])

def vigenc(a,b):
    b=ord(b)-ord('a')
    if 'a'<=a<='z':
        if ord(a)+b>ord('z'):
            return chr(ord(a)+b-26), True
        return chr(ord(a)+b), True
    if 'A'<=a<='Z':
        if ord(a)+b>ord('Z'):
            return chr(ord(a)+b-26), True
        return chr(ord(a)+b), True
    return a, False

def round():
    plain="\n".join([startline]+[genline() for _ in range(10)]+[""])
    cipher=[]
    keyoff=0
    freqs=[collections.Counter() for _ in range(len(key))]
    for c in plain:
        r,s=vigenc(c,key[keyoff])
        cipher.append(r)
        if s:
            freqs[keyoff].update([c.lower()])
            keyoff=(keyoff+1)%len(key)
    for i in freqs:
        print(i.most_common(3))
    with open("plain.txt","w") as f:
        f.write("".join(plain))
    with open("vigenere.txt","w") as f:
        f.write("".join(cipher))

round()
