
import json


class JsonKeeper:
    def __init__(self):
        self._data = {}


    def write(self, data, file):
        with open(file, 'w') as outfile:
            json.dump(self._data, outfile)

    def load(self, file):
        with open(file, "r") as f:
            self._data.update(json.load(f))

    @property
    def data(self):
        return self._data



