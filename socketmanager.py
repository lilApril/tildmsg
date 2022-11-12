from socket import *
import sqlite3
import sys

'''Функции в socketprocessor выполняют ровно то, что написано в их названии.
-------------------------------------
Первое слово либо get либо set
get - информация отправляется, потом принимается
set - информация отправляется на сервер, на нём и обрабатывается, ничего не принимается
исключения:
addgroup - создание группы
ext - прервать соединение с сервером
registration - создание нового аккаунта с объявленными логином, паролем и номером
idfromnumber - получить персональный айди-номер из номера (телефона) профиля
--------------------------------------
второе слово - ключ, т.е. name|login|password|id|ids|text|profile|ipaddress соответственно то, что мы должны получить 
или отправить
--------------------------------------
возможнен и постфикс "fromid", который существует только
 из-за того, что я посчитал его употребление нужным.
  он означает то, что мы работаем с единственным аргументом - id, по которому нам
  надо получить один из ключей (см. второе слово)'''


class socketprocessor:
    def __init__(self, ip):
        print(ip)
        hostName = gethostbyname(ip.strip())
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((hostName, 5666))

    def getloginfromid(self, id):
        self.client.send(bytes(f"getloginfromid|{id}", "utf-8"))
        return self.client.recv(2048)

    def registration(self, login, password, number):
        self.client.send(bytes(f"registration|{login}|{password}|{number}", "utf-8"))

    def getchatname(self, id, id1):
        self.client.send(bytes(f"getchatname|{id}|{id1}", "utf-8"))
        return self.client.recv(2048)

    def sendmessage(self, id, chatname, message):
        self.client.send(bytes(f"sendmessage|{id}|{chatname}|{message}", "utf-8"))

    def idfromnumber(self, number):
        self.client.send(bytes(f"idfromnumber|{number}", "utf-8"))
        return self.client.recv(2048)

    def getids(self, id):
        id = str(id)
        self.client.send(bytes(f"getids|{id}", "utf-8"))
        return self.client.recv(2048)

    def ext(self):
        self.client.close()

    def getnumber(self, number):
        self.client.send(bytes(f"getnumber|{number}", "utf-8"))
        return self.client.recv(2048)

    def gettext(self, id, id1):
        self.client.send(bytes(f"gettext|{id}|{id1}", "utf-8"))
        return self.client.recv(1048576)

    def getpassword(self, id, password):
        self.client.send(bytes(f"getpassword|{id}|{password}", "utf-8"))
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

    def getgroups(self, id):
        self.client.send(bytes(f"getgroups|{id}", "utf-8"))
        return self.client.recv(2048)

    def addgroup(self, id, name):
        self.client.send(bytes(f"addgroup|{id}|{name}", "utf-8"))
