#!/usr/bin/env python

import threading
from time import ctime, sleep


loops = [4, 2]


class ThreadFunc():
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.res = self.func(*self.args)


def loop(nloop, nsec):
    print('start loop {} at: {}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at: {}'.format(nloop, ctime()))


def main():
    print('starting at: ', ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]),
                             loop.__name__))
        threads.append(t)
    for i in nloops:  # 启动线程
        threads[i].start()
    # 不用再管理一堆锁, 只要简单地对每个线程调用join()函数就可以了
    for i in nloops:  # 等待所有
        threads[i].join()  # threads to finish
    print('all DONE at: ', ctime())


if __name__ == '__main__':
    main()
