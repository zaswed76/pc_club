
from datetime import datetime
from sqlite3 import
import os

import itertools

from club_stat.sql import sql_keeper as skp
from club_stat import pth

db__test_time = os.path.join(pth.TEST_DIR, "db__test_time.db")

def create_table(db_path, table):
    kp = skp.Keeper(db_path)
    kp.open_connect()
    kp.open_cursor()
    kp.create_table(table)
    kp.close()

def table():
    table = """\
    CREATE TABLE club
    (
    p1 INTEGER,
    p2 INTEGER,
    current_time TIME DEFAULT CURRENT_TIME
    );
"""
    return table

def ins_():
    return 'insert into club (p1)'

if __name__ == '__main__':

    # create_table(db__test_time, table())
    kp = skp.Keeper(db__test_time)
    kp.open_connect()
    kp.open_cursor()
    #
    # kp.cursor.execute("insert into club (p1, p2) VALUES (1,1)")
    # kp.close()
    # date_time = datetime.now()
    # date = date_time.date()
    # time = str(date_time.time())
    # # hour = time.hour
    # # minute = time.minute
    # print(time)
    # kp.cursor.execute('insert into club values (?)', (time,))
    # kp.close()
    kp.seq_print(kp.sample_all())
    line = '10:36:45'
    tm = datetime.strptime(line, "%H:%M:%S").time()
    print(tm)
    kp.cursor.execute("SELECT * FROM club WHERE current_time = ?", (str(tm),))
    print(kp.cursor.fetchall())
    # # kp.seq_print(kp.sample_all())
