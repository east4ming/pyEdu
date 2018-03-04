"""除法操作 - 捕获各类异常"""


try:
    num = int(input("number:"))
    result = 100 / num
except ValueError:
    print('请输入数字')
except ZeroDivisionError:
    print('不允许使用0')
except KeyboardInterrupt:
    print('Bye-bye')
except EOFError:
    print('Bye-bye')
else:
    print(result)
finally:
    print('Done') # 不管异常是否发生, 都要执行
