"""
Write a Python program to Demonstrate the Mining Process in Blockchain 
"""


import hashlib

data = "Sample Block"
difficulty = 4

nonce = 0
prefix = "0"*difficulty

while True:
    text = data + str(nonce)
    hash_val = hashlib.sha256(text.encode()).hexdigest()

    if hash_val.startswith(prefix):
        break

    nonce += 1

'''Block data + nonce কে hash করা হয়।

Check করা হয় hash কি "0000" দিয়ে শুরু হচ্ছে।

যদি না হয় → nonce 1 বাড়ানো হয় → পুনরায় চেষ্টা।

যতক্ষণ না মিলছে → loop চলতে থাকে।'''


print("Block Data:", data)
print("Nonce Found:", nonce)
print("Hash:", hash_val)


'''খানে মূল লক্ষ্য হলো Proof-of-Work (PoW) mining process simulate করা।

Mining মানে হলো: এমন একটি nonce খুঁজে বের করা যাতে 
block hash একটি নির্দিষ্ট difficulty satisfy করে (শুরু হয় n টি zero দিয়ে)।'''