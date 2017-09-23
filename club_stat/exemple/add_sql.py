import sqlite3 as sql
import datetime
from club_stat.exemple import dateex






def add_ins():
    pass

def add_table():
    con = sql.connect("data.db")
    cur = con.cursor()
    cur.executescript(table())
    con.commit()
    cur.close()
    con.close()






