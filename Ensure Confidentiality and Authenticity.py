
'''Write a Python program to ensure the confidentiality and 
authenticity of a message using encryption and digital signature.'''


# Ensure you have pycryptodome installed: pip install pycryptodome
import hashlib

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 1️⃣ Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# 2️⃣ Message to encrypt
message = b"Hello, this is a secret message."

# 3️⃣ Encrypt message (confidentiality)
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)
print("Encrypted:", encrypted_message.hex()[:60]+"...")  # truncated

# 4️⃣ Sign message (authenticity)
h = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(h)
print("Digital Signature:", signature.hex()[:60]+"...")

# 5️⃣ Decrypt message
decrypt_cipher = PKCS1_OAEP.new(private_key)
decrypted_message = decrypt_cipher.decrypt(encrypted_message)
print("Decrypted:", decrypted_message.decode())

# 6️⃣ Verify signature
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Signature verification: Success")
except (ValueError, TypeError):
    print("Signature verification: Failed")


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# 1️⃣ Generate RSA keys
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# 2️⃣ Message to encrypt
message = b"Hello, this is a secret message."

# 3️⃣ Encrypt message (confidentiality)
cipher = PKCS1_OAEP.new(public_key)
encrypted_message = cipher.encrypt(message)
print("Encrypted:", encrypted_message.hex()[:60]+"...")  # truncated

# 4️⃣ Sign message (authenticity)
h = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(h)
print("Digital Signature:", signature.hex()[:60]+"...")

# 5️⃣ Decrypt message
decrypt_cipher = PKCS1_OAEP.new(private_key)
decrypted_message = decrypt_cipher.decrypt(encrypted_message)
print("Decrypted:", decrypted_message.decode())

# 6️⃣ Verify signature
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Signature verification: Success")
except (ValueError, TypeError):
    print("Signature verification: Failed")