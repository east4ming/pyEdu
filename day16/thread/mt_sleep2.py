#!/usr/bin/env python

import _thread
from time import ctime, sleep


loops = [4, 2]


# 在sleep()的时间到了之后就释放相应的锁以**通知主线程**, 这个线程已经结束了.
def loop(nloop, nsec, lock):
    print('start loop {} at: {}'.format(nloop, ctime()))
    sleep(nsec)
    print('loop {} done at: {}'.format(nloop, ctime()))
    lock.release()


def main():
    print('starting at: ', ctime())
    locks = []
    nloops = range(len(loops))
    # 创建一个锁的列表
    # 并分别调用各个锁的acquire()函数获得锁, 获得锁表示"把锁锁上"
    # 锁上后, 把锁放到锁列表locks中.
    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    # 每个线程都会被分配一个事先已经获得的锁
    # 创建线程, 为什么不在创建锁的循环里创建线程?
    # 1. 想到实现线程的同步, 所以要让"所有的马同时冲出栅栏"
    # 2. 获取锁要花一些时间, 如果线程退出的"太快", 可能会导致还没有获得锁, 线程就已经结束的情况
    # 在线程结束时, 线程要自己做解锁操作
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 最后一个循环只是坐在那里一直等(达到暂停主线程的目的), 直到2个锁都被解锁为止才能继续运行.
    for i in nloops:
        while locks[i].locked(): pass

    print('all DONE at: ', ctime())


if __name__ == '__main__':
    main()
