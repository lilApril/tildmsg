from socket import *
import sqlite3
import sys


class manager:
    def __init__(self):
        self.con = sqlite3.connect("tilddatabase.db")
        self.cur = self.con.cursor()


    def registration(self, login, password, number):
        self.cur.execute(f"INSERT INTO userstable(login, dialogues, groups, avatar, password, number) VALUES({login}, {None}, {None}, {None}, {password}, {number})")
        self.con.commit()


    def setavatar(self, picture, id):
        self.cur.execute(
            f"""UPDATE userstable
            SET avatar = {picture}
            WHERE id = {id}""")
        self.con.commit()

    def getavatar(self, id):
        server.send(bytes('|'.join(self.cur.execute(f"""SELECT avatar
                                FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getlogin(self, id):
        server.send(bytes('|'.join(self.cur.execute(f"""SELECT login
                                        FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getnumber(self, id):
        server.send(bytes('|'.join(self.cur.execute(f"""SELECT number
                                        FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))
    def getpassword(self, id):
        server.send(bytes('|'.join(self.cur.execute(f"""SELECT password
                                        FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))
    def getprofile(self, login, password, number):
        server.send(bytes('|'.join(self.cur.execute(f"""SELECT *
                                                FROM userstable WHERE password = \"{password}\" and login = \"{login}\" and number = \"{number}\"""").fetchall()), 'utf-8'))
    def setlogin(self, login, id):
        self.cur.execute(
            f"""UPDATE userstable
                    SET login = {login}
                    WHERE id = {id}""")
        self.con.commit()
    def setpassword(self, password, id):
        self.cur.execute(
            f"""UPDATE userstable
                    SET password = {password}
                    WHERE id = {id}""")
        self.con.commit()

    def setnumber(self, number, id):
        self.cur.execute(
            f"""UPDATE userstable
                            SET number = {number}
                            WHERE id = {id}""")
        self.con.commit()


ex = manager()
while True:
    server = socket(AF_INET, SOCK_STREAM)
    hostName = gethostbyname('192.168.86.85')
    server.bind((hostName, 5666))
    server.listen()
    client, address = server.accept()
    while True:
        data = client.recv(128)
        data = data.decode("utf-8")
        if len(data.split('|')) > 2:
            command, context = data.split('|')[0], data.split('|')[1:]
            if command == '':
                pass

        else:
            command = data
            print(command)

