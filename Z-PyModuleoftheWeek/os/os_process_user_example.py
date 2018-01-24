# os_process_user_example.py

import os

TEST_GID = 1000
TEST_UID = 1000

def show_user_info():
    print('User (actual/effective)  : {} / {}'.format(
        os.getuid(), os.geteuid()))
    print('Group (actual/effective) : {} / {}'.format(
        os.getgid(), os.getegid()))
    print('Actual Groups  :', os.getgroups())

print('BEFORE CHANGE:')
show_user_info()
print()

try:
    os.setegid(TEST_GID)
except OSError:
    print('ERROR: Could not change effective group.'
    'Rerun as root.')
else:
    print('CHANGE GROUP:')
    show_user_info()
    print()

try:
    os.seteuid(TEST_UID)
except OSError:
    print('ERROR: Could not change effective user.'
    'Rerun as root.')
else:
    print('CHANGE USER:')
    show_user_info()
    print()