#!/usr/bin/env python

import threading
from time import ctime, sleep


loops = (4, 2)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        # 先调用基类的构造器
        super().__init__()
        self.name = name
        self.func = func
        self.args = args

    # 和mt_sleep4.py相比, 之前的特殊函数__call__()在子类中, 名字要改为run()
    def run(self):
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
        t = MyThread(loop, (i, loops[i]),
                             loop.__name__)
        threads.append(t)
    for i in nloops:  # 启动线程
        threads[i].start()
    for i in nloops:  # 等待所有
        threads[i].join()  # threads to finish
    print('all DONE at: ', ctime())


if __name__ == '__main__':
    main()
