#!/usr/bin/env python


class AnyIter():
    def __init__(self, data, safe=False):
        self.iter = iter(data)
        self.safe = safe

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter)

    def next(self, howmany=1):
        retval = []
        for item in range(howmany):
            try:
                retval.append(self.__next__())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval


if __name__ == '__main__':
    a = AnyIter(range(10))
    for i in range(1, 5):
        print(i, ':', a.next(i))
    # 不安全模式
    # b = AnyIter(range(10))
    # b.next(14)
    # 安全模式
    c = AnyIter(range(10), True)
    print(c.next(14))
