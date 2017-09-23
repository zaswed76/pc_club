import datetime

import sqlite3

from club_stat.sql import sql, table


def seq_line():
    d = datetime.datetime.now().date()
    dt = datetime.datetime.now()
    return (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1)


def seq_line_date(date):
    d = datetime.datetime.strptime(date, "%d.%m.%Y").date()
    dt = datetime.datetime.strptime(date, "%d.%m.%Y")
    return (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1)

def seq_line_date_time(date_time):
    dt = datetime.datetime.strptime(date_time, "%d.%m.%Y %H:%M")
    d = dt.date()
    return (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1)



def dates():
    lst = []
    d = (1, 2, 3, 4, 5)
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
        self.cursor.execute("SELECT * FROM club WHERE dt = ?", (d,))
        return self.cursor.fetchall()

    @staticmethod
    def str_to_date(line):
        return datetime.datetime.strptime(line, "%d.%m.%Y").date()

    @staticmethod
    def str_to_date_time(line):
        return datetime.datetime.strptime(line, "%d.%m.%Y %H:%M")

    def samp_range_date(self, date_start, date_end):
        if isinstance(date_start, str) and isinstance(date_end, str):
            start = self.str_to_date(date_start)
            end = self.str_to_date(date_end)
        elif isinstance(date_start, datetime.date) and isinstance(date_end, datetime.date):
            start = date_start
            end = date_end
        self.cursor.execute(
            "SELECT * FROM club WHERE dt BETWEEN ? AND ?", (start, end))
        return self.cursor.fetchall()

    def samp_all(self):
        self.cursor.execute("SELECT * FROM club")
        return self.cursor.fetchall()

    def samp_range_time(self, start, end):
        res = []
        start_date = self.str_to_date_time(start).date()
        end_date = self.str_to_date_time(end).date()

        start_time = self.str_to_date_time(start).time()
        end_time = self.str_to_date_time(end).time()

        range_date = self.samp_range_date(start_date, end_date)
        for line in range_date:
            sql_time = datetime.datetime.strptime(line[1], "%Y-%m-%d %H:%M:%S").time()
            if start_time <= sql_time <= end_time:
                res.append(line)
        return tuple(res)



if __name__ == '__main__':
    # region открыть базу
    path = "data.db"
    kp = Keeper(path)
    kp.open_connect()
    kp.open_cursor()
    # endregion

    s = kp.samp_range_time("28.09.2017 12:00", "28.09.2017 18:00")
    Keeper.seq_print(s)
    # Keeper.seq_print(kp.samp_range_date("24.09.2017", "26.09.2017"))

    # start_date = Keeper.str_to_date("24.09.2017")
    # end_date = Keeper.str_to_date("24.09.2017")
    # Keeper.seq_print(kp.samp_range_date(start_date, end_date))

    # Keeper.seq_print(kp.samp_all())

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

    # region добавить даты
    # kp.add_line(table.ins_club_stat(), seq_line_date("24.09.2017"))
    # kp.add_line(table.ins_club_stat(), seq_line_date("25.09.2017"))
    # kp.add_line(table.ins_club_stat(), seq_line_date("26.09.2017"))
    # kp.add_line(table.ins_club_stat(), seq_line_date("27.09.2017"))
    # endregion

    # region добавить даты + вермя
    # times = (9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
    # for t in times:
    #     kp.add_line(table.ins_club_stat(),  seq_line_date_time("28.09.2017 {}:00".format(t)))

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
