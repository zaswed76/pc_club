
import collections

class State(collections.Iterator):
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



s = State(range(13))
print(s.state["dt"])
