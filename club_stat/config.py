
import json


def save(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

def load(path):
    with open(path, "r") as f:
        return json.load(f)