from socket import *
import sys
import sqlite3
import sys



class socketprocessor:
    def __init__(self):
        PORT_NUMBER = 5000
        SIZE = 1024

        hostName = gethostbyname('192.168.0.4')
        self.con = sqlite3.connect("tilddatabase.db")
        self.cur = self.con.cursor()
        print(hostName)

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind((hostName, PORT_NUMBER))

    def setavatar(self, picture):
        result = self.cur.execute("""SELECT *
                                FROM groupstable""").fetchall()

    def getlogin(self):
        result = self.cur.execute("""SELECT *
                                FROM userstable""").fetchall()

    def getnumber(self, number):
        return self.cur.execute(f"""SELECT *
                                        FROM userstable WHERE number = \"{number}\"""").fetchall()
    def getpassword(self, password):
        return self.cur.execute(f"""SELECT *
                                        FROM userstable WHERE password = \"{password}\"""").fetchall()
    def getprofile(self, login, password, number):
        return self.cur.execute(f"""SELECT *
                                                FROM userstable WHERE password = \"{password}\" and login = \"{login}\" and number = \"{number}\"""").fetchall()
    def setlogin(self, login):
        return self.cur.execute(f"""SELECT *
                                FROM groupstable WHERE login = \"{login}\"""").fetchall()
    def setpassword(self):
        result = self.cur.execute("""SELECT *
                                FROM groupstable""").fetchall()
    def setnumber(self):
        result = self.cur.execute("""SELECT *
                                FROM groupstable""").fetchall()


