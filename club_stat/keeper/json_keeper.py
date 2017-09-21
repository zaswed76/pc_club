
import json


class JsonKeeper:
    def __init__(self, data_file):
        self.data_file = data_file
        self._data = {}


    def write(self):
        with open(self.data_file, 'w') as outfile:
            json.dump(self._data, outfile)

    def load(self):
        with open(self.data_file, "r") as f:
            self._data.update(json.load(f))

    @property
    def data(self):
        return self._data

    def update(self, d):
        self._data.update(d)



