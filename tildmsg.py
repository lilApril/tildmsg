# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tildmsg.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 551)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.frame.setMaximumSize(QtCore.QSize(1920, 1080))
        self.frame.setStyleSheet("background-color: rgb(16, 16, 36);\n"
"border: none;\n"
"border-radius:0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titlebar = QtWidgets.QFrame(self.frame)
        self.titlebar.setGeometry(QtCore.QRect(0, 0, 961, 31))
        self.titlebar.setMaximumSize(QtCore.QSize(1920, 1080))
        self.titlebar.setStyleSheet("background-color:rgb(36, 36, 56);")
        self.titlebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titlebar.setObjectName("titlebar")
        self.resizebtn = QtWidgets.QPushButton(self.titlebar)
        self.resizebtn.setGeometry(QtCore.QRect(910, 0, 21, 21))
        self.resizebtn.setMinimumSize(QtCore.QSize(21, 21))
        self.resizebtn.setMaximumSize(QtCore.QSize(21, 21))
        self.resizebtn.setStyleSheet("color: rgb(123, 158, 255);\n"
"background-color: rgb(123, 158, 255);\n"
"border-radius:10px;")
        self.resizebtn.setText("")
        self.resizebtn.setObjectName("resizebtn")
        self.closebtn = QtWidgets.QPushButton(self.titlebar)
        self.closebtn.setGeometry(QtCore.QRect(930, 0, 21, 21))
        self.closebtn.setMinimumSize(QtCore.QSize(21, 21))
        self.closebtn.setMaximumSize(QtCore.QSize(21, 21))
        self.closebtn.setStyleSheet("background-color: rgb(255, 98, 98);\n"
"color:  rgb(255, 98, 98);\n"
"border-radius:10px;")
        self.closebtn.setText("")
        self.closebtn.setObjectName("closebtn")
        self.label = QtWidgets.QLabel(self.titlebar)
        self.label.setGeometry(QtCore.QRect(10, 5, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb(176, 176, 186);\n"
"border-radius:8px;\n"
"")
        self.label.setObjectName("label")
        self.leftpanel = QtWidgets.QStackedWidget(self.frame)
        self.leftpanel.setGeometry(QtCore.QRect(10, 30, 231, 511))
        self.leftpanel.setObjectName("leftpanel")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.dialoguesmanager = QtWidgets.QFrame(self.page)
        self.dialoguesmanager.setEnabled(True)
        self.dialoguesmanager.setGeometry(QtCore.QRect(0, 0, 241, 501))
        self.dialoguesmanager.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dialoguesmanager.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dialoguesmanager.setObjectName("dialoguesmanager")
        self.searchline = QtWidgets.QLineEdit(self.dialoguesmanager)
        self.searchline.setGeometry(QtCore.QRect(80, 0, 151, 31))
        self.searchline.setStyleSheet("background-color: rgb(176, 176, 186);\n"
"border: none;\n"
"border-radius:0px;")
        self.searchline.setObjectName("searchline")
        self.profilebutton = QtWidgets.QPushButton(self.dialoguesmanager)
        self.profilebutton.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.profilebutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.profilebutton.setAutoFillBackground(False)
        self.profilebutton.setStyleSheet("background-color:rgb(192, 187, 255);\n"
"border-radius:35px;")
        self.profilebutton.setText("")
        self.profilebutton.setIconSize(QtCore.QSize(71, 71))
        self.profilebutton.setObjectName("profilebutton")
        self.dialoguebtn = QtWidgets.QPushButton(self.dialoguesmanager)
        self.dialoguebtn.setGeometry(QtCore.QRect(0, 80, 231, 421))
        self.dialoguebtn.setStyleSheet("background-color: rgb(186, 186, 196);\n"
"border: none;\n"
"border-radius:0px;")
        self.dialoguebtn.setObjectName("dialoguebtn")
        self.profilebutton.raise_()
        self.searchline.raise_()
        self.dialoguebtn.raise_()
        self.leftpanel.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.contextmenu = QtWidgets.QFrame(self.page_2)
        self.contextmenu.setEnabled(True)
        self.contextmenu.setGeometry(QtCore.QRect(0, 0, 241, 501))
        self.contextmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contextmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contextmenu.setObjectName("contextmenu")
        self.changeicon = QtWidgets.QPushButton(self.contextmenu)
        self.changeicon.setGeometry(QtCore.QRect(0, 0, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.changeicon.setFont(font)
        self.changeicon.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.changeicon.setObjectName("changeicon")
        self.changename = QtWidgets.QPushButton(self.contextmenu)
        self.changename.setGeometry(QtCore.QRect(0, 70, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.changename.setFont(font)
        self.changename.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.changename.setObjectName("changename")
        self.changepassword = QtWidgets.QPushButton(self.contextmenu)
        self.changepassword.setGeometry(QtCore.QRect(0, 140, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.changepassword.setFont(font)
        self.changepassword.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.changepassword.setObjectName("changepassword")
        self.changenumber = QtWidgets.QPushButton(self.contextmenu)
        self.changenumber.setGeometry(QtCore.QRect(0, 210, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        self.changenumber.setFont(font)
        self.changenumber.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.changenumber.setObjectName("changenumber")
        self.adddialogue = QtWidgets.QPushButton(self.contextmenu)
        self.adddialogue.setGeometry(QtCore.QRect(0, 280, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.adddialogue.setFont(font)
        self.adddialogue.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.adddialogue.setObjectName("adddialogue")
        self.addnewgroup = QtWidgets.QPushButton(self.contextmenu)
        self.addnewgroup.setGeometry(QtCore.QRect(0, 350, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addnewgroup.setFont(font)
        self.addnewgroup.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.addnewgroup.setObjectName("addnewgroup")
        self.backbtn = QtWidgets.QPushButton(self.contextmenu)
        self.backbtn.setGeometry(QtCore.QRect(0, 420, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.backbtn.setFont(font)
        self.backbtn.setStyleSheet("background-color:rgb(176, 176, 186);")
        self.backbtn.setObjectName("backbtn")
        self.leftpanel.addWidget(self.page_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(250, 30, 701, 501))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 701, 501))
        font = QtGui.QFont()
        font.setFamily("Gisha")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(176, 176, 186), stop:1  rgb(206, 206, 216));\n"
"border-radius:0px;")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stringfield = QtWidgets.QTextEdit(self.page_4)
        self.stringfield.setGeometry(QtCore.QRect(0, 470, 661, 31))
        self.stringfield.setStyleSheet("background-color: rgb(236, 236, 246);\n"
"border: none;\n"
"border-radius:0px;")
        self.stringfield.setObjectName("stringfield")
        self.sendbtn = QtWidgets.QPushButton(self.page_4)
        self.sendbtn.setGeometry(QtCore.QRect(654, 468, 51, 41))
        self.sendbtn.setStyleSheet("background-color: rgb(106, 106, 126);\n"
"border: none;\n"
"border-radius:0px;")
        self.sendbtn.setObjectName("sendbtn")
        self.textbrowser = QtWidgets.QLabel(self.page_4)
        self.textbrowser.setGeometry(QtCore.QRect(0, 0, 711, 471))
        self.textbrowser.setStyleSheet("background-color: rgb(186, 186, 196);\n"
"border: none;\n"
"border-radius:0px;")
        self.textbrowser.setText("")
        self.textbrowser.setObjectName("textbrowser")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.leftpanel.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.resizebtn.setToolTip(_translate("MainWindow", "Restore"))
        self.closebtn.setToolTip(_translate("MainWindow", "Close"))
        self.label.setText(_translate("MainWindow", " tild~"))
        self.dialoguebtn.setText(_translate("MainWindow", "Для начала общения \n"
"введите в поисковую строку\n"
"номер собеседника."))
        self.changeicon.setText(_translate("MainWindow", "Change icon"))
        self.changename.setText(_translate("MainWindow", "Change name"))
        self.changepassword.setText(_translate("MainWindow", "Change password"))
        self.changenumber.setText(_translate("MainWindow", "Change phone number"))
        self.adddialogue.setText(_translate("MainWindow", "Add friend-dialogue"))
        self.addnewgroup.setText(_translate("MainWindow", "New group"))
        self.backbtn.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", " Select a dialog and start a conversation"))
        self.stringfield.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendbtn.setText(_translate("MainWindow", ">"))
