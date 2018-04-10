#!/usr/bin/env python

from random import randint
from time import sleep
from queue import Queue
from day16.thread.my_thread import MyThread


# 把一个对象放入队列
# 字符串'xxx'就是对象
def write_q(queue):
    print('producting object for Q...')
    queue.put('xxx', 1)
    print('size now', queue.qsize())


# 消耗队列中的一个对象
def read_q(queue):
    val = queue.get(1)
    print('consumed object from Q... size now', queue.qsize())


# 一次往队列中放入一个对象, 等待一会儿(1-3s), 然后再做指定次数的同样的事情
def writer(queue, loops):
    for i in range(loops):
        write_q(queue)
        sleep(randint(1, 3))


# 一次从队列中读取一个对象, 等待一会儿(2-5s), 然后再做指定次数的同样的事情
def reader(queue, loops):
    for i in range(loops):
        read_q(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print('all DONE')


if __name__ == '__main__':
    main()
