import socket

class TCPTimeClient():
    def __init__(self, host='127.0.0.1', port=12345):
        self.srv_addr = (host, port)
        self.cli = socket.socket()
        self.cli.connect(self.srv_addr)

    def chat(self):
        while True:
            data = input('>')
            data = bytes(data, encoding='utf8')
            self.cli.sendall(data)
            if not data:
                break
            print(str(self.cli.recv(1024), encoding='utf8'))
        self.cli.close()


if __name__ == '__main__':
    c = TCPTimeClient()
    c.chat()
