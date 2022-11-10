from socket import *
import sqlite3
import sys
import multiprocessing


class manager:
    def __init__(self, client):
        self.con = sqlite3.connect("tilddatabase.db")
        self.cur = self.con.cursor()
        self.client = client

    def registration(self, login, password, number):
        self.cur.execute(
            f"""INSERT INTO userstable(login, groups, password, number) VALUES(\"{login}\", \"{'empty'}\", \"{password}\", \"{number}\")""")
        self.con.commit()

    def addgroup(self, id, name):
        self.cur.execute(
            f"""INSERT INTO chatstable(id, chats) VALUES(\"{name}\", '||')""")
        self.con.commit()
        tup = self.cur.execute(f"""SELECT groups
                                                                            FROM userstable WHERE id = \"{id}\"""").fetchall()[
                  0][0] + '|' + name
        self.cur.execute(
            f"""UPDATE userstable SET groups = \"{tup}\" WHERE id = {id}""")
        self.con.commit()

    def getgroups(self, id):
        tup = list(filter(lambda y: not any(map(str.isdigit, y)), list(map(lambda x: x[0], self.cur.execute(f"""SELECT id
                                                                            FROM chatstable""").fetchall()))))
        print(tup)
        tup = list(filter(lambda x: x in self.cur.execute(f"""SELECT groups
                                                                            FROM userstable WHERE id = {id}""").fetchall()[0][0].split('|'), tup))
        print(tup)
        if len(tup) > 0:
            self.client.send(bytes('|'.join(tup), 'utf-8'))
        else:
            self.client.send(b'empty')

    def getchatname(self, id, id1):
        if id1.isnumeric():
            tup = (str(id) + "|" + str(id1), str(id1) + "|" + str(id))
            if len(self.cur.execute(f"""SELECT id
                                                                FROM chatstable WHERE id in {tup}""").fetchall()) > 0:
                self.client.send(bytes(self.cur.execute(f"""SELECT id
                                                                    FROM chatstable WHERE id in {tup}""").fetchall()[0][
                                      0], 'utf-8'))
            else:
                self.cur.execute(f"""INSERT INTO chatstable VALUES(\"{str(id) + '|' + str(id1)}\", \"||\")""")
                self.con.commit()
                self.client.send(bytes(f'{str(id)}' + '|' + f'{str(id1)}', 'utf-8'))
        else:
            ispart = True if id1 in self.cur.execute(f"""SELECT groups
                                                                    FROM userstable WHERE id = {id}""").fetchall()[0][0].split('|') else False
            if ispart:
                self.client.send(bytes(id1, 'utf-8'))
            else:
                tup = self.cur.execute(f"""SELECT groups
                                                                    FROM userstable WHERE id = {id}""").fetchall()[0][0] + '|' + id1
                self.cur.execute(
                    f"""UPDATE userstable SET groups = \"{tup}\" WHERE id = {id}""")
                self.con.commit()
                self.client.send(bytes(id1, 'utf-8'))

    def sendmessage(self, id, chatname, message):
        if not chatname.isalnum():
            processedmsg = self.cur.execute(f"""SELECT chats
                                                        FROM chatstable WHERE id = \"{chatname}\"""").fetchall()[0][
                               0] + self.getlogin(id) + ':' + '|' + message + '||'
            self.cur.execute(
                f"""UPDATE chatstable SET chats = \"{processedmsg}\" WHERE id = \"{chatname}\"""")
            self.con.commit()

        else:
            tup = (str(id) + "|" + str(chatname), str(chatname) + "|" + str(id))
            processedmsg = self.cur.execute(f"""SELECT chats
                                                                    FROM chatstable WHERE id in {tup}""").fetchall()[
                               0][0] + self.getlogin(id) + ':' + '|' + message + '||'
            self.cur.execute(
                f"""UPDATE chatstable SET chats = \"{processedmsg}\" WHERE id in {tup}""")
            self.con.commit()

    def gettext(self, id, id1='grouptype'):
        if any(map(str.isdigit, id1)):
            tup = (str(id) + "|" + str(id1), str(id1) + "|" + str(id))
            print(tup)
            messages = self.cur.execute(f"""SELECT chats
                                                    FROM chatstable WHERE id in {tup}""").fetchall()
            if len(messages) == 0:
                self.client.send(b'empty')
            else:
                self.client.send(bytes(''.join(list(messages[0])).replace('|', '\n'), 'utf-8'))
        else:
            if len(self.cur.execute(f"""SELECT groups
                                                                FROM userstable WHERE id = \"{id}\"""").fetchall()[0]) == 0:
                self.client.send(b'empty')

            elif id1 in self.cur.execute(f"""SELECT groups
                                                                FROM userstable WHERE id = \"{id}\"""").fetchall()[0][0].split('|'):
                print(id1)
                messages = self.cur.execute(f"""SELECT chats
                                                                    FROM chatstable WHERE id = \"{id1}\"""").fetchall()[
                    0]
                if len(messages) == 0:
                    self.client.send(b'empty')
                else:
                    self.client.send(bytes(''.join(list(messages)).replace('|', '\n'), 'utf-8'))
            else:
                self.client.send(b'empty')

    def idfromnumber(self, number):
        if number.isalnum():
            content = bytes(str(self.cur.execute(f"""SELECT id
                                                    FROM userstable WHERE number = {number}""").fetchall()[0][0]),
                            'utf-8')
            if content:
                self.client.send(content)
            else:
                self.client.send(b'empty')
        else:

            self.client.send(bytes(number, 'utf-8'))

    def getids(self, id):
        tup = self.cur.execute(f"""SELECT id
                                        FROM chatstable""").fetchall()
        tup = list(map(lambda j: j[0] if j[0].isalpha() else j[0] if j[1] == id else j[1],
                       list(filter(lambda y: str(id) in y, list(map(lambda x: x[0].split('|'), tup))))))
        if len(tup) > 0 and len(tup[0]) > 0:
            self.client.send(bytes('|'.join(tup), 'utf-8'))
        else:
            self.client.send(bytes('empty', 'utf-8'))

    def getavatar(self, id):
        self.client.send(bytes('|'.join(self.cur.execute(f"""SELECT avatar
                                FROM userstable WHERE id = {id}""").fetchall()), 'utf-8'))

    def getlogin(self, id):
        return str(self.cur.execute(f"""SELECT login
                                        FROM userstable WHERE id = {id}""").fetchall()[0][0])

    def getloginfromid(self, id):
        try:
            self.client.send(bytes(str(self.cur.execute(f"""SELECT login
                                            FROM userstable WHERE id = {id}""").fetchall()[0][0]), 'utf-8'))
        except:
            self.client.send(b'empty')

    def getnumber(self, id):
        self.client.send(bytes('|'.join(self.cur.execute(f"""SELECT number
                                        FROM userstable WHERE id = {id}""").fetchall())[0][0], 'utf-8'))

    def getpassword(self, id):
        self.client.send(bytes('|'.join(self.cur.execute(f"""SELECT password
                                        FROM userstable WHERE id = {id}""").fetchall())[0][0], 'utf-8'))

    def getprofile(self, login, password, number):
        buff = bytes(str(self.cur.execute(f"""SELECT id
                                                FROM userstable WHERE password = \"{password}\" and login = \"{login}\" and number = \"{number}\"""").fetchall()[
                             0]),
                     'utf-8')
        self.client.send(buff if len(buff.decode('utf-8')) > 0 else bytes('|', 'utf-8'))

    def setlogin(self, login, id):
        self.cur.execute(
            f"""UPDATE userstable
                    SET login = \"{login}\"
                    WHERE id = {id}""")
        self.con.commit()

    def setpassword(self, password, id):
        self.cur.execute(
            f"""UPDATE userstable
                    SET password = \"{password}\"
                    WHERE id = {id}""")
        self.con.commit()

    def setnumber(self, number, id):
        self.cur.execute(
            f"""UPDATE userstable
                            SET number = \"{number}\"
                            WHERE id = {id}""")
        self.con.commit()


