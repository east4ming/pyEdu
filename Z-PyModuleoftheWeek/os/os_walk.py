import os
import sys

if len(sys.argv) == 1:
    root = 'C:\\Users\\cuika'
else:
    root = sys.argv[1]

for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name)
    # Make the subdirectory names stand out with /
    sub_dirs = [sub_dir + '\\' for sub_dir in sub_dirs]
    # Mix the directory contents together
    # 两个列表相加, 再按字母排序
    contents = sub_dirs + files
    contents.sort()
    # Show the contents
    for c in contents:
        print('    {}'.format(c))
    print()
