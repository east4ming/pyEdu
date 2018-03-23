#!/usr/bin/env python

from time import time, ctime, sleep


class TimedWrapMe():
    def __init__(self, obj):
        self.__data = obj
        # 实例化, 3个时间都是实例化的时间
        # time()为float类型
        self.__ctime = self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise TypeError("argument of 'c', 'm', or 'a' required")
        # 返回该类的 __ctime 等属性
        return getattr(self, '_{}__{}time'.format(self.__class__.__name__,
                                                  t_type[0]))

    def gettimestr(self, t_type):
        # 括号内为time()返回的float, ctime()会将其转换为人类可读的时间字符串.
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return '{}'.format(self.__data)

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        # 返回被包装的对象的属性.
        return getattr(self.__data, attr)


if __name__ == '__main__':
    # 创建
    time_wrapped_obj = TimedWrapMe(932)
    print(time_wrapped_obj.gettimestr('c'))
    print(time_wrapped_obj.gettimestr('m'))
    print(time_wrapped_obj.gettimestr('a'))
    # 查看
    sleep(5)
    print(time_wrapped_obj)
    print(time_wrapped_obj.gettimestr('c'))
    print(time_wrapped_obj.gettimestr('m'))
    print(time_wrapped_obj.gettimestr('a'))
    # 修改
    sleep(5)
    time_wrapped_obj.set('time is up!')
    print(time_wrapped_obj.gettimestr('m'))
    # 查看
    sleep(5)
    print(time_wrapped_obj)
    print(time_wrapped_obj.gettimestr('c'))
    print(time_wrapped_obj.gettimestr('m'))
    print(time_wrapped_obj.gettimestr('a'))
