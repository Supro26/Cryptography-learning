import random
import string

alphabet = list(string.ascii_uppercase)
substitution = alphabet.copy()
random.shuffle(substitution)

key = dict(zip(alphabet, substitution))
rev_key=dict(zip(substitution,alphabet))


def encrypt(key, p):
    Ctext=""
    for char in p.upper():
        if char in key:
            Ctext+=key[char]
        else:
            Ctext+=char
    return Ctext

def decrypt(rev_key, c):
    Ptext=""
    for char in c:
        if char in rev_key:
            Ptext+=rev_key[char]
        else:
            Ptext+=char
    return Ptext

a="Hello There!"
cypher=encrypt(key,a)
print(cypher)
plane=decrypt(rev_key,cypher)
print(plane)