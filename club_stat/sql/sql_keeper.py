import datetime

import sqlite3

def table():
    table = """\
    CREATE TABLE club
    (
    dt date,
    data_time timestam,
    club TEXT,
    load INTEGER,
    taken INTEGER,
    free INTEGER,
    guest INTEGER,
    resident INTEGER,
    admin INTEGER,
    workers INTEGER,
    school INTEGER
    );
"""
    return table

def ins_club_stat():
    return 'insert into club values (?,?,?,?,?,?,?,?,?,?,?)'

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

        try:
            self.cursor.executescript(table)
        except sqlite3.OperationalError:
            pass

    def add_line(self, ins, seq):
        self.cursor.execute(ins, seq)

    def open_connect(self):
        self.connect = sqlite3.connect(self.path)

    def open_cursor(self):
        self.cursor = self.connect.cursor()

    def commit(self):
        self.connect.commit()

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
        self.cursor.execute("SELECT data_time, taken FROM club WHERE dt = ?", (d,))
        return self.cursor.fetchall()

    @staticmethod
    def str_to_date(line):
        return datetime.datetime.strptime(line, "%d.%m.%Y").date()

    @staticmethod
    def str_to_date_time(line):

        return datetime.datetime.strptime(line, "%d.%m.%Y %H:%M:%S")

    def sample_range_date(self, date_start, date_end):
        if isinstance(date_start, str) and isinstance(date_end, str):
            start = self.str_to_date(date_start)
            end = self.str_to_date(date_end)
        elif isinstance(date_start, datetime.date) and isinstance(date_end, datetime.date):
            start = date_start
            end = date_end
        self.cursor.execute(
            "SELECT data_time, taken FROM club WHERE dt BETWEEN ? AND ?", (start, end))
        return self.cursor.fetchall()

    def sample_all(self):
        self.cursor.execute("SELECT * FROM club")
        return self.cursor.fetchall()

    def sample_range_time(self, start, end, sample_hour=False):
        res = []
        start_date_time = self.str_to_date_time(start)
        start_date = start_date_time.date()
        end_date_time = self.str_to_date_time(end)
        end_date = end_date_time.date()

        start_time = self.str_to_date_time(start).time()
        end_time = self.str_to_date_time(end).time()

        range_date = self.sample_range_date(start_date, end_date)

        for line in range_date:
            sql_date = datetime.datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S.%f")
            sql_time = sql_date.time()
            #
            # if (sql_time <
            #         datetime.datetime.strptime("23:59:59", "%H:%M:%S").time()):
            #     print(start_time, sql_time, end_time)
            if start_date_time <= sql_date <= end_date_time:
                if sample_hour:
                    if sql_time.minute == 0:
                        res.append(line)
                else:
                    res.append(line)
        print(res)
        return tuple(res)

    def sample_hour(self, start, end):
        return self.sample_range_time(start, end, sample_hour=True)




if __name__ == '__main__':
    # region открыть базу
    # path = "data.db"
    path = r"D:\Serg\project\pc_club\club_stat\data\data.db"
    kp = Keeper(path)
    kp.open_connect()
    kp.open_cursor()
    # Keeper.seq_print(kp.sample_all())
    # region Description
    r = kp.sample_hour("24.09.2017 09:00:00", "25.09.2017 09:00:00")

    lst = []
    for line in r:
        ln = list(line)
        st = ln[0]
        t = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S.%f").time()
        new_t = t.strftime("%H")
        ln[0] = new_t
        lst.append(ln)

    import pandas as pd
    df = pd.DataFrame(lst)

    writer = pd.ExcelWriter('output.xlsx')
    df.to_excel(writer,'Sheet1')
    writer.save()
    # endregion
    # endregion

    # s = kp.sample_range_time("24.09.2017 12:00", "24.09.2017 18:00")
    # Keeper.seq_print(s)
    # Keeper.seq_print(kp.sample_range_date("24.09.2017", "26.09.2017"))

    # start_date = Keeper.str_to_date("24.09.2017")
    # end_date = Keeper.str_to_date("24.09.2017")
    # Keeper.seq_print(kp.sample_range_date(start_date, end_date))

    # Keeper.seq_print(kp.sample_all())

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

    # kp.create_table(table())
    kp.close()
