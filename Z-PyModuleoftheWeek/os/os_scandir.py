# os_scandir.py
# 如果需要的不只只是文件的名字, 那么使用`scandir()`会更有效
# 因为在一个系统中, 当目录被扫描, 更多的信息会被收集
# `scandir()`返回一个目录items的*DirEntry*实例.
# 该对象有几个属性和来访问该文件元数据的方法.

import os
import sys

for entry in os.scandir(sys.argv[1]):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name} {typ}'.format(
        name=entry.name,
        typ=typ,
    ))
