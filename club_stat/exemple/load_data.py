
import sqlite3 as sql
import datetime

con = sql.connect("data.db")
cur = con.cursor()

# data_obj = cur.execute("SELECT data_time FROM club")
# for m in data_obj.fetchall():
#     print(m[0])
#
# print("-------------------")
date = "1.09.2017"
dt = datetime.datetime.strptime(date, "%d.%m.%Y").date()
print(dt)

cur.execute('select * from club WHERE dt = ?', (dt,))

for i in cur.fetchall():
    print(i)