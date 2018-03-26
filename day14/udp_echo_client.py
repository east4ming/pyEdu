import socket


class UDPEchoClient():
    """UDP 回声客户端."""
    def __init__(self, srv_host='localhost', srv_port=12345):
        self.srv_addr = (srv_host, srv_port)
        self.cli_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def mainloop(self):
        try:
            while True:
                try:
                    data = input('> ')
                    assert data
                except (EOFError, KeyboardInterrupt, AssertionError):
                    print('用户输入异常或为空, 退出...')
                    break
                else:
                    self.cli_sock.sendto(bytes(data, encoding='utf8'), self.srv_addr)
                    srv_msg, _ = self.cli_sock.recvfrom(1024)
                    print(srv_msg)
        finally:
            self.cli_sock.close()


if __name__ == '__main__':
    client = UDPEchoClient()
    client.mainloop()


