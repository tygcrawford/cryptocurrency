import time
from hashlib import sha256
from transaction import Transaction
from typing import List


class Block:
    def __init__(self, transactions, prev_hash, difficulty, nonce=0):
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.timestamp = time.time()
        self.difficulty = difficulty

        self.transactions = transactions

        self.hash = None
        self.merkle_root = None

    def compute_hash(self):
        h = sha256()

        h.update(self.prev_hash.encode())
        # h.update(self.merkle_root)
        # h.update(str(self.timestamp).encode())
        h.update(str(self.difficulty).encode())
        h.update(str(self.nonce).encode())

        return h.hexdigest()
	
    def compute_merkle_root(self):
        pass

    def validate(self, difficulty):
        while self.compute_hash()[0:difficulty] != ('0' * difficulty):
            self.nonce += 1

        self.hash = self.compute_hash()
