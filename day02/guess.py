"""Guess num.

随机生成一个数, 输入你猜的数字.
如果大, 提示大了.
如果小, 提示小了.
如果相等, 结束游戏.
"""

import random


def guess_num(randnum):
    """Guess num func.
    
    3次能才对就算赢.
    """
    guess_flag = False
    count = 3
    while (not guess_flag) and count != 0:
        num = int(input('Please input the num you guess: '))
        count -= 1
        if num > randnum:
            print('大了')
        elif num < randnum:
            print('小了')
        else:
            print('You win!')
            guess_flag = True
    else:
        print('You lose!')

randnum = random.randint(1, 10)
print(randnum)
guess_num(randnum)
