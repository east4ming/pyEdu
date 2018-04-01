import socket
import time


host = ''  # 代表本机的所有ip地址
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 绑定地址到套结字
s.listen(2)
cli_sock, cli_addr = s.accept()
data = str(cli_sock.recv(1024), encoding='utf8')
data = '[{}] {}'.format(time.strftime('%H:%M:%S'), data)
cli_sock.sendall(bytes(data, encoding='utf8'))
print(data)
cli_sock.close()
s.close()
