# crypto_1.py
# mgb 29/11/21
# play with python cryptography module

from cryptography.fernet import Fernet

#key = Fernet.generate_key()
key=b'1qComkUb0xWc2imWBvj-zn9QOdgnh6rH0cdja_QQvBU='
print(key)

f = Fernet(key)

token = f.encrypt(b"my deep dark secret")

print(token)


message=f.decrypt(token)
print(message)
