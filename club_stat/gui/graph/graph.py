

import pandas as pd
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, times, human, x_lb, y_lb, width = 0.5, title=""):
        self.title = title
        self.width = width
        self.y_lb = y_lb
        self.x_lb = x_lb
        self.human = human
        self.times = times

        self.create_plot()

    def create_plot(self):
        freq_series = pd.Series.from_array(self.human)
        self.ax = freq_series.plot(kind='bar', width = 0.8)
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_lb)
        self.ax.set_ylabel(self.y_lb)
        self.ax.set_xticklabels(times)
        plt.ylim([0, 50])
        rects = self.ax.patches


        for rect, label in zip(rects, self.human):
            height = rect.get_height()
            self.ax.text(rect.get_x() + rect.get_width()/2, height + 0.4,
                    label, ha='center', va='bottom')

    def show(self):
        plt.show()

    def save(self, path):
        plt.savefig(path)

if __name__ == '__main__':
    mans = [6, 7, 8, 9, 10, 15, 17, 12, 16, 7, 3, 7, 8,
               6, 7, 8, 9, 10, 15, 17, 12, 16, 7, 3]
    x_labels0 = ["{number:02}".format(number=x) for x in list(range(9, 25))]
    x_labels1 = ["{number:02}".format(number=x) for x in list(range(1, 10))]
    times = []
    times.extend(x_labels0)
    times.extend(x_labels1)
    gr = Graph(times, mans, "время", "человек", width=0.8, title="Lesnoy")
    gr.save("aaa.png")