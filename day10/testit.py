#!/usr/bin/env python

def testit(func, *args, **kwargs):
    try:
        return_value = func(*args, **kwargs)
        result = (True, return_value)
    except Exception as diag:
        result = (False, diag)
    return result


def test():
    funcs = (int, float, str)
    vals = (1234, 12.34, '1234', '12.34')

    for each_func in funcs:
        print('_' * 20)
        for each_val in vals:
            return_value = testit(each_func, each_val)
            if return_value[0]:
                print('{}({!r})= {!r}'.format(each_func.__name__, each_val,
                                         return_value[1]))
            else:
                print('{}({!r})= FAILED: {}'.format(each_func.__name__,
                                                    each_val, return_value[1]))


if __name__ == '__main__':
    test()
