class A():
    def foo(self):
        print('A method')


class B():
    def bar(self):
        print('B method')


class AB(A, B):
    pass


if __name__ == '__main__':
    ab = AB()
    ab.foo()
    ab.bar()
