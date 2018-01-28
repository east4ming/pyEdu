# sys_getsizeof_object.py

import sys

class WithoutAttributes:
    pass

class WithAttributes:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return

without_attrs = WithoutAttributes()
print('WithoutAttributes:', sys.getsizeof(without_attrs))

with_arrts = WithAttributes()
print('WithAttributes:', sys.getsizeof(with_arrts))