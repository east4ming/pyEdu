class Singleton():
    """通过__new__ 实现简单的单例模式."""
    def __new__(cls):
        # 关键在于这里, 每次实例化, 我们都只会返回同一个instance对象
        # hasattr 用于判断对象是否包含对应的属性。
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(id(obj1) == id(obj2))