def activeserver(client, address, server):
        ex = manager(client)
        while True:
            while True:
                try:
                    data = client.recv(1024)
                    print(address)
                    print(data)
                    if len(data.decode("utf-8")) > 0:
                        data = data.decode("utf-8")
                        if len(data.split('|')) != 0:
                            command, context = data.split('|')[0], data.split('|')[1:]
                            print(command, '\n', context)
                            if command == 'gettext':
                                if len(context) == 2:
                                    ex.gettext(context[0], context[1])
                                elif len(context) == 1:
                                    ex.gettext(context[0])
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
                            if command == 'sendmessage':
                                ex.sendmessage(context[0], context[1], context[2])
                            if command == 'getchatname':
                                ex.getchatname(context[0], context[1])
                            if command == 'getloginfromid':
                                ex.getloginfromid(context[0])
                            if command == 'getids':
                                ex.getids(context[0])
                            if command == 'getgroups':
                                ex.getgroups(context[0])
                            if command == 'addgroup':
                                ex.addgroup(context[0], context[1])

                    else:
                        client, address = server.accept()
                except:
                    break
            print('exit moment')

if __name__ == "__main__":
    hostName = gethostbyname_ex(gethostname())[-1][-1]
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((hostName, 5666))
        print(hostName)
        server.listen(1)
        while True:
            client, addr = server.accept()
            p = multiprocessing.Process(target=activeserver, args=(client, addr, server))
            p.start()


