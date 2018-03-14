# day10

## lambda

## filter()

## map()

## reduce()

位于模块`functools`中

## 变量作用域

### 全局变量

特征： 除非被删除掉， 否则它们的存活到脚本运行结束， 且对于所有的函数， 它们的值都是可以被访问的。

### 局部变量

如果局部域全局有相同名称的变量， 函数运行时， 局部变量的名称会把全局变量名称覆盖。

### global 语句

因为全局变量的名字能被局部变量给覆盖掉， 所以为了明确地引用一个已命名的全局变量， 必须使用`global`语句。

### 命名空间

任何时候， 总有一个到三个活动的作用域：

- 内建
- 全部
- 局部

标识符搜索顺序依次是：

1. 局部
2. 全局
3. 内建

## 函数式编程

### 偏函数

将函数式编程的概念和默认参数以及可变参数结合在一起
一个带有多个参数的函数， 如果其中某些参数基本上固定， 就可以通过偏函数为这些参数赋默认值

```
>>> from operator import add
>>> from functools import partial
>>> add10 = partial(add, 10)
>>> print(add10(25))
35
```

### 作业

#### 窗口程序

1. 3个按钮
2. 两个按钮前景色为白色， 背景色为蓝色
3. 第三个按钮前景色为红色， 背景色为红色
4. 按下第三个按钮， 程序退出

### 递归函数

函数包含对自身的调用。
在操作系统中， 查看某一目录内所有文件/修改权限等都是递归的应用。

```python
def func(num):
     if num == 1:
         return 1
     else:
         return num * func(num - 1)
```

## 要点

字典Value为函数:
`ops = {'+': add, '-': sub}`

`random.choice()`参数可以为字符串: `op = choice('+-')`
列表解析式: `nums = [randint(1, 10) for i in range(2)]`
对之前字典Value为函数的操作以及不定参数: `ans = ops[op](*nums)`
`except`可以后跟元组, 包含多个异常: `except (KeyboardInterrupt, EOFError, ValueError)`

### 装饰器

- 入参是**函数对象**，
- 返回是**函数对象**

```
@make_bold
def get_content():
    return 'hello world'

# 上面的代码等价于下面的

def get_content():
    return 'hello world'
get_content = make_bold(get_content)
```