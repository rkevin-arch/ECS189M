from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from timeout_decorator import timeout, TimeoutError
import random
import sys

def is_power_of_two(x):
    if x==1:
        return True
    if x%2==1:
        return False
    return is_power_of_two(x//2)

def encrypt(msg):
    global key # lazy
    if type(key) is bytes:
        key=int.from_bytes(key,"big")
    if type(msg) is str:
        msg=msg.encode()
    if type(msg) is bytes:
        msg=int.from_bytes(msg,"big")
    return msg^key

def decrypt(msg):
    global key # lazy
    if type(key) is bytes:
        key=int.from_bytes(key,"big")
    if type(msg) is not int:
        try:
            msg=int(msg)
        except:
            print("Your message is not decodable using Diffie-Hellman!")
            print("Make sure you're sending a big integer that's your message in ASCII, XORed by the shared secret.")
            sys.exit()
    plain=msg^key
    plain=plain.to_bytes((plain.bit_length()-1)//8+1,"big")
    return plain

def dhke_print(msg):
    print(encrypt(msg))
    sys.stdout.flush()

def dhke_scanint(answer):
    msg=decrypt(input())
    if int.from_bytes(msg, 'big')==answer:
        return answer
    try:
        return int(msg)
    except:
        print("Your message is not a valid number after decoding with Diffie-Hellman!")
        print("Make sure your answer is in ASCII, then encoded into a big number and XORed with the shared secret.")
        sys.exit()

def gatekeep():
    print("Please enter the secret passphrase: ")
    sys.stdout.flush
    phrase=input()
    if phrase != "engraving_daisy_remedy_gleaming_barometer":
        print("Passphrase incorrect! Use the right passphrase from the note.")
        sys.exit()

def dhke():
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
    if is_power_of_two(x):
        print("Hey! Your exponent (private key) is so small I could've guessed it! Try to use a larger secure exponent instead!")
        sys.exit()

    pn=dh.DHParameterNumbers(p,2)
    peer=dh.DHPublicNumbers(x,params.parameter_numbers()).public_key(default_backend())
    global key # lazy
    key=sk.exchange(peer)

@timeout(10)
def questions():
    for i in range(50):
        a=random.randint(1,999999999)
        b=random.randint(1,999999999)
        dhke_print("Question %d: %d + %d. Your answer?"%(i,a,b))
        c=dhke_scanint(a+b)
        if(c!=a+b):
            dhke_print("Wrong! Go back to grade school and learn your addition!")
            sys.exit()

def main():
    gatekeep()
    print("Note: You are 1/3 of the way from solving the full challenge.")
    print("Detail how you got here in your writeup and you'll get at least 175 points for this challenge.")
    print("Welcome! To proceed, you need to solve a little programming challenge.")
    print("To make sure no one is listening, we need to encrypt our further communications with a Diffie-Hellman key exchange.")
    print("After the 'Key exchange established!' message, we will be talking using only encrypted messages, unless there are error messages.")
    print("We will both encrypt our messages by XORing the message in ASCII with the shared secret, converting that to a big endian number, and sending the number in ASCII.")
    sys.stdout.flush()
    dhke()
    print("Key exchange established!")
    dhke_print("You are 2/3 of the way from solving the challenge!")
    dhke_print("Detail how you got here in your writeup,")
    dhke_print("and you'll get at least 350 points for this challenge.")
    dhke_print("Now for your last programming challenge.")
    dhke_print("John's homework is due in 10 seconds!")
    dhke_print("Yes, this is exactly what you think it is.")
    try:
        questions()
        dhke_print("Good job! Visit the following URL for the flag.")
        dhke_print("https://photon.rkevin.dev/uproar_untrue_calculus_swirl")
    except TimeoutError:
        dhke_print("You took too much time!")

if __name__ == "__main__":
    main()
