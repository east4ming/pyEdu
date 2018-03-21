class RoundFloat():
    """输入必须是float, 输出为2位圆整."""
    def __init__(self, value):
        assert isinstance(value, float), "Value must be a float!"
        self.value = round(value, 2)

    def __str__(self):
        # return str(self.value)
        return '%.2f' % self.value

    __repr__ = __str__


if __name__ == '__main__':
    # rfm = RoundFloat(42)
    rfm = RoundFloat(4.23974298)
    print(rfm)