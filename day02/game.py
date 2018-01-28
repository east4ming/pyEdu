"""猜拳游戏.

人出一个, 机器随机出一个.
判断胜负.
"""

import random

RPS = ('rock', 'paper', 'scissors')
computer = random.choice(RPS)
player = input("请出手: ('rock', 'paper', 'scissors')")
print('computer: ', computer)
# if player == 'rock':
#     if computer == 'rock':
#         print('平局')
#     elif computer == 'scissors':
#         print('You win.')
#     else:
#         print('You lose')
# elif player == 'scissors':
#     if computer == 'rock':
#         print('You lose')
#     elif computer == 'scissors':
#         print('平局')
#     else:
#         print('You win')
# else:
#     if computer == 'rock':
#         print('You win')
#     elif computer == 'scissors':
#         print('you lose')
#     else:
#         print('平局')

win_list  = (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock'))

def get_rps_results(player, computer):
    """根据剪刀石头布规则自动得出结果."""
    if player == computer :
        print('平局')
    elif (player, computer) in win_list:
        print('you win')
    else:
        print('you lose')

get_rps_results(player, computer)
