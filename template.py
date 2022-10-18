#FCS Assignment 1, question 1
#Name:
#Roll number:

from Crypto.Cipher import Salsa20
import gmpy2
from gmpy2 import mpz
import os
import random



alice_key=""
def randomword(length):
   letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
#    print(letters)
   return ''.join(random.choice(letters) for i in range(length))
   
def encrypt_text(num,e,n):
    return gmpy2.powmod(mpz(num), mpz(e), mpz(n))

def decrypt_text(num,d,n):
    return gmpy2.powmod(mpz(num), mpz(d), mpz(n))

def alice_generates_symmetric_key():
    ''' 
    A function that returns a 16 byte string to be used as the key for Salsa20.
    This key should be used to encrypt Bob and Alice's communications.
    But before that, it needs to be sent to Bob.

    Input: NA
    Return: the symmetric key (byte string)
    '''
    alice_key=randomword(16);
    return alice_key
    # pass

def bob_generates_asymmetric_keys(p ,q):
    '''
    A function that takes in prime numbers p and q and generates 
    the public and private keys for Bob as per RSA. Note that you are 
    not allowed to use loops to find e or d.

    Input: p, q (upto 1023 digits long)
    Return: Bob's public key and private key ((e,n), (d,n)) as a tuple
    '''
    n=gmpy2.lcm(mpz(p),mpz(q))# n, e, d
    
    phi=gmpy2.mul(mpz(gmpy2.sub(mpz(p), 1)),mpz(gmpy2.sub(mpz(q), 1)))
    if(p>q):
        e=gmpy2.next_prime(mpz(p));
        # e=3
    else:
        e=gmpy2.next_prime(mpz(q));
        # e=3
    
    d=gmpy2.invert(e, phi);
    print("e: ",e, " d: ",d)
    

    # print(gmpy2.mul(mpz(p),mpz(q)))

    return ((e,n),(d,n));
    # pass

def alice_sends_symmetric_key(k, e, n):
    '''
    A function that Alice uses to encrypt the symmetric key
    using Bob's public key. The ciphertext is sent to Bob.

    Input: the symmetric key k, Bob's public key e, n.
    Return: encrypted ciphertext
    '''

    # bobkeys=bob_generates_asymmetric_keys(p, q)
    pass

def bob_decrypts_symmetric_key(c, d, n):
    '''
    A function that Bob uses to decrypt the ciphertext c using his private key.
    The decrypted message would give him the symmetric key.

    Input: the ciphertext c, Bob's private key d, n.
    Return: the symmetric key (byte string)
    '''
    pass

def bob_sends_message(m, k):
    '''
    A function that takes a message m, shared key k and uses Salsa20 to encrypt m.

    Input: the message m (a byte string), the shared key k (byte string)
    Return: encrypted ciphertext
    '''
    pass

def alice_decrypts_message(c_, k):
    '''
    A function that takes an encrypted message c_, shared key k and uses Salsa20 to decrypt c_.

    Input: the ciphertext c_, the shared key k (byte string)
    Return: plaintext message
    '''
    pass

if __name__=="__main__":
    # p, q and the message m will be taken as inputs from the user.
    p=input("Enter p :")
    q=input("Enter q :")
    
    print(alice_generates_symmetric_key())
    key=bob_generates_asymmetric_keys(p, q);
    # print(key[0][0])

    msg=input("Enter Plaintext: ");
    

    decry=key[1][0]
    encry=key[0][0]
    prod=key[0][1]
    # phi=gmpy2.mul(mpz(gmpy2.sub(mpz(p), 1)),mpz(gmpy2.sub(mpz(q), 1)))
    #cipher=(msg^e)%prod
    # print("phi ",phi)
    cipher=encrypt_text(msg, encry, prod)
    # print(bob_generates_asymmetric_keys(p, q))
    print("Encrypted Text: ",cipher);
    # print("decry encry prod",decry,encry,prod);
    #plain=(cipher^d)%prod
    
    plain=decrypt_text(cipher, decry, prod)
    # print(encry,decry,prod)
    # print(gmpy2.invert(3, 5))
    
    print("Decrypted Text:  ",plain)
    pass
