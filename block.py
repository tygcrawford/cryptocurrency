from typing import List
from transaction import Transaction

import time
from Crypto.Hash import SHA256


class Block:
    def __init__(self, transactions: List[Transaction], prev_hash: str, difficulty: int, nonce: int = 0) -> None:
        self.prev_hash: str = prev_hash
        self.nonce: int = nonce
        self.timestamp: float = time.time()
        self.difficulty: int = difficulty

        self.transactions: List[Transaction] = transactions

        self.hash: str = None
        self.merkle_root: str = None

    def compute_hash(self) -> str:
        h = SHA256.new()

        h.update(self.prev_hash.encode())
        h.update(self.merkle_root.encode())
        h.update(str(self.timestamp).encode())
        h.update(str(self.difficulty).encode())
        h.update(str(self.nonce).encode())

        return h.hexdigest()

    @staticmethod
    def compute_merkle_tree_layer(layer: List[str]) -> List[str]:
        n = len(layer)
        if n == 1:
            return layer

        next_layer: List[str] = []
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

    def compute_merkle_root(self) -> str:
        h: List[str] = [transaction.compute_hash() for transaction in self.transactions]

        while len(h) != 1:
            h = Block.compute_merkle_tree_layer(h)

        return h[0]

    # split this up into single guess validation for network
    def validate(self) -> None:
        while self.compute_hash()[0:self.difficulty] != ('0' * self.difficulty):
            self.nonce += 1

        self.hash = self.compute_hash()
