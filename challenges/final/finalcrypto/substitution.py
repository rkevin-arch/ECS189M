import random
letters="abcdefghijklmnopqrstuvwxyz"
perm=list(letters)
random.shuffle(perm)
trans=str.maketrans(letters+letters.upper(),
    "".join(perm)+"".join(perm).upper())
with open("plain.txt","r") as i:
    with open("cipher.txt","w") as o:
        for l in i:
            for c in l:
                    o.write(c.translate(trans))
