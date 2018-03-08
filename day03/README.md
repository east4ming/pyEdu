# day03

## 上周复习

- 数据类型
- if语句

## 习题回顾

### 猜拳游戏改进

- 放到一个列表, 人输入下标
- 提示放到`prompt`中
- 放到一个字典, 人输入key

## 循环

### while语句

- 结束循环的一种技巧 - 使用变量, 刚开始把变量设置为True, 要结束循环就改为False
- 技巧2: 使用break
- 技巧3: 设置msg为"", 条件为用户输入某个字符串, 如'quit'. 则`while msg != 'quit': ...`

> DRY原则:
> Don't Repeat Yourself
>
> Pythonic
>   `a, b = b, a`

#### else字句

- 循环的else
- 其他语言一般都没有
- 只有循环**正常结束**才会执行

### break

中断循环

### continue

跳过本次循环

### for循环

- 数字不可以迭代
- 字符串/元组/列表/字典可以迭代, 字典迭代的是key

### 两种循环的选择

- 循环次数未知, 采用while循环
- 循环次数已知, 使用for循环