import json
import socket

import sctp

sock = sctp.sctpsocket(socket.AF_INET, sctp.TCP_STYLE, None)
sock.connect(('127.0.0.1', 9999))
for i in range(5):
    sock.sctp_send(json.dumps({'type': 'send', 'user': 'aaa', 'msg': i}))
