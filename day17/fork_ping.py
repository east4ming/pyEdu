import subprocess
import os

import sys


def ping(ip):
    rc = subprocess.call('ping -c2 {} &>/dev/null'.format(ip), shell=True)
    if rc == 0:
        return '{}: up'.format(ip)
    else:
        return '{}: down'.format(ip)


if __name__ == '__main__':
    ips = ['192.168.83.{}'.format(i) for i in range(1, 255)]
    for ip in ips:
        pid = os.fork()
        if not pid:
            print(ping(ip), end='\t')
            sys.exit()
