import os
import time


if os.fork():
    print("in parent sleeping...")
    # os.WNOHANG 是os模块常量, 值为1
    # print(os.waitpid(-1, 0))
    print(os.waitpid(-1, os.WNOHANG))
    time.sleep(5)
    print("parent exit")
else:
    print("in child sleeping...")
    time.sleep(10)
    print("child exit")
