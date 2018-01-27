"""Guess num.

规则:
- 随机生成一个数, 输入你猜的数字.
- 3次能猜对就算赢.
- 如果大, 提示大了.
- 如果小, 提示小了.
- 如果相等, 结束游戏, 提示"你赢了!!!".
- 如果3次都没猜对, 提示"你输了!!!"
"""

import random


def guess_num(randnum):
    """Guess num func.
    
    3次能才对就算赢.
    """

    count = 3
    while count != 0:
        num = int(input('Please input the num you guess (1-10): '))
        count -= 1
        if num > randnum:
            print('大了')
        elif num < randnum:
            print('小了')
        else:
            print('\033[31;1mYou win!!!\033[0m')
            break
    else:
        print('\033[31;1mYou lose!!!\033[0m')
        print('\033[32;1mThe rand num is:{}\033[0m'.format(randnum))

randnum = random.randint(1, 10)
guess_num(randnum)

