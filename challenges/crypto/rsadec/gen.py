import secrets
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.hashes import Hash, SHA512

private_key=rsa.generate_private_key(public_exponent=65537, key_size=1024, backend=default_backend())
key=private_key.private_numbers()
print("N =",key.public_numbers.n)
print("p =",key.p)
print("q =",key.q)
print("e =",key.public_numbers.e)
print("d =",key.d)

msg=int.from_bytes(b"ECS{N0T_5P0N50R3D_8Y_TH3_R54_C0NF3R3NC3_7A936E84C18824C4450A5F03B75B4C2B}", "big")
print(pow(msg,key.public_numbers.e,key.public_numbers.n))
