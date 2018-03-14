#!/usr/bin/env python

from time import ctime, sleep
import functools


def tsfunc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('[{}] {}() called'.format(ctime(), func.__name__))
        return func()
    return wrapper


@tsfunc
def foo():
    pass


foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
