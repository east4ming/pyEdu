#!/usr/bin/env python

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    """应用程序核心引擎 - 随机选择一个操作并生成2个操作数

    避免负数
    """
    op = choice('+-')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    prompt = '{} {} {}='.format(nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(input(prompt)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print('answer\n{} {}'.format(prompt, ans))
            else:
                print('incorrect... try again')
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print('invalid input... try again')


def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()
