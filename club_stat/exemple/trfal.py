
import datetime
import collections
from club_stat import pth
from club_stat.sql import sql_keeper



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

    def __call__(self, *args):
        r = []
        for n in args:
            r.append(self.state[n])
        return r


class States:
    def __init__(self, data):
        self.data = [State(x) for x in data]

    def __call__(self, *args):
        r = []
        for x in self.data:
            r.append(x(*args))
        return r




if __name__ == '__main__':
    path = pth.DATA_FILE_2
    kp = sql_keeper.Keeper(path)
    kp.open_connect()
    kp.open_cursor()

    ds = datetime.datetime.strptime("02.10.2017 14:00", "%d.%m.%Y %H:%M")
    de = datetime.datetime.strptime("02.10.2017 18:01", "%d.%m.%Y %H:%M")

    res = kp.sample_range_date(ds, de, "step1")
    st = States(res)

    print((st("visitor", "mhour")))


