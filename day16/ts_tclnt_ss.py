#!/usr/bin/env python

from socket import *

host = 'localhost'
port = 21567
bufsiz = 1024
addr = (host, port)


while True:
    tcp_cli_sock = socket()
    tcp_cli_sock.connect(addr)
    data = input('> ')
    if not data:
        break
    tcp_cli_sock.send(bytes('{}\r\n'.format(data), encoding='utf8'))
    data = tcp_cli_sock.recv(bufsiz)
    if not data:
        break
    print(data.strip())
    tcp_cli_sock.close()
