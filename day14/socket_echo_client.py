import socket

srv_host = 'localhost'
srv_port = 10000
srv_addr = (srv_host, srv_port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Connecting to {}:{}'.format(srv_host, srv_port))
client.connect(srv_addr)
try:
    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    client.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    client.close()
