import functools


def make_bold(func):
    print('Initialize')
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Call')
        return '<b>{}</b>'.format(func(*args, **kwargs))
    return wrapper


@make_bold
def get_content():
    """Return page content"""
    return 'hello world'


print(get_content())
print(get_content.__name__)
print(get_content.__doc__)