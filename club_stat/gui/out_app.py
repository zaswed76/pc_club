import os
import sys
import datetime
import tempfile

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QDate, QDateTime
from club_stat.sql import sql_keeper
from club_stat import mstat
from club_stat.gui.graph import graph
from club_stat import club
import numpy as np

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
    def __init__(self, db_path, clubs_object):
        super().__init__()
        self.clubs_object = clubs_object
        self.pxm = None
        self.current_club_name = None
        self.db_path = db_path
        self.resize(500, 500)
        self.form = uic.loadUi(ui_pth, self)
        self.setWindowTitle("Форма вывода")

        yesterday_dt = datetime.datetime.now() - datetime.timedelta(
            days=1)
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

        self.form.les.toggled.connect(self.update_graph)
        self.form.akadem.toggled.connect(self.update_graph)
        self.form.troya.toggled.connect(self.update_graph)
        self.form.dream.toggled.connect(self.update_graph)

        self.form.export_to_png.clicked.connect(self._export_to_png)

        self.time_steps = {
            self.form.step1.objectName(): self.form.step1,
            self.form.step2.objectName(): self.form.step2,
            self.form.step30.objectName(): self.form.step30
        }

        self.clubs = {
            self.form.les.objectName(): self.form.les,
            self.form.akadem.objectName(): self.form.akadem,
            self.form.troya.objectName(): self.form.troya,
            self.form.dream.objectName(): self.form.dream
        }

    def update_graph(self):
        dt_start = self.form.dt_start_edit.dateTime().toPyDateTime()
        dt_end = self.form.dt_end_edit.dateTime().toPyDateTime()
        time_step = self.get_time_step()
        self.current_club_name = self.get_current_club()

        keep = sql_keeper.Keeper(self.db_path)
        keep.open_connect()
        keep.open_cursor()
        res = keep.sample_range_date(dt_start, dt_end, time_step,
                                     self.current_club_name)
        stat_obj = mstat.States(res)
        time_lst, mans = mstat.resort(stat_obj("mhour", "visitor"))

        if len(time_lst) <= 24:
            times = ["{number:02}".format(number=x) for x in time_lst]
        else:
            times = rs(time_lst)
        self.form.graph_lb.clear()
        try:
            club = self.get_club_on_field(self.current_club_name)
            gr = graph.Graph(times, mans, "время", "человек",
                             width=0.8, title=self.current_club_name, max=club.max_visitor)
        except TypeError:
            pass
        else:
            temp = tempfile.mkstemp()[1] + ".png"
            gr.save(temp)

            self.pxm = QtGui.QPixmap(temp)

            self.form.graph_lb.setPixmap(self.pxm)

    def _export_to_png(self):
        if self.pxm is not None:
            img_name = self.current_club_name + ".png"
            desktop_file = os.path.expanduser(os.path.join("~/Desktop/", img_name))
            self.pxm.save(desktop_file, "PNG")

    def set_step(self, step_name):
        getattr(self.form, step_name).setChecked(True)

    def set_club(self, club_name):
        getattr(self.form, club_name).setChecked(True)

    def get_time_step(self):
        for n in self.time_steps:
            if self.time_steps[n].isChecked():
                return n

    def get_current_club(self):
        for n in self.clubs:
            if self.clubs[n].isChecked():
                return club.Club.get_field_by_name(n)

    def get_club_on_field(self, field):
        for club in self.clubs_object.values():
            if club.field_name == field:
                return club






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = OutApp()
    main.show()
    sys.exit(app.exec_())
