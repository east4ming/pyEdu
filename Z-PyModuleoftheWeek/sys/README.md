# `sys` - 系统相关配置

> 目的: 提供系统相关的配置和操作
> 原文链接: [sys — System-specific Configuration](https://pymotw.com/3/sys/index.html)

sys模块包括用于在运行时探测或改变解释器的配置的服务的集合以及用于与当前程序之外的操作环境交互的资源。

[TOC]

## 解释器设置

`sys`包含用于访问解释器的编译时或运行时配置设置的属性和函数。

### 编译版本信息

用于构建c解释器的版本有几种形式。sys.version是一个人类可读的字符串，通常包含完整的版本号以及有关构建日期，编译器和平台的信息。因为sys.hexversion是一个简单的整数，所以它更容易用来检查解释器的版本。当使用hex（）进行格式化时，显然sys.hexversion的一部分来自版本信息，这些版本信息在更可读的sys.version_info（仅代表版本号的五部分namedtuple）中也是可见的。当前解释器使用的单独的c api版本保存在sys.api_version中。

> 具体见`sys_version_values.py`

所有的值都取决于用来运行示例程序的实际解释器。
用于构建解释器的操作系统平台保存为sys.platform。

> 具体见`sys_platform.py`

对于大多数unix系统来说，其值来自`uname -s`的输出与`uname -r`中版本的第一部分的结合。对于其他操作系统，有一个硬编码的值表。

> 参见:
> - [Platform values](https://docs.python.org/3/library/sys.html#sys.platform) - 没有uname的系统的sys.platform的硬编码值。

### 解释器执行

cpython解释器是Python语言的几个实现之一。提供了sys.implementation来检测库的当前实现，这些库需要解决解释器中的任何差异。

> 具体见`sys_implementation.py`

sys.implementation.version与cpython的sys.version_info相同，但对于其他解释器而言将会不同。

> 参见:
> - [PEP421](https://www.python.org/dev/peps/pep-0421) - 增加`sys.implementation`

### 命令行选项

cpython解释器接受几个命令行选项来控制其行为，如下表所列。

| 选项    | 含义                              |
| ----- | ------------------------------- |
| `-B`  | 不要在导入时写入.py [co]文件              |
| `-b`  | 发出有关将字节转换为字符串而不正确解码和比较字节与字符串的警告 |
| `-bb` | 将字节警告转换为错误                      |
| `-d`  | 从解析器调试输出                        |
| `-E`  | 忽略PYTHON 环境变量（如PYTHONPATH）     |
| `-i`  | 运行脚本后交互式检查                      |
| `-O`  | 稍微优化生成的字节码                      |
| `-OO` | 除-O优化外，还要除去doc-strings          |
| `-s`  | 不要将用户站点目录添加到sys.path            |
| `-S`  | 初始化时不要运行`import site`                  |
| `-t`  | 发出有关标签使用不一致的警告                  |
| `-tt` | 为不一致的选项卡使用发出错误                  |
| `-v`  | 详细                              |

其中一些可用于程序检查 `sys.flags`。

> 具体见`sys_flags.py`

### 默认编码

获取解释器正在使用的默认unicode编码的名称，调用getdefaultencoding（）。该值在启动时设定，不能更改。
对于某些操作系统，内部编码默认值和文件系统编码可能不同，因此有一种单独的方式来检索文件系统设置。getfilesystemencoding（）返回特定于操作系统（而不是文件系统特定）的值。

> 具体见`sys_unicode.py`

大多数unicode专家建议不要使用全局默认编码，而是应该明确指出unicode。这提供了两个好处：针对不同数据源的不同Unicode编码可以被更干净地处理，并且减少了关于编码在应用程序代码中的假设数量。

### 交互式提示

交互式解释程序使用两个单独的提示来指示默认输入级别（ps1）和多行语句（ps2）的“延续”。这些值只能由交互式解释器使用。

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>>
```

一个或两个提示可以更改为不同的字符串。

```python
>>> sys.ps1 = '::: '
::: sys.ps2 = '~~~ '
::: for i in range(3):
~~~   print(i)
~~~
0
1
2
:::
```

或者，可以将任何可以转换为字符串的对象（通过__str__）用于提示。

> 具体见`sys_ps1.py`

### 显示钩子

每次用户输入表达式时，交互式解释器都会调用sys.displayhook。评估表达式的结果作为函数的唯一参数传递。

> 具体见`sys_displayhook.py`

默认值（保存在`sys .__ displayhook__`中）将结果打印到标准输出并保存在`_`中以便稍后参考。

### 安装位置

在解释器路径有意义的所有系统上，`sys.executable`中的实际解释程序的路径是可用的。这对于确保正在使用正确的解释器是有用的，并且还提供了可能基于解释器位置设置的路径的线索。
`sys.prefix`引用解释器安装的父目录。它通常分别包含可执行文件和已安装模块的`bin`和`lib`目录。

> 具体见`sys_locations.py`

## 运行时环境

sys通过接受命令行参数，访问用户输入以及将消息和状态值传递给用户，提供了与应用程序之外的系统进行交互的低级别API。

### 命令行参数

解释器捕获的参数在那里被处理，而不会传递给正在运行的程序。任何剩余的选项和参数，包括脚本本身的名字，都保存到sys.argv中，以防程序确实需要使用它们。

> 具体见`sys_argv.py`

在第三个例子中，-u选项被解释器理解，并且不被传递给正在运行的程序。

```shell
$ python3 sys_argv.py

Arguments: ['sys_argv.py']

$ python3 sys_argv.py -v foo blah

Arguments: ['sys_argv.py', '-v', 'foo', 'blah']

$ python3 -u sys_argv.py

Arguments: ['sys_argv.py']
```

> **参见:**
> - [argparse](https://pymotw.com/3/argparse/index.html#module-argparse) - 用于解析命令行参数的模块。

### 输入输出流

遵循unix范例，python程序默认可以访问三个文件描述符。

> 具体见`sys_stdio.py`

stdin是通常从控制台读取输入的标准方式，也是通过管道从其他程序读取输入的标准方式。标准输出是将输出写入用户（到控制台）或者发送到管道中的下一个程序的标准方式。stderr旨在用于警告或错误消息。

```shell
$ cat sys_stdio.py | python3 -u sys_stdio.py

STATUS: Reading from stdin
STATUS: Writing data to stdout
#!/usr/bin/env python3

#end_pymotw_header
import sys

print('STATUS: Reading from stdin', file=sys.stderr)

data = sys.stdin.read()

print('STATUS: Writing data to stdout', file=sys.stderr)

sys.stdout.write(data)
sys.stdout.flush()

print('STATUS: Done', file=sys.stderr)
STATUS: Done
```

> **参见:**
> [subprocess](https://pymotw.com/3/subprocess/index.html#module-subprocess) 和 `pipes` - 子进程和管道都具有流水线程序的功能。

### 返回状态

从程序返回一个退出代码，将一个整数值传递给sys.exit（）。

> 具体见`sys_exit.py`

非零值意味着程序退出时出错。

## 内存管理和限制

sys包含了一些理解和控制内存使用的函数。

### 引用计数

python（cpython）的主要实现使用引用计数和垃圾回收进行自动内存管理。一个对象被自动标记为在其引用计数下降到零时收集。要检查现有对象的引用计数，请使用getrefcount（）。

> 具体见`sys_getrefcount.py`

报告的值实际上比预期值大1，因为存在由getrefcount（）本身持有的对象的临时引用。

> **参见:**
> [gc](https://pymotw.com/3/gc/index.html#module-gc) - 通过gc中暴露的函数来控制垃圾收集器。

### 对象大小

知道一个对象有多少引用可能有助于查找周期或内存泄漏，但仅仅确定哪些对象消耗的内存最多是不够的。这需要关于大对象的知识。

> 具体见`sys_getsizeof.py`

getsizeof（）以字节(bytes)报告对象的大小。

报告的自定义类的大小不包含属性值的大小。

> 具体见`sys_getsizeof_object.py`

这可能会给正在使用的内存数量造成误解。
为了更全面地估计一个类所使用的空间，提供一个__sizeof __（）方法来计算该值，方法是聚合一个对象的属性大小.

> 具体见`sys_getsizeof_custom.py`

此版本将对象的基本大小添加到存储在内部__dict__中的所有属性的大小。

### 递归

允许在python应用程序中进行无限递归可能会在解释器本身引入堆栈溢出，导致崩溃。为了消除这种情况，解释器提供了使用setrecursionlimit（）和getrecursionlimit（）来控制最大递归深度的方法。

> 具体见`sys_recursionlimit.py`

一旦堆栈大小达到递归限制，解释器引发一个RuntimeError 异常，所以程序有机会处理这种情况。

### 最大值

以及运行时可配置值，sys包含定义各系统类型的最大值的变量。

> 具体见`sys_maximums.py`

maxsize是由c解释程序的大小类型指定的列表，字典，字符串或其他数据结构的最大大小。maxunicode是当前配置的解释器支持的最大整数unicode点。

### 浮点值

结构float_info包含有关解释器使用的浮点类型表示的信息，这些信息是基于底层系统的float实现。

> 具体见`sys_float_info.py`

这些值取决于编译器和底层系统。

> **参见:**
> 本地编译器的float.h c头文件包含有关这些设置的更多详细信息。

### 整数值

结构int_info保存关于解释器使用的整数的内部表示的信息。

> 具体见`sys_int_info.py`

当解释器被构建时，用于在内部存储整数的c类型被确定。默认情况下，64位体系结构自动使用30位整数，并且可以使用配置标志--enable-big-digits为32位体系结构启用它们。

> **参见:**
> [Build and C API Changes](https://docs.python.org/3.1/whatsnew/3.1.html#build-and-c-api-changes) from What's New in Python 3.1

### 字节顺序

字节顺序被设置为本地字节顺序。

```python
sys_byteorder.py
import sys

print(sys.byteorder)
```
值为大端或小端.

> See also
>
> - [Wikipedia: Endianness](https://en.wikipedia.org/wiki/Byte_order) – Description of big and little endian memory systems.
>
> - [`array`](https://pymotw.com/3/array/index.html#module-array) and [`struct`](https://pymotw.com/3/struct/index.html#module-struct) – Other modules that depend on the byte order of data.
>
> - - `float.h` – The C header file for the local compiler contains
>
>     more details about these settings.

## 异常处理

sys包含用于捕获和处理异常的功能。

### 未处理的异常

许多应用程序的结构都是一个主循环，它将执行封装在全局异常处理程序中，以捕获不在较低级别处理的错误。另一种实现同样事情的方法是将sys.excepthook设置为一个带有三个参数（错误类型，错误值和回溯）的函数，并让它处理未处理的错误。

> 具体见`sys_exceptionhook.py`

因为没有`try: except`块, 引发异常，即使设置了异常挂钩，下面的print（）调用也不会运行。

### 当前异常

有些时候显式的异常处理程序是首选的，无论是为了清晰的代码，或避免与试图安装自己的excepthook库的冲突。在这些情况下，通过调用exc_info（）来检索线程的当前异常，可以创建一个通用的处理函数，该函数不需要明确地传递异常对象。

> 具体见`sys_exc_info.py`

这个例子避免了在traceback对象和当前帧中的局部变量之间引入一个循环引用，忽略exc_info（）的那部分返回值。如果需要回溯（例如，可以记录），则显式删除本地变量（使用del）以避免周期。

### 以前的互动例外

在交互式解释器中，只有一个交互线程。该线程中未处理的异常保存到`sys`（`last_type`，`last_value`和`last_traceback`）中的三个变量中，以便于检索它们以进行调试。使用pdb中的postmortem调试器可以避免直接使用这些值。

```python
$ python3
Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def cause_exception():
...     raise RuntimeError('This is the error message')
...
>>> cause_exception()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in cause_exception
RuntimeError: This is the error message
>>> import pdb
>>> pdb.pm()
> <stdin>(2)cause_exception()
(Pdb) where
  <stdin>(1)<module>()
> <stdin>(2)cause_exception()
(Pdb)
```

> **参见:**
> - exceptions - 内置错误
> - pdb - Python调试器
> - traceback - Module for working with tracebacks

## 低级别线程支持

> 待补充
## 模块和导入

> 待补充

## 在运行时追踪程序

> 待补充
