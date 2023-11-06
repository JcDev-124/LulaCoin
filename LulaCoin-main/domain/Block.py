import datetime
import hashlib

class Block:
    def __init__(self, description, previous_hash, block_count):
        self.index = block_count
        self.time = datetime.datetime.now()
        self.description = description
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.time) + str(self.description) + str(self.previous_hash)
        return hashlib.sha256(data.encode()).hexdigest()

