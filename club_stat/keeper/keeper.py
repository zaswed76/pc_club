import datetime


class Keeper:
    def __init__(self,  keeper):
        self.keeper = keeper


    def write(self):
        self.keeper.write()

    def load(self):
        self.keeper.load()

    @property
    def data(self):
        return self.keeper.data

    def update(self, data):
        self.keeper.update(data)

if __name__ == '__main__':
    from club_stat.keeper import json_keeper
    f = r"D:\Serg\project\pc_club\club_stat\data\data.JSON"
    json_keep = json_keeper.JsonKeeper(f)
    kp = Keeper(json_keep)
    print(kp.data)
    data = {}
    d = datetime.datetime.now()
    dt = d.date().strftime('%Y-%m-%d')

    tm = d.time().strftime('%H-%M-%S.%f')
    print(tm)
    data[dt] = {tm: 3}
    kp.update(data)
    kp.write()