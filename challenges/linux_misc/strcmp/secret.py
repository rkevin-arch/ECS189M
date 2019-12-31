import random
flag="ECS{81N4RY_534RCH_50AF9F479667C26EBF4EE74E956371D5}"
def genpasswd(l):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    return "".join([random.choice(alphabet) for _ in range(l)])
password=genpasswd(20)
