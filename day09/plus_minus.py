"""简单的加减法数学游戏.

1. 随机生成两个100以内的数字
2. 随机选择加法或剑法
3. 总是使用大的数字减去小的数字
4. 如果用户打错三次， 程序给出正确答案
"""
from random import randint
from random import choice


def gen_two_nums():
    """随机生成两个100以内的数字"""
    num1, num2 = randint(1, 100), randint(1, 100)
    return num1, num2


def caculate(num1, num2):
    """"""
    operator = choice(('+', '-'))
    if operator == '-':
        if num1 > num2:
            result = num1 - num2
        else:
            result = num2 - num1
    else:
        result = num1 + num2
    return result


def ui():
    num1, num2 = gen_two_nums()
    prompt = """生成的两个数字是： {} {}.
游戏会对这两个数字随机做加法或减法（大-小）
请输入你计算的结果：（数字）""".format(num1, num2)
    result = caculate(num1, num2)
    n = 3
    while n:
        guess_num = int(input(prompt))
        n -= 1
        if guess_num == result:
            print("You win!")
            break
        else:
            print("你猜错了， 请重试")
    else:
        print("You lose!")
        print("结果是", result)


if __name__ == '__main__':
    ui()
