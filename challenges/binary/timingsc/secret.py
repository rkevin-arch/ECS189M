import random
flag="CSCaUCD{T1CK_T0CK_86EB9A0242E94E66DB372F75E1BCF415}"
def gensecret(i):
    alphabet="0123456789ABCDEF"
    return "".join([random.choice(alphabet) for _ in range(i)])
secret=gensecret(random.randint(8,15))
