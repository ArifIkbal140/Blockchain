"""
Write a program in Python to implement PoW algorithm. 
"""


import hashlib
import time

def mine_block(data, difficulty):
    nonce = 0
    prefix = "0"*difficulty

    while True:
        text = data + str(nonce)
        hash_val = hashlib.sha256(text.encode()).hexdigest()

        if hash_val.startswith(prefix):
            return nonce, hash_val

        nonce += 1


data = "Block Data"
difficulty = 4
###data += str(time.time())

nonce, hash_val = mine_block(data, difficulty)

print("Data:", data)
print("Nonce:", nonce)
print("Hash:", hash_val)



'''PoW হলো blockchain-এর একটি consensus mechanism, যেমন Bitcoin ব্যবহার করে।

Miner (Node) নতুন block add করার জন্য computational puzzle solve করে।

Puzzle হলো এমন hash তৈরি করা যা difficulty অনুযায়ী zero দিয়ে শুরু হয়।

যিনি প্রথম solve করবে, সেই block chain-এ add হবে এবং reward পাবে।'''