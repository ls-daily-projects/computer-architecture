class RAM():
    """CPU's RAM"""

    def __init__(self, size=0xFF):
        self.size = size
        self.storage = [0b0] * self.size

    def __len__(self):
        return self.size

    def write(self, address, value):
        self.storage[address] = value
        return self

    def read(self, address):
        return self.storage[address]
