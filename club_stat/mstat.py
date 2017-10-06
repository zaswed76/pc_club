import collections

def resort(lst):
    t = []
    m = []
    for req in lst:
        t.append(req[0])
        m.append(req[1])
    return (t, m)

class MState(collections.Iterator):
    s = ["dt",
    "data_time",
    "mhour",
    "mminute",
    "club",
    "load",
    "taken",
    "free",
    "guest",
    "resident",
    "admin",
    "workers",
    "school",
    "visitor"]
    def __init__(self, state):
        self.value = 0
        self.stop = len(self.s)
        self.state = {}
        for n, v in zip(self.s, state):
            self.state[n] = v

    def __next__(self):
        if self.value == self.stop:
            raise  StopIteration
        st = self.s[self.value]
        self.value += 1
        return st

    def __call__(self, *args):
        r = []
        for n in args:
            r.append(self.state[n])
        return r


class States:
    def __init__(self, data):
        self.data = [MState(x) for x in data]

    def __call__(self, *args):
        r = []
        for x in self.data:
            r.append(x(*args))
        return r
