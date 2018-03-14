class MakeBold():
    """html加粗装饰器"""
    def __init__(self, func):
        print('Initialize')
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Call')
        return '<b>{}</b>'.format(self.func(*args, **kwargs))


@MakeBold
def get_content():
    return 'hello world'


print(get_content())
