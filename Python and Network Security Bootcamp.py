import password as password

x = input()

import hashlib
#1st method
hash_object = hashlib.md5(x.encode())
hash_dig = hash_object.hexdigest()
print(hash_dig)
#2nd method
hash_object = hashlib.sha224(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
#3rd method
hash_object = hashlib.sha256(x.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
#4th method
hash_object = hashlib.sha384(x.encode())
hash_dig = hash_object.hexdigest()
print(hash_dig)

