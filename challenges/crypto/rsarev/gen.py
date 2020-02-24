import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.hashes import Hash, SHA512

tmp_key=rsa.generate_private_key(public_exponent=65537, key_size=1024, backend=default_backend())
p=tmp_key.private_numbers().p
e=tmp_key.private_numbers().public_numbers.e
# find a q thats a prime and really close to p
# copied from https://jeremykun.com/2013/06/16/miller-rabin-primality-test/
import random

def decompose(n):
   exponentOfTwo = 0

   while n % 2 == 0:
      n = n//2
      exponentOfTwo += 1

   return exponentOfTwo, n

def isWitness(possibleWitness, p, exponent, remainder):
   possibleWitness = pow(possibleWitness, remainder, p)

   if possibleWitness == 1 or possibleWitness == p - 1:
      return False

   for _ in range(exponent):
      possibleWitness = pow(possibleWitness, 2, p)

      if possibleWitness == p - 1:
         return False

   return True

def probablyPrime(p, accuracy=100):
   if p == 2 or p == 3: return True
   if p < 2: return False

   exponent, remainder = decompose(p - 1)

   for _ in range(accuracy):
      possibleWitness = random.randint(2, p - 2)
      if isWitness(possibleWitness, p, exponent, remainder):
         return False

   return True

q=p+2
while not probablyPrime(q):
    q+=2
print(p)
print(q)
print(q-p)
print("---")
n=p*q
print(n)
print(e)
msg=int.from_bytes(b"ECS{L00K1NG_F0R_5P0N50R5H1P5_PL3453_53ND_M0N3Y_FB94A235B061514E83F43DB79C91BD91}", "big")
print(pow(msg,e,n))
