import random
import string as str

chars = " " + str.punctuation + str.digits + str.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")
plaintext = input("Enter a message to encrypt: ")

cypher_text = ""

for letter in plaintext:
    cypher_text += key[chars.index(letter)]

print(f"Encrypted message: {cypher_text}")