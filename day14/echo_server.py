import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('', 10000)
print("starting up {} on {}".format(*addr))
s.bind(addr)
s.listen(1)
while True:
    print('Waiting for a connection.')
    conn, cli_addr = s.accept()
    try:
        print('Connection from {}'.format(cli_addr))
        while True:
            data = conn.recv(1024)
            print('Received data: {!r}'.format(data))
            if data:
                print('Sending data back to client.')
                conn.sendall(data)
            else:
                print('No data from {}'.format(cli_addr))
                break
    finally:
        s.close()
