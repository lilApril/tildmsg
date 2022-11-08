import sys
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFileIconProvider
from tildmsg import Ui_MainWindow
from PIL.ImageQt import ImageQt
from socketmanager import socketprocessor
import os.path
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, loginvalues, socketvalue):
        self.loginvalues = loginvalues
        super().__init__()
        self.setupUi(self)
        self.globalized = 0
        self.dialoguebtn.clicked.connect(self.showdialogue)
        self.closebtn.clicked.connect(self.closebtnevent)
        self.resizebtn.clicked.connect(self.maximize_restore)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.profilebutton.clicked.connect(self.callcontextmenu)
        self.backbtn.clicked.connect(self.calldialoguesmanager)
        self.changeicon.clicked.connect(self.changeiconfunc)
        self.socketmanager = socketvalue
        if os.path.isfile(os.getcwd() + '/tildavatar.png'):
            self.profilebutton.setIcon(QtGui.QIcon('tildavatar.png'))



        def moveWindow(event):
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

        self.titlebar.mouseMoveEvent = moveWindow



    def showdialogue(self):
        anotherid = str(self.socketmanager.idfromnumber(self.searchline.text()).decode('utf-8').strip(')').strip('(').strip(','))
        gottext = self.socketmanager.gettext(self.loginvalues, anotherid).decode('utf-8')
        self.textbrowser.setText(gottext)


    def closebtnevent(self):
        self.socketmanager.ext()
        self.close()

    def maximize_restore(self):
        self.showMinimized()

    def run(self):
        pass

    def changeiconfunc(self):
        fname = QFileDialog.getOpenFileName(self, 'choose icon', '')[0]
        print(fname)
        size = (79, 79)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        im = Image.open(fname)

        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save('tildavatar.png')
        self.profilebutton.setIcon(QtGui.QIcon('tildavatar.png'))

    def showapp(self):
        app = QApplication(sys.argv)
        self.showMaximized()
        app.exec_()

    def calldialoguesmanager(self):
        self.leftpanel.setCurrentIndex(0)
        self.showdialogues()

    def callcontextmenu(self):
        self.leftpanel.setCurrentIndex(1)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

