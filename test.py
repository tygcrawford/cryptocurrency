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

b = Block([], '0', 5)
b.calculate_hash()