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
    fib = [0, 1]
    for i in range(length-2):
        fib.append(fib[-1] + fib[-2])
    return fib


length = int(input('Please input the length what you want:'))
fib = fibonacci(length)
print(len(fib))
print(fib)
