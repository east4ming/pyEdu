class PositiveInt(int):
    """想要一个永远都是正数的整数类型, 通过继承int实现."""
    def __new__(cls, value):
        return super(PositiveInt, cls).__new__(cls, abs(value))


if __name__ == '__main__':
    a_pos_int = PositiveInt(-3)
    print(a_pos_int)