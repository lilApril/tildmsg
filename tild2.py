import sys
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from PyQt5 import QtCore, QtGui, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QFileIconProvider
from tildmsg import Ui_MainWindow
from PIL.ImageQt import ImageQt
from socketmanager import socketprocessor
import os.path
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QListWidget, QListWidgetItem, QHBoxLayout, QLayout
from PyQt5.QtWidgets import QInputDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    # инициализация окна, установка аватара профиля и вкладок чатов в чатлист
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
        self.prpressed = False
        self.addnewgroup.clicked.connect(self.addgroup)
        self.backbtn.clicked.connect(self.calldialoguesmanager)
        self.changeicon.clicked.connect(self.changeiconfunc)
        self.socketmanager = socketvalue
        if os.path.isfile(os.getcwd() + '/' + self.loginvalues + '.png'):
            self.profilebutton.setIcon(QtGui.QIcon(f'{self.loginvalues}.png'))
        self.textbrowser.setAlignment(QtCore.Qt.AlignLeft)
        self.textbrowser.setAlignment(QtCore.Qt.AlignTop)
        self.quitacc.clicked.connect(self.exitacc)
        self.chatname = self.loginvalues
        self.sendbtn.setEnabled(0)
        self.dialogues = []
        self.chats = []
        self.changename.clicked.connect(self.changenamefunc)
        self.changepassword.clicked.connect(self.changepasswordfunc)
        self.changenumber.clicked.connect(self.changenumberfunc)
        for i in self.socketmanager.getids(self.loginvalues).decode('utf-8').split('|'):
            if str(i).isalnum():
                self.dialogues.append(self.socketmanager.getloginfromid(i).decode('utf-8') + '|' + str(i))
            else:
                self.chats.append(str(i))
        if len(self.chats) == 0:
            self.chats.extend(self.socketmanager.getgroups(self.loginvalues).decode('utf-8').split('|'))
        self.sendbtn.clicked.connect(self.sendmessage)
        self.dialoguelist.addItems(self.chats + self.dialogues)

        # инструкция к событию передвижения окна
        def moveWindow(event):
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

        self.titlebar.mouseMoveEvent = moveWindow

    # ============================================================================
    # Функции диалогов контекстного меню
    def addgroup(self):
        name, ok_pressed = QInputDialog.getText(self, "",
                                                "Название группы:")
        if not any(map(str.isdigit, name)):
            name = name.replace('|', '')
            if ok_pressed and name != 'empty':
                self.socketmanager.addgroup(self.loginvalues, name)
        self.dialogues = []
        self.chats = []
        for i in self.socketmanager.getids(self.loginvalues).decode('utf-8').split('|'):
            if str(i).isalnum():
                self.dialogues.append(self.socketmanager.getloginfromid(i).decode('utf-8') + '|' + str(i))
            else:
                self.chats.append(str(i))
        if len(self.chats) == 0:
            self.chats.extend(self.socketmanager.getgroups(self.loginvalues).decode('utf-8').split('|'))
        self.dialoguelist.clear()
        self.dialoguelist.addItems(self.chats + self.dialogues)

    def changenamefunc(self):
        name, ok_pressed = QInputDialog.getText(self, "",
                                                "Введите новый логин:")
        name = name.replace('|', '')

        if ok_pressed:
            self.socketmanager.setlogin(name, self.loginvalues)

    def changepasswordfunc(self):
        name, ok_pressed = QInputDialog.getText(self, "",
                                                "Введите новый пароль:")
        name = name.replace('|', '')

        if ok_pressed:
            self.socketmanager.setpassword(name, self.loginvalues)

    def changenumberfunc(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Введите новый номер:")
        if name.isnumeric():
            name = name.replace('|', '')
            if ok_pressed:
                self.socketmanager.setnumber(name, self.loginvalues)

    # ============================================================================
    # Функция, отвечающая за отображение содержимого чата и отображение чатов в чатлисте
    def showdialogue(self):
        self.stackedWidget.setCurrentIndex(1)
        if len(self.searchline.text()) > 0 and '|' not in self.searchline.text():
            self.anotherid = str(self.socketmanager.idfromnumber(self.searchline.text()).decode('utf-8'))
            if self.anotherid != 'empty':
                gottext = self.socketmanager.gettext(self.loginvalues, self.anotherid).decode('utf-8')
                self.textbrowser.setText(gottext)
                self.chatname = self.socketmanager.getchatname(self.loginvalues, self.anotherid).decode('utf-8')
                if '|' in self.chatname:
                    self.chatname = self.anotherid
                self.sendbtn.setEnabled(1)
        elif '|' not in self.searchline.text():
            self.anotherid = self.dialoguelist.currentItem().text().split('|')[1] if len(
                self.dialoguelist.currentItem().text().split('|')) > 1 else self.dialoguelist.currentItem().text()
            if self.anotherid != 'empty':
                gottext = self.socketmanager.gettext(self.loginvalues, self.anotherid).decode('utf-8')
                self.textbrowser.setText(gottext)
                self.chatname = self.socketmanager.getchatname(self.loginvalues, self.anotherid).decode('utf-8')
                if '|' in self.chatname:
                    self.chatname = self.anotherid
                self.sendbtn.setEnabled(1)
        self.dialogues = []
        self.chats = []
        for i in self.socketmanager.getids(self.loginvalues).decode('utf-8').split('|'):
            if str(i).isalnum():
                self.dialogues.append(self.socketmanager.getloginfromid(i).decode('utf-8') + '|' + str(i))
            else:
                self.chats.append(str(i))
        if len(self.chats) == 0:
            self.chats.extend(self.socketmanager.getgroups(self.loginvalues).decode('utf-8').split('|'))
        self.dialoguelist.clear()
        self.dialoguelist.addItems(self.chats + self.dialogues)

    # Функция отправки сообщения
    def sendmessage(self):
        self.socketmanager.sendmessage(self.loginvalues, self.chatname, self.stringfield.toPlainText().replace('|', ''))
        self.textbrowser.setText(self.socketmanager.gettext(self.loginvalues, self.chatname).decode('utf-8'))
        self.stringfield.setText('')
        self.dialogues = []
        self.chats = []
        for i in self.socketmanager.getids(self.loginvalues).decode('utf-8').split('|'):
            if str(i).isalnum():
                self.dialogues.append(self.socketmanager.getloginfromid(i).decode('utf-8') + '|' + str(i))
            else:
                self.chats.append(str(i))
        if len(self.chats) == 0:
            self.chats.extend(self.socketmanager.getgroups(self.loginvalues).decode('utf-8').split('|'))
        self.dialoguelist.clear()
        self.dialoguelist.addItems(self.chats + self.dialogues)

    # Событие нажатия на круглую красную кнопку в правом верхнем углу
    def closebtnevent(self):
        self.socketmanager.ext()
        self.close()

    # Событие нажатия на круглую синюю кнопку в правом верхнем углу
    def maximize_restore(self):
        self.showMinimized()

    # Контекстное меню: поменять аватар профиля
    def changeiconfunc(self):
        fname = QFileDialog.getOpenFileName(self, 'choose icon', '')[0]
        size = (79, 79)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        im = Image.open(fname)

        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save(f'{self.loginvalues}.png')
        self.profilebutton.setIcon(QtGui.QIcon(f'{self.loginvalues}.png'))

    # К этому методу обращается tild1.py чтобы запустить приложение
    def showapp(self):
        app = QApplication(sys.argv)
        self.show()
        app.exec_()
        self.close()

    # Закрытие контекстного меню
    def calldialoguesmanager(self):
        self.leftpanel.setCurrentIndex(0)

    # Открытие контекстного меню
    def callcontextmenu(self):
        self.leftpanel.setCurrentIndex(1)

    # Отвечает за перемещение окна
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # Контекстное мени Quit from account
    def exitacc(self):
        os.startfile(os.getcwd() + '/' + 'tild1.py')
        self.close()
