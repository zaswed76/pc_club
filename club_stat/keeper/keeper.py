
class Keeper:
    def __init__(self,  keeper):
        self.keeper = keeper


    def write(self, data, file):
        self.keeper.write(data, file)

    def load(self, file):
        return self.keeper.load(file)