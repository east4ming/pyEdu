#!/usr/bin/env python

import os
import pickle


class FileDescr():
    # 用来记录描述符访问的所有属性
    saved = []

    def __init__(self, name=None):
        self.name = name

    # 获取描述符的属性之前, 必须确保赋值后才能使用
    def __get__(self, instance, owner=None):
        if self.name not in FileDescr.saved:
            raise AttributeError("{!r} used before assignment".format(self.name))
        try:
            f = open(self.name, 'rb')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError, EOFError, AttributeError,
                ImportError, IndexError):
            raise AttributeError("could not read {0!r}: {0}".format(self.name))

    def __set__(self, instance, value):
        """打开pickle文件, 添加到saved列表"""
        f = open(self.name, 'wb')
        try:
            pickle.dump(value, f)
            FileDescr.saved.append(self.name)
        except (TypeError, pickle.PicklingError) as e:
            # print(e)
            raise AttributeError("could not pickle {!r}".format(self.name))
        finally:
            f.close()

    def __delete__(self, instance):
        """属性删除, 文件会被删除, saved中对应元素也会删除"""
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError):
            pass


if __name__ == '__main__':
    class MyFileVarClass():
        foo = FileDescr('foo')
        bar = FileDescr('bar')

    fvc = MyFileVarClass()
    # 抛出AttributeError
    # print(fvc.foo)

    fvc.foo = 42
    fvc.bar = 'leanna'
    print(fvc.foo, fvc.bar)
    # del fvc.foo
    # print(fvc.foo, fvc.bar)

    # AttributeError: could not pickle 'foo'
    fvc.foo = __builtins__
