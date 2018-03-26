import socket


class TCPEchoServer():
    """基于TCP协议的回声服务器."""
    def __init__(self, host='', port=12345):
        """Server初始化.

        1. 创建socket
        2. 绑定socket到地址+端口号
        3. 监听
        """
        self.srv_addr = (host, port)
        self.srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srv_sock.bind(self.srv_addr)
        self.srv_sock.listen(1)

    def handle_msg(self, conn):
        """处理socket信息, 接受信息并发送同样信息.

        增加异常处理:
        断言接收的msg不为空;
        为空则抛出异常, 捕获异常并break跳出循环.
        跳出循环后关闭该conn
        """
        while True:
            try:
                msg = conn.recv(16)
                assert msg
            except AssertionError:
                print('用户输入为空或异常, 忽略...')
                break
            else:
                print(msg)
                conn.sendall(msg)

    def mainloop(self):
        """主循环. 正常情况下永不停止.

        1. accept
        2. 调用处理信息的方法
        3. 关闭socket连接
        """
        print('TCPEchoServer Running...')
        while True:
            conn, client_addr = self.srv_sock.accept()
            print('Connection from {}'.format(client_addr))
            self.handle_msg(conn)
            conn.close()


if __name__ == '__main__':
    srv = TCPEchoServer()
    srv.mainloop()
