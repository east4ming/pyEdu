import os


print("starting....")
pid = os.fork()
if pid:
    print('hello from parent')
else:
    print('hello from child')
