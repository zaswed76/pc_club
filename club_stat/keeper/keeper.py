
class Keeper:
    def __init__(self, data, keeper):
        self.keeper = keeper
        self.data = data

    def write(self):
        self.keeper.write(self.data)

    def load(self):
        self.keeper.load(self.data)