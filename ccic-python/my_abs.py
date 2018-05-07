"""我自己的求绝对值的函数"""


def my_abs(value):
    # if type(value) not in (int, float):
    if not isinstance(value, (int, float)):
        raise ValueError
    if value >= 0:
        return value
    else:
        return -value


if __name__ == '__main__':
    print(my_abs(-9))
    print(my_abs(0))
    print(my_abs(9))
    print(my_abs('a'))

