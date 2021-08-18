# Implement a Caesar cipher, both encoding and decoding. 
# The key is an integer from 1 to 25.

import math
import string

# create alphabet in list with string.asccii_uppercase
def listAlphabet():
    return list(string.ascii_uppercase)

liAlphabet = listAlphabet()

#return a string the encryptionCaesar
def encryptionCaesar(message: str, rotate: int) -> str:
    print("message encrypted: ", end="")
    for i in message.upper():
        if i in liAlphabet:
            """search the index of alphabet and the sum with the rotate and 27"""
            caesarCipher: int = liAlphabet.index(i) + int(math.fmod(rotate, 27))
            if caesarCipher >= len(liAlphabet):
                caesarCipher: int = caesarCipher - len(liAlphabet)
            print(liAlphabet[caesarCipher], end="")

#return a string the decryptorCaesar
def decryptorCaesar(message: str, rotate: int) -> str:
    print("message decrypted: ", end="")
    for i in message.upper():
        if i in liAlphabet:
            """search the index of alphabet and the subtraction with the rotate and 27"""
            descyptedCaesar: int = liAlphabet.index(i) - int(math.fmod(rotate, 27))
            if descyptedCaesar < 0:
                descyptedCaesar: int = descyptedCaesar + len(liAlphabet)
            print(liAlphabet[descyptedCaesar], end="")

if __name__=='__main__':
    option: str = input("Encryption or Decryptor[E/D]: ").lower()
    if option == "e":
        message: str = input("Message: ")
        rotate: int = int(input("Rotate: "))
        caesarCipher = encryptionCaesar(message, rotate)
    elif option == "d":
        message: str = input("Message: ")
        rotate: int = int(input("Rotate: "))
        descyptedCaesar = decryptorCaesar(message, rotate)
    else:
        print("Error!")
    print()