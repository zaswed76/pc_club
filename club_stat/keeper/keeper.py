
class Keeper:
    def __init__(self,  keeper):
        self.keeper = keeper


    def write(self, data, file):
        self.keeper.write(data)

    def load(self, file):
        self.keeper.load(file)