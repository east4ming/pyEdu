def make_header(level):
    print('Create decorator')
    # 这部分跟通常的装饰器一样, 只是wrapper通过闭包访问了变量level
    def decorator(func):
        print('Initialize')
        def wrapper():
            print('Call')
            return '<h{0}>{1}</h{0}>'.format(level, func())
        return wrapper
    # make_header 返回装饰器
    return decorator


@make_header(2)
def get_content():
    return 'hello world'


print(get_content())
