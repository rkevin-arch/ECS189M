import random
perm=list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(perm)
table={}
for i in range(len(perm)):
    table[chr(ord('a')+i)]=perm[i]
    table[chr(ord('A')+i)]=perm[i].upper()
with open("plain.txt","r") as i:
    with open("substitution.txt","w") as o:
        for l in i:
            for c in l:
                if c in table:
                    o.write(table[c])
                else:
                    o.write(c)
