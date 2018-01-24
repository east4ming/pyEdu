# os_directories.py

import os

# 创建目录
dir_name = 'os_directories_example'
print('Creating', dir_name)
os.makedirs(dir_name)

# 创建文件
filename = os.path.join(dir_name, 'example.txt')
print('Creating', filename)
with open(filename, 'wt') as f:
    f.write('example file')

# 删除
print('Cleaning up')
os.unlink(filename)
os.rmdir(dir_name)
