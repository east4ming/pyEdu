class A():
    count = 0

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    a = A(1)
    print(a.__dict__)
    print(A.__dict__)
    adict = {'name': 'casey', 'age': 24, 'count': 1}
    a.__dict__.update(adict)
    print(a.__dict__)
    print(A.__dict__)