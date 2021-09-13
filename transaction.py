from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pss


class Transaction:
    def __init__(self, sender: bytes, reciever: bytes, ammount: int) -> None:
        self.sender: bytes = sender
        self.reciever: bytes = reciever
        self.ammount: int = ammount

        self.signature: bytes = None

    def compute_hash(self) -> str:
        h = SHA256.new()

        h.update(self.sender)
        h.update(self.reciever)
        h.update(str(self.ammount).encode())
        h.update(self.signature)

        return h.hexdigest()

    def verify_signature(self) -> bool:
        h = SHA256.new()

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
