import subprocess
import multiprocessing


def ping(ip):
    rc = subprocess.call('ping -c2 {} &>/dev/null'.format(ip), shell=True)
    if rc == 0:
        print('{}: up'.format(ip))
    else:
        print('{}: down'.format(ip))


if __name__ == '__main__':
    ips = ['192.168.83.{}'.format(i) for i in range(1, 255)]
    for ip in ips:
        p = multiprocessing.Process(target=ping, args=(ip,))
        p.start()
