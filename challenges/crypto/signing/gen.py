import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.hashes import Hash, SHA512

private_key=rsa.generate_private_key(public_exponent=65537, key_size=1024, backend=default_backend())
key=private_key.private_numbers()
print("N =",key.public_numbers.n)
print("E =",key.public_numbers.e)

def genflag():
    return "ECS{4_3V3N_81GG3R_H4Y5T4CK_"+("".join([secrets.choice("0123456789ABCDEF") for _ in range(32)]))+"}"

def sign(msg):
    digest=Hash(SHA512(), backend=default_backend())
    digest.update(msg.encode())
    signingdata=int.from_bytes(digest.finalize(), "big")
    return pow(signingdata, key.d, key.public_numbers.n)

flag=genflag()
print(flag, sign(flag))

for i in range(9999):
    print(genflag(), sign(secrets.token_hex()))
