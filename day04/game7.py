"""猜拳游戏.

人出一个, 机器随机出一个.
判断胜负.
3局2胜
"""

import random

RPS = ('rock', 'paper', 'scissors')

prompt = """
(0) - 石头
(1) - 布
(2) - 剪刀
请输入(0/1/2):"""
win_list  = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))
pwin = 0
cwin = 0
while pwin < 2 and cwin < 2:
    ai = random.choice(RPS)
    ind = int(input(prompt))
    player = RPS[ind]
    print('You:', player, '\nComputer: ', ai)
    if player == ai :
        # 显示绿色
        print('\033[32;1m一局平局,pass\033[0m')
    elif (player, ai) in win_list:
        # 显示红色
        print('\033[31;1m一局You win!!!\033[0m')
        pwin += 1
    else:
        print('\033[31;1m一局You lose!!!\033[0m')
        cwin += 1
    if pwin == 2:
        print('\033[31;1mFinally: You win!!!\033[0m')
    if cwin == 2:
        print('\033[31;1mFinally: You lose!!!\033[0m')