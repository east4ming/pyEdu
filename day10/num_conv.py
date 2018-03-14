#!/usr/bin/env python


def convert(func, seq):
    """conv. sequence of numbers to same type"""
    return [func(each_num) for each_num in seq]


myseq = (123, 45.67, -6.2e8, 99999999)
print(convert(int, myseq))
print(convert(float, myseq))
print(convert(str, myseq))
