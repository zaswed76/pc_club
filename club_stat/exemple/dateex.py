

import datetime


s = "2017-09-18 17:56:08.978765"
d1 = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")
print(d1.time())