
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import datetime

# path = r"D:\Serg\project\pc_club\club_stat\data\data.db"
#
# con = sqlite3.connect(path)
#
# df = pd.read_sql("SELECT data_time, load, taken from club", con)
#
# print(df.loc["24.09.2017"])

# writer = pd.ExcelWriter('output.xlsx')
# df.to_excel(writer,'Sheet1')
# writer.save()

# fields = ["data", "time", "taken"]
# seq = (("24.09.2017", "09:00", 1), ("24.09.2017", "09:00", 2))
# print(pd.DataFrame(list(seq), columns=fields, index=[1,2]))


d1 = datetime.datetime.strptime("24.09.2017 09:00:00", "%d.%m.%Y %H:%M:%S")
d2 = datetime.datetime.strptime("25.09.2017 09:00:00", "%d.%m.%Y %H:%M:%S")
print(d1 < d2)
