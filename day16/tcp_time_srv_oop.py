import socket
import time
import os


class TCPTimeServer():
    def __init__(self, host, port):
        self.addr = (host, port)
        self.srv = socket.socket()
        self.srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
            try:
                while True:
                    result = os.waitpid(-1, os.WNOHANG)
                    print('Reaped child process {}'.format(result[0]))
                    if result[0] == 0:
                        break
            except OSError:
                pass
            finally:
                conn, cli_addr = self.srv.accept()
            if os.fork():
                conn.close()
            else:
                self.srv.close()
                self.handle_child(conn)
            self.srv.close()


if __name__ == '__main__':
    srv = TCPTimeServer('', 10000)
    srv.mainloop()
