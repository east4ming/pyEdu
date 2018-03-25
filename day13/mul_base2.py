class A():
    def foo(self):
        print('A-foo')

    def bar(self):
        print('A-bar')


class B1(A):
    def foo(self):
        print('B1-foo')


class B2(A):
    def bar(self):
        print('B2-bar')


class C(B1, B2):
    pass


if __name__ == '__main__':
    c = C()
    c.foo()
    c.bar()
