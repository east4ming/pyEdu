#!/usr/bin/env python

from random import choice


class RandSeq():
    def __init__(self, seq):
        self.data = seq

    # 仅返回self, 这就是如何将一个对象声明为迭代器的方式
    def __iter__(self):
        return self

    # 迭代器没有终点
    def __next__(self):
        return choice(self.data)

    next = __next__


if __name__ == '__main__':
    seq = RandSeq(range(5))
    print(seq.next())
    print(seq.next())
    for i in seq:
        print(i)
