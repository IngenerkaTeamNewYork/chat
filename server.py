import pprint

import sctp
import socket
import json
import datetime
import select


class ChatHandle:
    def __init__(self):
        self.__sock = sctp.sctpsocket(socket.AF_INET, sctp.TCP_STYLE, None)
        self.__sock.setblocking(True)
        self.log = []

    def start(self):
        self.__sock.bind(('127.0.0.1', 9999))
        self.__sock.listen(2)
        conn, addr = self.__sock.accept()
        while True:
            if conn.sock() in select.select([conn.sock()], [], [])[0]:
                fromaddr, flags, msg, notif = conn.sctp_recv(1024)
                if len(msg) > 0:
                    self.__action(msg)
                else:
                    conn, addr = self.__sock.accept()
            pprint.pprint(self.log)

    def __action(self, data):
        info = json.loads(data)
        if info['type'] == 'send':
            self.log.append((info['user'], info['msg'], datetime.datetime.now().isoformat()))


chat = ChatHandle()

chat.start()
