import time
from Crypto.Hash import SHA256


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
        h = SHA256.new()

        h.update(self.prev_hash)
        h.update(self.merkle_root)
        h.update(str(self.timestamp).encode())
        h.update(str(self.difficulty).encode())
        h.update(str(self.nonce).encode())

        return h.hexdigest()

    @staticmethod
    def compute_merkle_tree_layer(layer):
        n = len(layer)
        if n == 1:
            return layer

        next_layer = []
        for hash in range(0, n, 2):
            h = SHA256.new()

            if hash + 1 < n:
                h.update(layer[hash].encode())
                h.update(layer[hash+1].encode())

                next_layer.append(h.hexdigest())
            else:
                h.update(layer[hash].encode())
                h.update(layer[hash].encode())

                next_layer.append(h.hexdigest())

        return next_layer

    def compute_merkle_root(self):
        h = [transaction.compute_hash() for transaction in self.transactions]

        while len(h) != 1:
            h = Block.compute_merkle_tree_layer(h)

        return h[0]

    # split this up into single guess validation for network
    def validate(self, difficulty):
        while self.compute_hash()[0:difficulty] != ('0' * difficulty):
            self.nonce += 1

        self.hash = self.compute_hash()
