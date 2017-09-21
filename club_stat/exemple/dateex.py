import datetime

def test_create_table():
    dates = []
    days = [21, 22, 23, 24, 25]
    for d in days:
        date = "2017-09-{} 00:00:00.000000".format(d)
        dobj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        dates.append(dobj)
    return dates


t1 = datetime.date.today()
s = "2017-09-21"
t2 = datetime.datetime.strptime(s, "%Y-%m-%d")

print(t1 == t2)
