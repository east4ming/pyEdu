#!/usr/bin/env python


class NumStr():

    def __init__(self, num=0, string=''):
        # 双下划线, 信息隐藏时加强一个级别
        # 导入该模块时, 不能直接访问到这些元素
        self.__num = num
        self.__string = string

    def __str__(self):
        return '[{} :: {!r}]'.format(self.__num, self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self.__num + other.__num,
                                  self.__string + other.__string)
        else:
            raise TypeError('Illegal argument for built-in operation')

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.__num * num,
                                  self.__string * num)
        else:
            raise TypeError('Illegal argument for built-in operation')

    def __bool__(self):
        # 如果它的结果​​是非零的, 则该对象被认为是真的
        # 对于True的定义
        return bool(self.__num) or bool(len(self.__string))

    def __gt__(self, other):
        return self.__num > other.__num and self.__string > other.__string

    def __lt__(self, other):
        return self.__num < other.__num and self.__string < other.__string


if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(4, 'goo')
    print(b > a)
    print(a < b)