import os
import sys
import datetime
import tempfile

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QDate, QDateTime
from club_stat.sql import sql_keeper
from club_stat import mstat
from club_stat.gui.graph import graph
from club_stat import pth

root = os.path.join(os.path.dirname(__file__))
ui_pth = os.path.join(root, "ui/out_form.ui")

def rs(lst):
    res = []
    for i in lst:
        if not i in res:
            res.append(i)
        else:
            res.append("")
    return res

class OutApp(QtWidgets.QWidget):
    def __init__(self, db_path):
        super().__init__()
        self.db_path = db_path
        self.resize(500, 500)
        self.form = uic.loadUi(ui_pth, self)
        self.setWindowTitle("Форма вывода")

        yesterday_dt = datetime.datetime.now() - datetime.timedelta(days=1)
        d_start = yesterday_dt.date()
        t_start = datetime.datetime.strptime("09:00", "%H:%M").time()
        self.form.dt_start_edit.setDate(d_start)
        self.form.dt_start_edit.setTime(t_start)

        current_dt = datetime.datetime.now()
        d_end = current_dt.date()
        t_end = datetime.datetime.strptime("09:00", "%H:%M").time()
        self.form.dt_end_edit.setDate(d_end)
        self.form.dt_end_edit.setTime(t_end)

        update_btn_size = QtCore.QSize(22, 22)
        self.form.update_graph_btn.clicked.connect(self.update_graph)
        self.form.update_graph_btn.setIconSize(update_btn_size)
        self.form.update_graph_btn.setFixedSize(update_btn_size)




        self.time_steps = {
            self.form.step1.objectName(): self.form.step1,
            self.form.step2.objectName(): self.form.step2,
            self.form.step30.objectName(): self.form.step30
                           }



    def update_graph(self):
        dt_start = self.form.dt_start_edit.dateTime().toPyDateTime()
        dt_end = self.form.dt_end_edit.dateTime().toPyDateTime()
        time_step = self.get_time_step()

        keep = sql_keeper.Keeper(self.db_path)
        keep.open_connect()
        keep.open_cursor()
        res = keep.sample_range_date(dt_start, dt_end, time_step)
        stat_obj = mstat.States(res)
        time_lst, mans = mstat.resort(stat_obj("mhour", "visitor"))


        if len(time_lst) <= 24:
            times = ["{number:02}".format(number=x) for x in time_lst]
        else:
            times = rs(time_lst)

        try:
            gr = graph.Graph(times, mans, "время", "человек", width=0.8, title="Lesnoy")
        except TypeError:
            pass
        else:
            temp = tempfile.mkstemp()[1] + ".png"
            gr.save(temp)
            self.form.graph_lb.clear()
            pxm = QtGui.QPixmap(temp)
            self.form.graph_lb.setPixmap(pxm)
            self.form.graph_lb.resize(pxm.size())
            self.form.graph_lb.setScaledContents(True)
            # self.form.graph_lb.setMinimumSize(pxm.size())
            # QtWidgets.QLabel


    def set_step(self, step_name):
        getattr(self.form, step_name).setChecked(True)

    def get_time_step(self):
        for n in self.time_steps:
            if self.time_steps[n].isChecked():
                return n





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = OutApp()
    main.show()
    sys.exit(app.exec_())