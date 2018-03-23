"""包装对象的简单例子."""


class WrapMe():
    def __init__(self, obj):
        self.__data = obj

    def get(self):
        return self.__data

    def __repr__(self):
        return '{}'.format(self.__data)

    def __str__(self):
        return str(self.__data)

    # 对属性及方法的访问, 都是通过getattr()方法
    def __getattr__(self, attr):
        return getattr(self.__data, attr)


if __name__ == '__main__':
    # 复数
    # wrapped_complex = WrapMe(3.5+4.2j)
    # print(wrapped_complex)
    # print(wrapped_complex.real)
    # print(wrapped_complex.imag)
    # print(wrapped_complex.conjugate())
    # print(wrapped_complex.get())
    # 列表
    wrapped_list = WrapMe([123, 'foo', 45.67])
    wrapped_list.append('bar')
    wrapped_list.append(123)
    print(wrapped_list)
    print(wrapped_list.index(45.67))
    print(wrapped_list.count(123))
    print(wrapped_list.pop())
    print(wrapped_list)
    # 切片操作不可以, 它是内建于类型中, 而不是像append()方法那样作为属性存在
    # print(wrapped_list[3])
    # "作弊"方法, 访问get(), 得到实际对象
    real_list = wrapped_list.get()
    print(real_list[3])
    # 文件
    f = WrapMe(open('README.md'))
    print(f)
    print(f.get())
    print(f.readline())
    print(f.tell())
    print(f.seek(0))
    f.close()
    f.get()
