"""猜拳游戏.

人出一个, 机器随机出一个.
判断胜负.
"""

import random

RPS = ('rock', 'paper', 'scissors')

prompt = """
(0) - 石头
(1) - 布
(2) - 剪刀
请输入(0/1/2):"""




win_list  = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))

def get_rps_results(player, computer):
    """根据剪刀石头布规则自动得出结果."""
    if player == computer :
        # 显示绿色
        print('\033[32;1m一局平局,pass\033[0m')
        return 0
    elif (player, computer) in win_list:
        # 显示红色
        print('\033[31;1m一局You win!!!\033[0m')
        return 1
    else:
        print('\033[31;1m一局You lose!!!\033[0m')
        return -1

counter = 0
result = 0
while True:
    computer = random.choice(RPS)
    ind = int(input(prompt))
    player = RPS[ind]
    print('You:', player, '\nComputer: ', computer)
    i = get_rps_results(player, computer)

    if i != 0:
        counter += 1
        result += i
    if counter == 3:
        if result > 0:
            print('\033[31;1mFinally: You win!!!\033[0m')
        elif result < 0:
            print('\033[31;1mFinally: You lose!!!\033[0m')
        break
