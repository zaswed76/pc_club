from datetime import datetime
import os

import itertools

from club_stat.sql import sql_keeper as skp
from club_stat import pth

test_db_1 = os.path.join(pth.TEST_DIR, "db_1.db")

def create_table(db_path, table):
    kp = skp.Keeper(db_path)
    kp.open_connect()
    kp.open_cursor()
    kp.create_table(table)
    kp.close()

def str_to_datetime(date, hour):
    return datetime.strptime("{date} {hour}:00".format(date=date, hour=hour), "%d.%m.%Y %H:%M")

def add_note(kp, table):
    t_int = list(itertools.chain(range(9, 24), range(0, 10)))
    hour_str = ["{number:02}".format(number=x) for x in t_int]


    date_start = "29.09.2017"
    date_end = "30.09.2017"
    midnight_flag = False
    for h in hour_str:

        if not midnight_flag:
            d = date_start
            dt = str_to_datetime(date_start, h)
            if h == "00":
                midnight_flag = True
        else:
            d = date_end
            dt = str_to_datetime(date_end, h)
        seq = (d, dt, "les", 1, 1, 1, 1, 1, 1, 1, 1, 1)
        kp.add_line(skp.ins_club_stat(), seq)
    kp.close()


    # for t in times:
    #     kp.add_line(table.ins_club_stat(),  seq_line_date_time("28.09.2017 {}:00".format(t)))
    # kp.add_line(table.ins_club_stat(), note_seq)



if __name__ == '__main__':
    # kp = skp.Keeper(test_db_1)
    # kp.open_connect()
    # kp.open_cursor()
    # add_note(kp, skp.table())

    # create_table(test_db_1, skp.table())

    kp = skp.Keeper(test_db_1)
    kp.open_connect()
    kp.open_cursor()
    kp.seq_print(kp.sample_all())
