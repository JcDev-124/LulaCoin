import hashlib
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        data_to_hash = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode('utf-8')
        sha.update(data_to_hash)
        return sha.hexdigest()

