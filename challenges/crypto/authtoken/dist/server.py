import sys
import re
from secret import KEY, FLAG

def xor(key, ciphertext):
    return bytes([key[i] ^ ciphertext[i] for i in range(len(ciphertext))])

username_regex=re.compile(b'[A-Za-z0-9]*\Z')

def decrypt(token):
    try:
        token=bytes.fromhex(token)
    except ValueError:
        return None
    if len(KEY)<len(token):
        return None
    plaintext=xor(KEY, token)
    if username_regex.match(plaintext) is None:
        return None
    return plaintext.decode()

def main():
    while True:
        print("Please enter your secret token!")
        sys.stdout.flush()
        token=input()
        username=decrypt(token)
        if username is None:
            print("The token you entered was invalid.")
            continue
        if username != 'administrator':
            print("You are validated as user %s, but you are not the administrator. Please enter the administrator's token."%username)
            continue
        print("Welcome back, administrator! Here's your flag:",FLAG)
        break

if __name__=="__main__":
    main()
