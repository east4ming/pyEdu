def set_age(name, age):
    if not 0<age<100:
        raise ValueError("Age out of range.")
    print("{} is {} years old".format(name, age))


def set_age2(name, age):
    assert 0<age<100, 'Age out of range.'
    print("{} is {} years old".format(name, age))


if __name__ == '__main__':
    set_age('amy', 25)
    set_age2('bob', 250)
