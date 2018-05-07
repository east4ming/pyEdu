#!/usr/bin/env python
# -*- coding:utf-8 -*-


def check_score(score):
    if score > 90:
        return '优秀'
    elif score > 80:
        return '良好'
    elif score > 60:
        return '及格'
    else:
        return '不及格'


if __name__ == '__main__':
    my_score = 99
    print(check_score(my_score))
