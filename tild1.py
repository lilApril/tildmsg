import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import Qt, QtCore
from tildwidget import Ui_Form
from tild2 import MainWindow
from socketmanager import socketprocessor


profileid = ''

class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        self.globalized = 0
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.log_in)
        self.pushButton_2.clicked.connect(self.register)
        self.ended = False
        self.login_string_marker = 1
        self.password_string_marker = 1
        self.mobile_string_marker = 1
        self.lineEdit.textChanged.connect(self.login)
        self.lineEdit_2.textChanged.connect(self.password)
        self.lineEdit_3.textChanged.connect(self.mobilephonenumber)
        self.closebtn.clicked.connect(self.closebtnevent)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def moveWindow(event):
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

        self.titlebar.mouseMoveEvent = moveWindow
        self.socketmanagement = socketprocessor()

    def closebtnevent(self):
        self.socketmanagement.ext()
        sys.exit()

    def log_in(self):
        global profileid
        profileid = str(self.socketmanagement.getprofile(login=self.lineEdit.text(), password=self.lineEdit_2.text(),
                                                     number=self.lineEdit_3.text()).decode('utf-8').strip('(').strip(')').strip(','))
        if (not (self.login_string_marker and self.password_string_marker)) and len(profileid) > 0 and profileid != '|':
            self.ended = True
            self.close()
        elif profileid.decode('utf-8') == '|':
            self.lineEdit.setText('<incorrect> login')
            self.lineEdit_2.setText('<incorrect> password')
            self.lineEdit_3.setText('<incorrect> number')
            self.login_string_marker = 1
            self.password_string_marker = 1
            self.mobile_string_marker = 1


    def register(self):
        if (not (self.login_string_marker and self.password_string_marker)):
            self.ended = True
            self.socketmanagement.registration(self.lineEdit, self.lineEdit_2, self.lineEdit_3)
            self.close()

    def mobilephonenumber(self):
        if self.mobile_string_marker:
            self.mobile_string_marker = 0
            self.lineEdit_3.setText(self.lineEdit_3.text()[-1])

    def password(self):
        if self.password_string_marker:
            self.password_string_marker = 0
            self.lineEdit_2.setText(self.lineEdit_2.text()[-1])

    def login(self):
        if self.login_string_marker:
            self.login_string_marker = 0
            self.lineEdit.setText(self.lineEdit.text()[-1])

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    app.exec_()
    if ex.ended:
        print(profileid)
        MainWindow(profileid, ex.socketmanagement).showapp()

