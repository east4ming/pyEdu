import socket

host = '127.0.0.1'
port = 12345
c = socket.socket()
c.connect((host, port))
c.sendall(b'I C U')
print(str(c.recv(1024), encoding='utf8'))
c.close()
