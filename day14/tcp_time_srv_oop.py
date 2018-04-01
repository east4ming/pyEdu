import socket
import time


class TCPTimeServer():
    def __init__(self, host, port):
        self.addr = (host, port)
        self.srv = socket.socket()
        self.srv.bind(self.addr)
        self.srv.listen(2)

    def handle_child(self, conn):
        while True:
            data = str(conn.recv(1024), encoding='utf8')
            if not data.strip():
                break
            data = '[{}] {}'.format(time.strftime('%H:%M:%S'), data)
            conn.sendall(bytes(data, encoding='utf8'))
        conn.close()

    def mainloop(self):
        while True:
            conn, cli_addr = self.srv.accept()
            self.handle_child(conn)
        self.srv.close()


if __name__ == '__main__':
    srv = TCPTimeServer('', 12345)
    srv.mainloop()
