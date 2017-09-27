import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

frequencies = [6, 7, 8, 9, 10, 15, 17, 12, 16, 7, 3, 7, 8,
               6, 7, 8, 9, 10, 15, 17, 12, 16, 7, 3]   # bring some raw data

freq_series = pd.Series.from_array(frequencies)   # in my original code I create a series and run on that, so for consistency I create a series from the list.

x_labels0 = ["{number:02}".format(number=x) for x in list(range(9, 25))]
x_labels1 = ["{number:02}".format(number=x) for x in list(range(1, 10))]
x_labels = []
x_labels.extend(x_labels0)
x_labels.extend(x_labels1)

# now to plot the figure...
# plt.figure(figsize=(10, 5))
ax = freq_series.plot(kind='bar')
ax.set_title("")
ax.set_xlabel("время")
ax.set_ylabel("Человек")
ax.set_xticklabels(x_labels)
plt.ylim([0, 50])
rects = ax.patches

# Now make some labels
labels = [i for i in frequencies]

for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height + 0.3, label, ha='center', va='bottom')

# plt.show()
plt.savefig("image.png")