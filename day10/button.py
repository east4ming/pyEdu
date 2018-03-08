"""窗口程序

1. 3个按钮
2. 两个按钮前景色为白色， 背景色为蓝色
3. 第三个按钮前景色为红色， 背景色为红色
4. 按下第三个按钮， 程序退出
"""


def button(style, forecolor='white', bgcolor='blue'):
    """打印输出对应的按钮"""
    forecolors = {'white': 37, 'red': 31}
    bgcolors = {'blue': 44, 'red': 41}
    print('\033[{};{}m {}\033[0m'.format(forecolors[forecolor],
                                         bgcolors[bgcolor], style))


if __name__ == '__main__':
    button('-')
    button('+')
    button('X', 'red', 'red')
    while 1:
        if input("请选择要按的按钮：（1/2/3）") == '3':
            break
