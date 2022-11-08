from socket import *
import sqlite3
import sys


class manager:
    def __init__(self):
        self.con = sqlite3.connect("tilddatabase.db")
        self.cur = self.con.cursor()

    def registration(self, login, password, number):
        self.cur.execute(
            f"INSERT INTO userstable(login, dialogues, groups, avatar, password, number) VALUES({login}, {None}, {None}, {None}, {password}, {number})")
        self.con.commit()

    def setavatar(self, id):
        #client, address = server.accept()
        #file = open(f'{id}.png', mode='wb')
        #datapic = client.recv(2048)
        #while datapic:
            #file.write(datapic)
            #datapic = client.recv(2048)
           # print(1)
        #file.close()
        pass

    def gettext(self, id, id1):
        tup = (str(id) + "|" + str(id1), str(id1) + "|" + str(id))
        print(tup)
        self.messages = self.cur.execute(f"""SELECT chats
                                                FROM chatstable WHERE id in {tup}""").fetchall()[0]
        print(self.messages)
        if len(self.messages) == 0:
            client.send(b'empty')
        else:
            if len(self.messages) > 1024:
                client.send(bytes(''.join(list(self.messages)[len(self.messages) - 1024:]).replace('|', '\n'), 'utf-8'))
            else:
                client.send(bytes(''.join(list(self.messages)).replace('|', '\n'), 'utf-8'))

    def idfromnumber(self, number):
        print(number)
        print(str(self.cur.execute(f"""SELECT id
                                                FROM userstable WHERE number = {number}""").fetchall()))
        client.send(bytes(str(self.cur.execute(f"""SELECT id
                                                FROM userstable WHERE number = {number}""").fetchall()[0]), 'utf-8'))

    def getids(self, id):
        print(self.cur.execute(f"""SELECT id
                                        FROM chatstable WHERE {id} in id""").fetchall())
        client.send(bytes(list(filter(lambda x: x != id, self.cur.execute(f"""SELECT id
                                        FROM chatstable WHERE {id} in id""").fetchall()[0].split('|')))[0], 'utf-8'))

    def getavatar(self, id):
        client.send(bytes('|'.join(self.cur.execute(f"""SELECT avatar
                                FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getlogin(self, id):
        client.send(bytes('|'.join(self.cur.execute(f"""SELECT login
                                        FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getnumber(self, id):
        client.send(bytes('|'.join(self.cur.execute(f"""SELECT number
                                        FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getpassword(self, id):
        client.send(bytes('|'.join(self.cur.execute(f"""SELECT password
                                        FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getprofile(self, login, password, number):
        buff = bytes(str(self.cur.execute(f"""SELECT id
                                                FROM userstable WHERE password = \"{password}\" and login = \"{login}\" and number = \"{number}\"""").fetchall()[0]),
                          'utf-8')
        client.send(buff if len(buff.decode('utf-8')) > 0 else bytes('|', 'utf-8'))

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
server = socket(AF_INET, SOCK_STREAM)
hostName = gethostbyname_ex(gethostname())[-1][-1]
print(hostName)
server.bind((hostName, 5666))
server.listen()

while True:
    client, address = server.accept()
    while True:
        try:
            data = client.recv(1024)
            data = data.decode("utf-8")
            if len(data.split('|')) != 0:
                command, context = data.split('|')[0], data.split('|')[1:]
                print(command, '\n', context)
                if command == 'gettext':
                    ex.gettext(context[0], context[1])
                if command == 'getprofile':
                    ex.getprofile(context[0], context[1], context[2])
                if command == 'registration':
                    ex.registration(context[0], context[1], context[2])
                if command == 'setavatar':
                    ex.setavatar(context[0])
                if command == 'setlogin':
                    ex.setlogin(context[0], context[1])
                if command == 'setpassword':
                    ex.setpassword(context[0], context[1])
                if command == 'setnumber':
                    ex.setnumber(context[0], context[1])
                if command == 'idfromnumber':
                    ex.idfromnumber(context[0])
        except:
            break
    print('exit moment')
