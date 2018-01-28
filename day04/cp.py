"""cp /usr/bin/ls /tmp
"""

source = '/usr/bin/ls'
target = '/tmp/ls'
s_data = b''
with open(source, 'rb') as s:
    while True:
        data = s.read(4096)
        if data == b'':
            break
        s_data += data
with open(target, 'wb') as t:
    t.write(data)


