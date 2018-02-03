"""100块钱买100只鸡

- 公鸡5块钱一只
- 母鸡3块钱一只
- 3只小鸡1块钱

问有几种买法?
"""
for cock in range(21):
    for hen in range(34):
        chick = 100 - cock - hen
        if cock * 5 + hen * 3 + chick / 3 == 100:
            print(cock, hen, chick)
