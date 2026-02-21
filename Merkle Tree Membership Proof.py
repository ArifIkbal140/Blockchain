"""
Write a program in Python to Prove Membership and Non-membership in a Merkle Tree
Blockchain
"""


import hashlib

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

def build_tree(data):
    level = [h(x) for x in data]
    tree = [level]

    while len(level) > 1:
        new = []
        for i in range(0,len(level),2):
            left = level[i]
            right = level[i+1] if i+1 < len(level) else left
            new.append(h(left+right))
        tree.append(new)
        level = new

    return tree

def prove_membership(tree, index):
    proof = []
    for level in tree[:-1]:
        sibling = index ^ 1
        
        if sibling < len(level):
            if index % 2 == 0:
                proof.append(("right", level[sibling]))
            else:
                proof.append(("left", level[sibling]))
        
        index //= 2
    return proof

def verify_proof(data, proof, root):
    cur = h(data)

    for direction, p in proof:
        if direction == "right":
            cur = h(cur + p)
        else:
            cur = h(p + cur)

    return cur == root


# Transactions
tx = ["A","B","C","D"]
tree = build_tree(tx)

root = tree[-1][0]
print("Merkle Root:", root)

# Membership proof for "C"
index = tx.index("B")
proof = prove_membership(tree,index)

print("\nProof:", proof)
print("Verification:", verify_proof("C",proof,root))

# Non-membership test
print("\nCheck non-member 'X':",
      verify_proof("X",proof,root))


'''অর্থাৎ এমন একটি প্রোগ্রাম লিখতে হবে যা:

একটি Merkle Tree তৈরি করবে

প্রমাণ করবে কোনো ডাটা tree-এর সদস্য (membership) কিনা'''