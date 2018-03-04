# Day05

## 回顾

### 作业

- 函数
    - 默认参数
    - 返回值
- string 模块
    - 模块内的各种变量: 大小写字母/数字/符号/空白...
- random模块
    - choice
- 代码执行效率
    - 尽量少循环嵌套
    - 判断条件优化精简

### pycharm 使用

- ctrl + b 或ctrl + 点击 调转到函数声明和源码
- ctrl + j 插入模板

## Shutil 模块

- shutil.copyfileobj() - 可以拷贝网络流
- shutil.copyfile() - 相当于shell的`copy`
- shutil.copymode() - 只拷贝权限, 如777
- shutil.copystat() - 只拷贝stat
- shutil.copy() - 可以拷贝文件到文件或目录
- shutil.copy2() - 拷贝文件 + stat
- shutil.copytree() - 拷贝文件夹
- shutil.rmtree() - 删除文件夹
- shutil.move() - 相当于shell的`move`
- shutil.chown() - 相当于shell的`chown`
- shutil.disk_usage() - 相当于`du`
- shutil.which() - 相当于`which`
- shutil.make_archive()
- shutil.get_archive_formats()
- shutil.unpack_archive()
- shutil.get_terminal_size()

## 语法风格

- 支持链式多重赋值
    - 查看内存引用`id`
- 多元赋值
- 合法的标识符
    - 第一个字符: 字母或下划线
    - 其他字符: 字母数字下划线
    - 大小写敏感
- 关键字
    - `keyword`模块
    - `keyword.kwlist` - 关键字列表
    - `keyword.iskeyword()`
- 内建
    - python运行就会加载的名字, 可以被覆盖(但尽量不要覆盖)
- 模块结构和布局
    - ctrl + alt + l 格式化代码

```python
#!/usr/bin/env python  # 起始行
"""this is a test module.

description...
"""  # 模块文档字符串
import sys  # 导入模块

debug = True  # 全局变量


class FooClass():
    """Foo Class."""
    pass


def test():
    """test function"""
    foo = FooClass()


if __name__ == '__main__':
    test()
```

## 练习

### 创建文件

1. 要求用户输入文件名
2. 以存在, 要求重新输入
3. 提示输入数据, 每行数据先写到列表中
4. 将列表数据写道用户输入的文件名中

## 列表推导式

```python
[x*x for x in range(1, 6) if x%2==0]
```

## 序列对象

### 共有操作

- `seq[ind]`
- `seq[ind1:ind2:step]`
- `seq * expr`
- `seq1 + seq2`
- `obj in seq`  `obj not in seq`
- `s.index(x)`
- `s.count(x)` - s序列中x的出现次数
### 内建函数

- `list(iter)`
- `tuple(iter)`
- `str(obj)`
- `len(seq)`
- `max(iter, key=None)`  `min(iter, key=None)`
- `enumerate(iter)`
- `reversed()`
- `sorted()`

```python
alist = ['abc', 'def', 'xgsd']
for ind in range(len(alist)):
    print('{}: {}'.format(ind, alist[ind]))
for ind, val in enumerate(alist):
    print('{}: {}'.format(ind, val))
```

### 字符串操作

- `ord(a)` - 返回对应的ascii码数字
- 比较操作 - 按ascii比较
- 小写字母从97开始, 大写字母从65开始

### 作业

#### 检查标示符

1. 接受用户输入
2. 判断用户输入的标示符是否合法
3. 用户输入的标示符不能使用关键字
4. 有不合法字符, 需要指明第几个不合法

### 格式化输出

- `%c` - 根据ascii转换为字符
- `%s`
- `%d` - 转换成整数
- `%o` - 转换为无符号八进制输出
- `%#o` - 转换为带前缀的
- `%#x` - 十六进制
- `%e` - 科学记数法
- `%f` - 浮点数
- `%4.2f` - 总宽度为4, 小数位占2位
- `%12s%-8s` - 第一个占12个宽度, 右对齐; 第二个占8个宽度, 左对齐
- `% d` 正整数前面空格, 负整数前面没有空格
- `%+d` 正整数前面'+'填充
- `%010d` 用0填充, 10位

#### format 方法

语法:
```
replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | integer]
attribute_name    ::=  identifier
element_index     ::=  integer | index_string
index_string      ::=  <any source character except "]"> +
conversion        ::=  "r" | "s" | "a"
format_spec       ::=  <described in the next section>
```

一些简单的示例:
```python
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.
```

关于conversion的用法示例:
```python
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first
```

format_spec相关用法:
```
format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  integer
grouping_option ::=  "_" | ","
precision       ::=  integer
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X
```

#### 案例 - 创建用户

1. 实现创建用户功能
2. 提示输入用户名
3. 随机生成8位密码
4. 创建用户并设置密码
5. 将用户相关信息写入指定文件

### 字符串内建函数

- `str.endswith()` `str.startswith()`
- `str.center()` `str.ljust()` `str.rjust()`
- `str.capitalize()` `str.title()` 
- `str.count()`
- `str.isupper()` `str.islower()` 
- `str.isdigits()` `str.isalpha()` `str.isalnum()`
- `str.upper()` `str.lower()`
- `str.strip()` `str.lstrip()` `str.rstrip()`
- `str.split()`

### 列表

- `lst.append()`
- `lst.insert(1, 15)` 在下标位1的位置写入15
- `lst.count()`
- `lst.index()`
- `lst.pop()` 移除列表最后一个, 并返回该值
- `lst.pop(2)` 下标为2
- `lst.remove('bob)`  将bob从列表中remove
- `lst.sort()` 改变列表本身(字符串和数字sort会报错)
- `lst.reverse()` 
- `lst.copy()` 只将值拷贝到新列表
- `lst.clear()` 清空
- `lst.extend()` 

### 作业

