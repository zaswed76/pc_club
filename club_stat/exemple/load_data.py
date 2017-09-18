
import sqlite3 as sql

con = sql.connect("data.db")
cur = con.cursor()

data_obj = cur.execute("SELECT data_time, club, taken FROM club")
for m in data_obj.fetchall():
    print(m)