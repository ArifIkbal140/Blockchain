'''Write a Python program using a Merkle Tree to determine whether 
a given data block has been tampered with or not.'''


import hashlib

def h(x):
    return hashlib.sha256(x.encode()).hexdigest()

# Build Merkle Tree
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

# Generate proof for a given index
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

# Verify proof
def verify_proof(data, proof, root):
    cur = h(data)
    for direction, p in proof:
        if direction == "right":
            cur = h(cur+p)
        else:
            cur = h(p+cur)
    return cur == root

# Transactions
tx = ["A", "B", "C", "D"]
tree = build_tree(tx)
root = tree[-1][0]
print("Merkle Root:", root)

# Check tampering
for t in tx + ["X"]:  # X is tampered/non-member
    index = tx.index(t) if t in tx else 0
    proof = prove_membership(tree, index)
    valid = verify_proof(t, proof, root)
    print(f"Data '{t}' tampered? {'No' if valid else 'Yes'}")