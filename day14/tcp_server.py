import socket

host = ''  # 代表本机的所有ip地址
port = 12345
addr = (host, port)
s = socket.socket()
# 默认情况下, 套结字被系统保留一分钟, 程序结束后, 1分钟内无法再次启动
# 设置地址重用, 程序结束后, 可以再立即运行
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 绑定地址到套结字
s.listen(2)  # 启动监听, 最多有2个客户端
# The return value is a pair (conn, address)
# where conn is a new socket object usable to send and receive data on the connection,
# and address is the address bound to the socket on the other end of the connection.
cli_sock, cli_addr = s.accept()  # 开始等待客户端连接
print('Client connected from:', cli_addr)
data = cli_sock.recv(1024)  # 一次最多从客户套结字接受1024字节
print([data])
cli_sock.close()
s.close()
# 使用telnet连接, 连接之后可以直接输入数据回车发送数据.
