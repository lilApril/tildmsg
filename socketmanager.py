from socket import *
import sqlite3
import sys


class socketprocessor:
    def __init__(self, profile):
        hostName = gethostbyname('192.168.86.85')
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((hostName, 5666))
        self.profile = profile

    def registration(self, login, password, number):
        self.client.send(bytes(f"registration|{login}|{password}|{number}", "utf-8"))

    def setavatar(self, picture):
        self.client.send(bytes(f"setavatar|{picture}", "utf-8"))

    def getlogin(self, login):
        self.client.send(bytes(f"getlogin|{login}", "utf-8"))
        return self.client.recv(256)

    def getnumber(self, number):
        self.client.send(bytes(f"getnumber|{number}", "utf-8"))
        return self.client.recv(256)

    def getpassword(self, password):
        self.client.send(bytes(f"getpassword|{password}", "utf-8"))
        return self.client.recv(256)

    def getprofile(self, login, password, number):
        self.client.send(bytes(f"getprofile|{login}|{password}|{number}", "utf-8"))
        return self.client.recv(256)

    def setlogin(self, login):
        self.client.send(bytes(f"setlogin|{login}", "utf-8"))

    def setpassword(self, password):
        self.client.send(bytes(f"setpassword|{password}", "utf-8"))

    def setnumber(self, number):
        self.client.send(bytes(f"setnumber|{number}", "utf-8"))
