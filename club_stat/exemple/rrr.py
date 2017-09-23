

import datetime

l = "23.09.2017 09:00"
dt = datetime.datetime.strptime(l, "%d.%m.%Y %H:%M").date()

print(type(dt))




