
import json


class JsonKeeper:
    def __init__(self):
        pass


    def write(self, data, file):
        with open(file, 'w') as outfile:
            json.dump(data, outfile)

    def load(self, file):
        with open(file, "r") as f:
            return json.load(f)

