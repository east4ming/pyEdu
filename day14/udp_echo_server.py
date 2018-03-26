import socket


class UDPEchoServer():
    """UDP 回声服务器."""
    def __init__(self, host='localhost', port=12345):
        """初始化:

        - 创建socket
        - 绑定server地址端口
        """
        self.srv_addr = (host, port)
        self.srv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.srv_sock.bind(self.srv_addr)
        print('UDP Server Starting...')

    def mainloop(self):
        print('Waiting a connection')
        while True:
            try:
                msg, cli_addr = self.srv_sock.recvfrom(1024)
                print('Received msg: {!r} from {}.'.format(msg, cli_addr))
                assert msg
            except AssertionError:
                print('用户输入为空或异常, 忽略...')
                break
            else:
                print('Send {!r} to {}'.format(msg, cli_addr))
                self.srv_sock.sendto(msg, cli_addr)


if __name__ == '__main__':
    srv = UDPEchoServer()
    srv.mainloop()
