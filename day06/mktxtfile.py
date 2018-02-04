"""
创建txt文件.

1. 要求用户输入文件名
2. 以存在, 要求重新输入
3. 提示输入数据, 每行数据先写到列表中
4. 将列表数据写道用户输入的文件名中
"""
import os


def get_fname():
    """输入文件名并返回, 如果已存在, 重新输入."""
    while True:
        fname = input('请输入文件名: ')
        if not os.path.exists(fname):
            break
        print('文件已存在, 请重新输入: ')
    return fname


def get_contents():
    contents = ''
    print('\n请输入文件内容(输入"end"结束)')
    while contents[-5:] != '\nend\n':
        line = input('>>> ') + '\n'
        contents += line
    contents = contents[:-4]
    return contents

    # contents = []
    # print('\n请输入文件内容(输入"end"结束)')
    # while True:
    #     line = input('>>> ')
    #     if line == 'end':
    #         break
    #     contents.append(line + '\n')
    # return contents


def write_file(fname, contents):
    with open(fname, 'w') as fobj:
        fobj.write(contents)
        # fobj.writelines(contents)


if __name__ == '__main__':
    fname = get_fname()
    contents = get_contents()
    write_file(fname, contents)
