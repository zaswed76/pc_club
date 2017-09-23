import datetime

import sqlite3

from club_stat.sql import sql, table

def seq_line():
    d = datetime.datetime.now().date()
    dt = datetime.datetime.now()
    return (d, dt, "les", 1, 1,1,1,1,1,1,1)

def seq_line_date(date):
    d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
    dt = datetime.datetime.strptime(date, "%d.%m.%Y")
    return (d, dt, "les", 1, 1,1,1,1,1,1,1)

def dates():
    lst = []
    d = (1, 2, 3 ,4 ,5)
    for i in d:
        strdate = "{}.09.2017".format(i)
        lst.append(datetime.datetime.strptime(strdate, "%d.%m.%Y").date())
    return lst


class Keeper():

    def __init__(self, path):
        self.path = path

    def create_table(self, table):
        self.cursor.executescript(table)

    def add_line(self, ins, seq):
         self.cursor.execute(ins, seq)

    def open_connect(self):
        self.connect = sqlite3.connect(self.path)

    def open_cursor(self):
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()

    @staticmethod
    def seq_print(seq):
        for i in seq:
            print(i)

    def samp_date(self, date):
        d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
        self.cursor.execute("select * from club WHERE dt = ?", (d,))
        return self.cursor.fetchall()

    def samp_range_time(self):
        pass



if __name__ == '__main__':
    path = "data.db"
    kp = Keeper(path)
    kp.open_connect()
    kp.open_cursor()
    # res = kp.samp_date("23.09.2017")
    # Keeper.seq_print(res)
    # date = "23.09.2017"
    # tm = "11:39:24"
    # t = datetime.datetime.strptime(tm, "%H:%M:%S").time()
    # d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
    # kp.cursor.execute("select * from club")
    # for i in kp.cursor.fetchall():
    #     dt_t = i[1]
    #     sql_time = datetime.datetime.strptime(dt_t, "%Y-%m-%d %H:%M:%S.%f").time()
    #     print(dt_t)

    # region Description
    kp.add_line(table.ins_club_stat(), seq_line_date("24.09.2017"))
    kp.add_line(table.ins_club_stat(), seq_line_date("25.09.2017"))
    kp.add_line(table.ins_club_stat(), seq_line_date("26.09.2017"))
    kp.add_line(table.ins_club_stat(), seq_line_date("27.09.2017"))
    # endregion

    # # # kp.create_table(table.table())
    kp.close()
    # # dt_tm = datetime.datetime.strptime('2017-09-23 11:39:24.000000', "%Y-%m-%d %H:%M:%S.%f")
    # ttt = '2017-09-23 15:00:00'
    # dt_tm = datetime.datetime.strptime(ttt, "%Y-%m-%d %H:%M:%S").hour
    # # print(dt_tm, 888)
    # kp.cursor.execute("select * from club WHERE dt > ?", (dt_tm,))
    # print("--------------")
    # Keeper.seq_print(kp.cursor.fetchall())
    # print("-------------------")
