import sqlite3 as sql
import datetime

con = sql.connect("data.db")
cur = con.cursor()

table = """\
    CREATE TABLE IF NOT EXISTS club
    (
    data_time timestamp,
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
# cur.executescript(table)

dt = datetime.datetime.today()
data_ls = (dt, "IT_Land_Les", 1,2,4,5,6,7,8,9)
data_ak = (dt, "IT_Land_Ak", 1,2,4,5,6,7,8,9)
data_dt = (dt, "IT_Land_Dream", 1,2,4,5,6,7,8,9)
data_troya = (dt, "IT_Land_Troya", 1,2,4,5,6,7,8,9)

ins = 'insert into club values (?,?,?,?,?,?,?,?,?,?)'
for d in [data_ls, data_ak, data_dt, data_troya]:
    cur.execute(ins, d)
con.commit()
cur.close()
con.close()
