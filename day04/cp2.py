"""cp /usr/bin/ls /tmp
"""
import sys

source = sys.argv[1]
target = sys.argv[2]


def copy(source, target):
    s_data = b''
    with open(source, 'rb') as s:
        while True:
            data = s.read(4096)
            if data == b'':
                break
            s_data += data
    with open(target, 'wb') as t:
        t.write(s_data)


copy(source, target)
