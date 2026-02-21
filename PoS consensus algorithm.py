"""
Write a program in Python to implement PoS consensus algorithm.
"""


import random

validators = {
    "Alice": 50,
    "Bob": 30,
    "Charlie": 20
}

def select_validator():
    total = sum(validators.values())
    pick = random.uniform(0,total)
    current = 0

    for v,stake in validators.items():
        current += stake
        if current > pick:
            return v

selected = select_validator()
print("Selected Validator:", selected)


'''PoS হলো blockchain-এ একটি consensus mechanism যেখানে:
✅ নির্বাচিত validator block তৈরি বা verify করে


যারা বেশি stake (coin/token) রাখে, তাদের নির্বাচিত হওয়ার সম্ভাবনা বেশি

Random না, probability নির্ভর করে stake এর পরিমাণের উপর

এটি energy-efficient কারণ mining (Proof of Work) এর মত computational power লাগে না'''


'''total = 100

pick = 65

current ধাপে ধাপে:

Alice: current = 50 → 50 > 65? না

Bob: current = 50 + 30 = 80 → 80 > 65? হ্যাঁ → Bob নির্বাচিত

এভাবে stake অনুযায়ী probability proportional হয়।s'''