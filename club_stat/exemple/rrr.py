


import sys
from PyQt5 import QtWidgets as QtGui
from PyQt5 import QtCore as QtCore

class X(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.label = QtGui.QLabel(self)
		self.setCentralWidget(self.label)
		dialog = Dialog(self)
		dialog.signal.connect(self.slot)
		dialog.show()

	def slot(self):
		self.label.setText(self.label.text()+u"Обломись баклан!\n")

class Dialog(QtGui.QDialog):
	signal = QtCore.Signal()
	def __init__(self, parent):
		QtGui.QDialog.__init__(self, parent)
		self.knopka = QtGui.QPushButton(self)
		self.knopka.setText(u"Нажми меня")
		self.knopka.clicked.connect(self.signal)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	win = X()
	win.show()
	sys.exit(app.exec_())