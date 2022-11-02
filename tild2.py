import sys

from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFileIconProvider
from tildmsg import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, loginvalues):
        self.loginvalues = loginvalues
        super().__init__()
        self.setupUi(self)
        self.globalized = 0
        self.closebtn.clicked.connect(self.closebtnevent)
        self.resizebtn.clicked.connect(self.maximize_restore)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.profilebutton.clicked.connect(self.callcontextmenu)
        self.backbtn.clicked.connect(self.calldialoguesmanager)
        self.changeicon.clicked.connect(self.changeiconfunc)
        def moveWindow(event):
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
        self.titlebar.mouseMoveEvent = moveWindow

    def closebtnevent(self):
        sys.exit()
    def maximize_restore(self):
        if not self.globalized:
            self.showMaximized()
            self.resizebtn.setToolTip('Restore')
            self.globalized = 1

        else:
            self.globalized = 0
            self.showNormal()
            self.resizebtn.setToolTip("Maximize")

    def run(self):
        pass

    def changeiconfunc(self):
        fname = QtGui.QIcon(QFileDialog.getOpenFileName(self, 'Выберите файл-инициализатор L-системы', '')[0])
        self.profilebutton.setIcon(fname)
    def showapp(self):
        app = QApplication(sys.argv)
        self.showMaximized()
        app.exec_()

    def calldialoguesmanager(self):
        self.leftpanel.setCurrentIndex(0)

    def callcontextmenu(self):
        self.leftpanel.setCurrentIndex(1)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

