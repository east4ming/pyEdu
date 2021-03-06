class Person(object):
    """Silly Person"""
    def __new__(cls, name, age):
        print('__new__ called.')
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: {}({})>'.format(self.name, self.age)


if __name__ == '__main__':
    caseycui = Person('CaseyCui', 26)
    print(caseycui)
