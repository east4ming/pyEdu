class ProtectAndHideX():
    def __init__(self, x):
        assert isinstance(x, int), '"x" must be an int!'
        self.__x = ~x

    def get_x(self):
        return ~self.__x

    def set_x(self, x):
        assert isinstance(x, int), '"x" must be an int!'
        self.__x = ~x

    x = property(get_x, set_x)


if __name__ == '__main__':
    # inst = ProtectAndHideX('foo')
    inst = ProtectAndHideX(10)
    print('inst.x = ', inst.x)
    inst.x = 20
    print(inst.x)
