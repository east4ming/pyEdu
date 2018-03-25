class TimeDeco():
    def __init__(self, func):
        self.func = func
        print('{} inited'.format(self.func.__name__))

    def __call__(self, *args, **kwargs):
        print('{} called'.format(self.func.__name__))
        return self.func


@TimeDeco
def test():
    print('test')


if __name__ == '__main__':
    test()