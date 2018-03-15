from time import time, sleep
import functools


# logger(when)是带参数的装饰器
# 真正的装饰器其实是 `logger('pre')` 或 `logger('post')`
def logger(when):
    """日志装饰器, 可以添加参数选择在函数运行 前/后 记录日志"""
    def log(func, *args, **kwargs):
        """打印被装饰函数相关信息

        打印:
        - 函数
        - 位置参数
        - 关键字参数
        不是装饰器, 是辅助函数
        用于被真正的装饰器函数: `pre_log(func)` 和 `post_log(func)`调用
        """
        print("""Called:
function:   {}
args:       {}
kwargs:     {}
""".format(func, args, kwargs))

    # 装饰器函数的参数**仅仅只有一个**func
    def pre_log(func):
        """装饰器: 在函数运行前打印信息

        调用辅助函数 `log(func, *args, **kwargs)`
        传入参数是函数对象 - func
        返回值是函数对象 - wrapper
        """
        @functools.wraps(func)
        # wrapper为闭包, 可以调用外层作用于的func对象. 所以只用写wrapper需要的参数.
        def wrapper(*args, **kwargs):
            log(func, *args, **kwargs)
            # wrapper函数返回的是函数调用 - `func(*args, **kwargs)`
            return func(*args, **kwargs)
        # 装饰器返回的是函数对象 - wrapper
        return wrapper

    def post_log(func):
        """装饰器: 在函数运行后打印信息

        相比`pre_log()`, 额外打印了`func()`执行前后的时间消耗
        调用辅助函数 `log(func, *args, **kwargs)`
        传入参数是函数对象 - func
        返回值是函数对象 - wrapper
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time()
            try:
                # 使用try...finally结构来确保在成功执行`func()`才执行`log()`和打印时间
                # 记得return
                return func(*args, **kwargs)
            finally:
                log(func, *args, **kwargs)
                print('time delta: {}'.format(time()-now))
        return wrapper

    # 主函数, 用于判断具体执行哪个装饰器
    try:
        # 记得还要进行return!!!!!!
        # 通过字典(key是str, value是函数对象. 即返回的还是函数对象(二选一)
        return {'pre': pre_log,
                'post': post_log}[when]
    except KeyError as e:
        raise ValueError('must be "pre" or "post"') from e


@logger('post')
def hello(name):
    print('Hello ', name)
    sleep(5)


hello('World!')
