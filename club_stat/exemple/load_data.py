
import sqlite3 as sql
import datetime

con = sql.connect("data.db")
cur = con.cursor()

# data_obj = cur.execute("SELECT data_time FROM club")
# for m in data_obj.fetchall():
#     print(m[0])
#
# print("-------------------")

t = datetime.datetime(2017, 9, 22, 1, 00, 00, 0)

cur.execute('select * from club WHERE data_time = ? AND club="IT_Land_Les"', (t,))
for i in cur.fetchall():
    print(i)