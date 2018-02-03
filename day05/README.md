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