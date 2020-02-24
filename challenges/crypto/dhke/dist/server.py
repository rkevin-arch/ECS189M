from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
import sys
flag="ECS{H3R3_83_M4RL1N5P1K35_0030F47DD6D5452D1218A4321E4D344C}"
print("Generating some numbers, please wait for a sec...")
sys.stdout.flush()
params = dh.generate_parameters(generator=2, key_size=512, backend=default_backend())
sk=params.generate_private_key()
p=sk.public_key().public_numbers().parameter_numbers.p
y=sk.public_key().public_numbers().y
print("Let's use the following modulus for our key exchange, using generator g=2:")
print(p)
print("I have generated my public key as follows:")
print(y)
print("Please enter your public key!")
try:
    x=int(input())
except ValueError:
    print("You didn't enter an integer for your key! Quitting!")
    sys.exit()
if x<2 or x>=p:
    print("Hey! Public keys within range only!")
    sys.exit()
def is_power_of_two(x):
    if x==1:
        return True
    if x%2==1:
        return False
    return is_power_of_two(x//2)
if is_power_of_two(x):
    print("Hey! Your exponent (private key) is so small I could've guessed it! Try to use a larger secure exponent instead!")
    sys.exit()

pn=dh.DHParameterNumbers(p,2)
peer=dh.DHPublicNumbers(x,params.parameter_numbers()).public_key(default_backend())
key=sk.exchange(peer)
print("I have encrypted the flag by XORing it bitwise with our shared secret. Here it is:")
def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])
print(int.from_bytes(xor(key,flag.encode().rjust(len(key),b'\0')),"big"))
