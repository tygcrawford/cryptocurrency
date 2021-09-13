from hashlib import sha256
from Crypto.PublicKey import RSA
from Crypto.Signature import pss


class Transaction:
    def __init__(self, sender, reciever, ammount):
        self.sender = sender
        self.reciever = reciever
        self.ammount = ammount

        self.signature = None

    def compute_hash(self):
        h = sha256()

        h.update(self.sender)
        h.update(self.reciever)
        h.update(str(self.ammount).encode())
        h.update(self.signature)

        return h.hexdigest()

    def verify_signature(self):
        h = sha256()

        h.update(self.sender)
        h.update(self.reciever)
        h.update(str(self.ammount).encode())

        k = RSA.import_key(self.sender)
        v = pss.new(k)

        try:
            v.verify(h, self.signature)
            return True
        except (ValueError, TypeError):
            return False
