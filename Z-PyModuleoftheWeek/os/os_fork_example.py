# os_fork_example.py

import os

pid = os.fork()

if pid:
    print('Child process id:', pid)
else:
    print('I am the child')
