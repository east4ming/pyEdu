#!/usr/bin/env python

from time import ctime, sleep
import functools


class TSFunc():
    def __init__(self, func):
        self.func = func
        print('[{}] {}() init'.format(ctime(), self.func.__name__))

    def __call__(self, *args, **kwargs):
        print('[{}] {}() called'.format(ctime(), self.func.__name__))
        return self.func


# def tsfunc(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('[{}] {}() called'.format(ctime(), func.__name__))
#         return func()
#     return wrapper


@TSFunc
def foo():
    pass


foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
