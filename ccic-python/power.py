def power(x, i=2):
    if not i:
        s = 1
    elif i > 0:
        s = _p_power(x, i)
    elif i < 0:
        s = _p_power(x, abs(i))
        s = 1/s
    return s


def _p_power(x, i=2):
    s = 1
    while i > 0:
        s *= x
        i -= 1
    return s


if __name__ == '__main__':
    print(power(2))
    print(power(2, 3))
    print(power(2, 1))
    print(power(2, 0))
    print(pow(2, -2))
    print(power(2, -2))
