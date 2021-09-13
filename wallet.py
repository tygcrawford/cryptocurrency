from transaction import Transaction
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pss


class Wallet:
    def __init__(self):
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()

    def sign_transaction(self, transaction):
        h = SHA256.new()
        
        h.update(transaction.sender)
        h.update(transaction.reciever)
        h.update(str(transaction.ammount).encode())

        transaction.signature = pss.new(self.private_key).sign(h)
    
    def construct_transaction(self, reciever, ammount):
        t = Transaction(self.public_key.exportKey(), reciever, ammount)
        self.sign_transaction(t)
        return t
