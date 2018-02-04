"""check identifier.

1. 接受用户输入
2. 判断用户输入的标示符是否合法
3. 用户输入的标示符不能使用关键字
4. 有不合法字符, 需要指明第几个不合法
"""
import keyword
import string
import sys

first_ch = string.ascii_lowercase + '_'
all_chs = first_ch + string.digits


def isvalid_identifier(identifier):
    if identifier[0] not in first_ch:
        # 满足条件, 直接返回, 函数结束
        return (0, identifier[0])
    for ind, value in enumerate(identifier, start=1):
        if value not in all_chs:
            return (ind, value)


def main():
    # identifier = input('请输入一个标示符: ')
    identifier = sys.argv[1]
    if keyword.iskeyword(identifier):
        print('该标示符是关键字')
    else:
        invalid_ind, invalid_value = isvalid_identifier(identifier)
        if invalid_value:
            print('该标示符第{}个字符不合法, 为{}'.format(invalid_ind+1, invalid_value))
        else:
            print('该标示符合法.')


if __name__ == '__main__':
    main()
