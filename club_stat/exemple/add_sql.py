import sqlite3 as sql
import datetime
from club_stat.exemple import dateex

def table():
    table = """\
    CREATE TABLE IF NOT EXISTS club
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

def dates():
    lst = []
    d = (1, 2, 3 ,4 ,5)
    for i in d:
        strdate = "{}.09.2017".format(i)
        lst.append(datetime.datetime.strptime(strdate, "%d.%m.%Y").date())
    return lst


con = sql.connect("data.db")
cur = con.cursor()
cur.executescript(table())

d = datetime.datetime.now().date()
dt = datetime.datetime.now()
lst = (d, dt, "les", 1, 1,1,1,1,1,1,1)

ins = 'insert into club values (?,?,?,?,?,?,?,?,?,?,?)'
cur.execute(ins, lst)
con.commit()
cur.close()
con.close()


