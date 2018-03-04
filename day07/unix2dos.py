"""unix to dos

python3 unix2dos.py test.txt

将每行行尾的`\n`转换为`\r\n`
"""

import sys


def unix2dos(file):
    dst = file + '.txt'
    with open(file) as src_obj:
        with open(dst, 'w') as dst_obj:
            for line in src_obj:
                line = line.rstrip('\r\n') + '\r\n'
                dst_obj.write(line)


if __name__ == '__main__':
    unix2dos(sys.argv[1])
