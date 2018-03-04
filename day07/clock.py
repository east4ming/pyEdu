import time
import sys

# for i in range(1, 6):
#     print('\r{}'.format(i), end='')
#     sys.stdout.flush()
#     time.sleep(1)


def clock():
    print('#' * 20, end='')
    n = 0
    while 1:
        print('\r{}@{}'.format('#' * n, '#' * (19-n)), end='')
        sys.stdout.flush()
        n += 1
        time.sleep(0.4)
        if n == 19:
            n = 0


if __name__ == '__main__':
    clock()
