from socket import *
import sqlite3
import sys


class socketprocessor:
    def __init__(self):
        hostName = gethostbyname('192.168.0.4')
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((hostName, 5666))

    def registration(self, login, password, number):
        self.client.send(bytes(f"registration|{login}|{password}|{number}", "utf-8"))
        print('ok2')

    def idfromnumber(self, number):
        self.client.send(bytes(f"idfromnumber|{number}", "utf-8"))
        return self.client.recv(2048)

    def setavatar(self, picture, id):
        #self.client.send(bytes(f"setavatar|{id}", "utf-8"))
        #file = open(picture, mode='rb')
        #datapic = file.read(2048)
        #while datapic:
             #self.client.send(datapic)
             #datapic = file.read(2048)
        #file.close()
        pass

    def getids(self, id):
        id = str(id)
        self.client.send(bytes(f"getids|{id}", "utf-8"))
        return self.client.recv(2048)

    def ext(self):
        self.client.close()

    def getlogin(self, login):
        self.client.send(bytes(f"getlogin|{login}", "utf-8"))
        return self.client.recv(2048)

    def getnumber(self, number):
        self.client.send(bytes(f"getnumber|{number}", "utf-8"))
        return self.client.recv(2048)
    def gettext(self, id, id1):
        print(id, id1)
        self.client.send(bytes(f"gettext|{id}|{id1}", "utf-8"))
        return self.client.recv(2048)

    def getpassword(self, password):
        self.client.send(bytes(f"getpassword|{password}", "utf-8"))
        return self.client.recv(2048)

    def getprofile(self, login, password, number):
        self.client.send(bytes(f"getprofile|{login}|{password}|{number}", "utf-8"))
        return self.client.recv(2048)

    def setlogin(self, login, id):
        self.client.send(bytes(f"setlogin|{login}|{id}", "utf-8"))

    def setpassword(self, password, id):
        self.client.send(bytes(f"setpassword|{password}|{id}", "utf-8"))

    def setnumber(self, number, id):
        self.client.send(bytes(f"setnumber|{number}|{id}", "utf-8"))

