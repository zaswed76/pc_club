

import matplotlib.pyplot as plt
import numpy as np


chel = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33,
        13, 11, 6, 20, 18, 21, 14, 14, 17, 8, 7, 6, 7]


r0 = [9, 10, 11, 12, 13, 14, 15,
     16, 17, 18, 19, 20,
     21, 22, 23, 24, 1,
     2, 3, 4, 5,
     6, 7, 8, 9]

r = [str(x) for x in r0]
locs = np.asarray(r0)
locs2 = np.asarray(r)
print(np.array(locs))


width = 0.9


plt.ylim([0, 50])

plt.bar(locs, chel, width=width)


plt.xticks(locs + width*0.005, locs)

for i, v in enumerate(chel):
    plt.text(v, i, str(v), color='blue', fontweight='bold')

plt.show()