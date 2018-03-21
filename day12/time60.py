#!/usr/bin/env python


class Time60():
    """Time60 - track hours and minutes."""

    def __init__(self, hr, min):
        """Time60 constructor - takes hours and minutes."""
        self.hr = hr
        self.min = min

    def __str__(self):
        """Time60 - string representation."""
        return '{:02}:{:02}'.format(self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        """Time60 - overloading the addition operator."""
        # 加之后是另一个Time60 对象, 应当创建另一个对象并填入计算出来的总数
        # 调用类构造器返回一个新的对象
        # 新的对象通过调用类来创建, 在类中, 直接使用 self.__class__属性(就是Time60)
        # return Time60(self.hr+other.hr, self.min+other.min)
        return self.__class__(self.hr+other.hr, self.min+other.min)

    def __iadd__(self, other):
        """Time60 - overloading in-place addition."""
        self.hr += other.hr
        self.min += other.min
        return self


if __name__ == '__main__':
    a_time = Time60(5, 2)
    b_time = Time60(12, 30)
    c_time = a_time+b_time
    print(c_time)
    print(id(a_time))
    a_time += b_time
    print(id(a_time))
    print(a_time)
