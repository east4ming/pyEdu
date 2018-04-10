#!/usr/bin/env python

import _thread
from time import ctime, sleep


def loop0():
    print('start loop 0 at: ', ctime())
    sleep(4)
    print('loop 0 done at: ', ctime())


def loop1():
    print('start loop 1 at: ', ctime())
    sleep(2)
    print('loop 1 done at: ', ctime())


def main():
    print('starting at: ', ctime())
    # start_new_thread 一定要有2个参数, 所以, 就算没有参数, 也要传递一个空元组
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # 为什么要加这一句?
    # 因为如果没有让主线程停下来, 主线程就会运行下一条语句, 显示"all DONE", 然后直接关闭两个子线程, 并退出.
    sleep(6)
    print('all DONE at: ', ctime())


if __name__ == '__main__':
    main()
