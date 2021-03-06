from typing import List
from wallet import Wallet
from transaction import Transaction
from blockchain import BlockChain
from block import Block

# s = Wallet()
# r = Wallet()

# t = Transaction(s.public_key.exportKey().decode('utf-8'), r.public_key.exportKey().decode('utf-8'), 10)
# s.sign(t)

# bc = BlockChain(4)
# bc.add_block([t.__dict__])

# t_temp = Transaction(None, None, None)
# t_temp.__dict__ = bc.chain[0].transactions[0]
# print(t_temp.verify())

s = Wallet()
r = Wallet()

temp = Wallet()

t = []

for ammount in range(5):
    t.append(s.construct_transaction(r.public_key.exportKey(), ammount))

t[2].reciever = temp.public_key.exportKey()

for i in t:
    print(i.verify_signature())

b = Block(t, '0', 5)
print(b.compute_merkle_root())
b.merkle_root = b.compute_merkle_root()
print(b.compute_hash())