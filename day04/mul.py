"""mul 1 - 9.

打印9 9乘法表, 效果如下:
1*1=1
1*2=2 2*2=2
...
1*9=9 2*9=18 ... 9*9=81
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}X{}={}'.format(j, i, i*j), end='\t')
    print()
