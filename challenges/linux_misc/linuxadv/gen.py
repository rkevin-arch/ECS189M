import random
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def genstr():
    return "".join([random.choice(alphabet) for _ in range(random.randint(5,20))])
for i in range(10000):
    print(genstr())
