#!/usr/bin/env python

from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime


host = ''
port = 21567
addr = (host, port)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from: {}'.format(self.client_address))
        # self.wfile.write(bytes('[{}] {}'.format(ctime(), self.rfile.readline()),
        #                        encoding='utf8'))
        self.wfile.write(bytes('[{}]    '.format(ctime()), encoding='utf8') +
                               self.rfile.readline())


tcp_serv = TCP(addr, MyRequestHandler)
print('waiting for connection...')
tcp_serv.serve_forever()
