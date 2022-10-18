from Crypto.Cipher import Salsa20 as Salsa20
import base64
import gmpy2 
from gmpy2 import mpz


plaintext=b'hi gurl'
secret = b'*Thirty-two byte (256 bits) key*'
cipher = Salsa20.new(secret)
msg = cipher.nonce + cipher.encrypt(plaintext)
print(msg , base64.b64encode(msg))


secret = b'*Thirty-two byte (256 bits) key*'
msg_nonce = msg[:8]
ciphertext = msg[8:]
print(msg_nonce,"ctext ",ciphertext)
cipher = Salsa20.new(secret,msg_nonce)

plaintext = cipher.decrypt(ciphertext)
print(ciphertext,plaintext.decode())


# in1=input("Input first prime: ")
# in2=input("Input second prime: ")
# if(in2>in1):
#     k=(gmpy2.next_prime(mpz(in2)))

# else:
#     k=(gmpy2.next_prime(mpz(in1)))
# m=gmpy2.mul(mpz(in1), mpz(in2));

# print(gmpy2.gcd(mpz(k),mpz(m)))
# print(m,k)

# print(gmpy2.is_strong_prp((15),2));

# print(plaintext , msg,cipher.nonce)