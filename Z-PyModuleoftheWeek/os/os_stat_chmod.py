# os_stat_chmod.py

import os
import stat

filename = 'os_stat_chmod_example.txt'
if os.path.exists(filename):
    os.unlink(filename)
with open(filename, 'wt') as f:
    f.write('contents')

# Determine what permissions are already set using stat
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)
print(existing_permissions)

if not os.access(filename, os.X_OK):
    print('Adding execute permission')
    # RW: 6即110, S_IXUSR: 1即001. 做 | 即为111, 7
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # use xor to remove the user execute permission
    # 异或, 111 ^ 001 为110(1 ^ 1为0)
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(filename, new_permissions)
