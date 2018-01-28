"""fibonacci list.

某个数字, 为前两个数之和
10个数字的数列
"""
# def fibonacci(length):
#     fib = [0, 1]
#     for i in range(2, length):
#         fib.append(fib[i-2] + fib[i-1])
#     return fib


def fibonacci(length):
    fiba = 0
    fibb = 1
    for i in range(length):
        print(fiba, end='\t')
        fiba, fibb = fibb, fiba + fibb
    print()


length = int(input('Please input the length what you want:'))
fibonacci(length)
