
import collections
stat = collections.OrderedDict()

a = [1, 2, 3]

stat_names = ["load", "taken", "free", "guest",
             "resident", "admin", "workers", "school"]

for opt in stat_names:
    stat[opt] = opt

a.extend(stat.values())
print(a)

