from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import binascii

iv = binascii.unhexlify('6ed541b6ca008267aec855b643fe4dfc')

def encrypt(plaintext, password="abc"):
    key = PBKDF2(password, b'', dkLen=24, count=10000)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = pad(plaintext.encode('utf-8'), AES.block_size) 
    ciphertext = cipher.encrypt(plaintext)
    return binascii.hexlify(ciphertext).decode('utf-8') 

def decrypt(ciphertext, password="abc"):
    key = PBKDF2(password, b'', dkLen=24, count=10000)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = cipher.decrypt(binascii.unhexlify(ciphertext))
    return unpad(plaintext, AES.block_size).decode('utf-8')

print(encrypt("my secret message"))
print(decrypt(encrypt("my secret message")))
print(decrypt("bc9f5d72bf3053d4a906e9de41509af3"))

