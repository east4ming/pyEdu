import os
import time


print("starting...")
if os.fork():
    print("In parent")
    time.sleep(10)
    print("parent exit")
else:
    for i in range(5):
        print(time.ctime())
        time.sleep(1)
    print("child exit")

