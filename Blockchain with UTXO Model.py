"""
Write a program in Python to implement a blockchain and UTXo (unspent transaction output).
"""

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class BlockchainUTXO:
    def __init__(self):
        self.utxo = {}   # wallet -> balance  utxo = dictionary → wallet এর current balance track করে।
        self.chain = []  #chain = list → সব transactions কে store করে।

    def create_transaction(self, tx):
        if tx.sender != "SYSTEM":
            if self.utxo.get(tx.sender,0) < tx.amount:
                print("Transaction failed: insufficient balance")
                return

            self.utxo[tx.sender] -= tx.amount

        self.utxo[tx.receiver] = self.utxo.get(tx.receiver,0) + tx.amount
        self.chain.append(tx)
        print("Transaction successful")   #Sender এর balance কমানো হয়। #Receiver এর balance বৃদ্ধি পায়।




    def show_balances(self): #সব wallet এর current balance দেখায়।
        print("\nBalances:")
        for user,balance in self.utxo.items():
            print(user,":",balance)


bc = BlockchainUTXO()

bc.create_transaction(Transaction("SYSTEM","Alice",50))
bc.create_transaction(Transaction("Alice","Bob",20))
bc.create_transaction(Transaction("Bob","Charlie",10))

bc.show_balances()



'''
এখানে মূল লক্ষ্য হলো UTXO-based blockchain এর কাজ দেখানো।

UTXO = Unspent Transaction Output → মানে হলো প্রতিটি wallet-এ কত balance আছে, যা এখনও খরচ হয়নি।

প্রোগ্রামটি blockchain-এর মতো transaction management করে, কিন্তু সহজভাবে, mining বা hash logic ছাড়া।'''