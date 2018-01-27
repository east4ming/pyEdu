"""猜拳游戏.

人出一个, 机器随机出一个.
判断胜负.
"""

import random

RPS = ('rock', 'paper', 'scissors')
RPS_dict = {'a': 'rock', 'b': 'paper', 'c': 'scissors'}
computer = random.choice(RPS)
prompt = """
(a) - 石头
(b) - 布
(c) - 剪刀
请输入(a/b/c):"""

key = input(prompt)
player = RPS_dict[key]
print('You:', player, '\nComputer: ', computer)


win_list  = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))

def get_rps_results(player, computer):
    """根据剪刀石头布规则自动得出结果."""
    if player == computer :
        # 显示绿色
        print('\033[32;1m平局\033[0m')
    elif (player, computer) in win_list:
        # 显示红色
        print('\033[31;1mYou win!!!\033[0m')
    else:
        print('\033[31;1mYou lose!!!\033[0m')

get_rps_results(player, computer)
