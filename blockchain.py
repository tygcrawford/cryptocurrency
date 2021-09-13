from block import Block


class BlockChain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty

    def add_block(self, transactions):
        if len(self.chain) == 0:
            genesis_block = Block(0, transactions, '0'*64)
            genesis_block.prove(self.difficulty)
            self.chain.append(genesis_block)
        else:
            block = Block(len(self.chain), transactions, self.chain[-1].hash)
            block.prove(self.difficulty)
            self.chain.append(block)
