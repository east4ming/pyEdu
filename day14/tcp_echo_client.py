import socket


class TCPEchoClient():
    """基于TCP协议的回声客户端."""
    def __init__(self, srv_host='127.0.0.1', srv_port=12345):
        """Client初始化.

        1. 创建socket
        2. 连接socket到服务器地址+端口号
        """
        self.srv_addr = (srv_host, srv_port)
        self.cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cli_sock.connect(self.srv_addr)

    def mainloop(self):
        """主循环.

        1. 发送信息
        2. 接受信息
        3. 关闭socket连接

        异常处理:
        - 断言非空, 为空抛出异常
        - 捕获3类异常(EOFError: UNIX上为Ctrl+d,Windows上为Ctrl+Z+Enter), 跳出循环
        - 关闭socket连接.
        """
        while True:
            try:
                data = input('> ')
                assert data
            except (EOFError, KeyboardInterrupt, AssertionError) as e:
                print('用户输入异常或为空, 退出...', e, sep='\n\t')
                break
            else:
                self.cli_sock.sendall(bytes(data, encoding='utf8'))
            srv_msg = self.cli_sock.recv(16)
            print(srv_msg)
        self.cli_sock.close()


if __name__ == '__main__':
    client = TCPEchoClient()
    client.mainloop()
