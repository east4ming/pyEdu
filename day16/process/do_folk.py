import os

print('Process ({}) start...'.format(os.getpid()))
# Only works on Unix/Linux/Mac
pid = os.fork()
if pid == 0:
    print('I am child process ({}) and my parent is ({})'.format(os.getpid(),
                                                                 os.getppid()))
else:
    print('I ({}) just created a child process ({})'.format(os.getpid(), pid))
