def make_bold(func):
    print('Initialize')
    def wrapper():
        print('Call')
        return '<b>{}</b>'.format(func())
    return wrapper


@make_bold
def get_content():
    return 'hello world'


print(get_content())
