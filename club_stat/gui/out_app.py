import os
import sys
import datetime
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QDate, QDateTime
from club_stat.sql import sql_keeper

root = os.path.join(os.path.dirname(__file__))
ui_pth = os.path.join(root, "ui/out_form.ui")

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

        t_step = datetime.datetime.strptime("01:00:00", "%H:%M:%S").time()
        self.form.step_edit.setTime(t_step)

        update_btn_size = QtCore.QSize(22, 22)
        self.form.update_graph_btn.clicked.connect(self.update_graph)
        self.form.update_graph_btn.setIconSize(update_btn_size)
        self.form.update_graph_btn.setFixedSize(update_btn_size)

    def update_graph(self):
        dt_start = self.form.dt_start_edit.dateTime().toPyDateTime()
        keep = sql_keeper.Keeper(self.db_path)
        keep.open_connect()
        keep.open_cursor()
        res = keep.sample_range_date(dt_start, dt_start)
        for i in res:
            print(i)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = OutApp()
    main.show()
    sys.exit(app.exec_())