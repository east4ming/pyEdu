# day12

## OOP 面向对象

- 类
- 示例化
- 方法
- 对象

### 构造器方法

```python
class BearToy():
    def __init__(self, size, color):
        self.size = size
        self.color = color
```

### __new__

#### __new__ 方法是什么

在2.2以后的版本中, 随着类型(type)和类(class)的统一和新式类的引入, 可以对**标准类型**进行子类化.
下面介绍2个子类化Python类型的例子, 一个是可变类型, 另一个是不可变类型.

__new__方法接受的参数虽然也是和__init__一样，但__init__是在**类实例创建之后调用**，而 __new__方法正是**创建这个类实例**的方法。
__init__ 和 __new__ 最主要的区别在于：

1. __init__ 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
2. __new__ 通常用于控制生成一个新实例的过程。它是类级别的方法。

> 具体见*person.py*

#### __new__ 作用

依照Python官方文档的说法，__new__方法主要是当你继承一些**不可变**的class时(比如int, str, tuple)， 提供给你一个**自定义这些类的实例化过程**的途径。还有就是实现**自定义的metaclass**。

如, 我们想要一个永远都是正数的整数类型, 通过继承int, 代码如下:

> 具体见 *pos_int.py*

处理浮点型的子类. 每次得到一个货币值(浮点型), 需要通过四舍五入, 变为带2位小数的数值.

> 具体见 *round_float.py*

#### 用`__new__`实现单例

实现 设计模式中的 单例模式(singleton) 。
因为类每一次实例化后产生的过程都是通过__new__来控制的，所以通过重载__new__方法，我们 可以很简单的实现单例模式。

> 见*singleton.py*

## 多重继承

mixin

## 类 内建函数

### issubclass()

### isinstance()

第二个参数可以是类, 可以是类型对象(int等)

### hasattr() getattr() setattr() delattr()

`*attr()`系列函数可以在各种对象下工作, 不限于类和实例.

- hasattr(): 一个对象是否有一个特定的属性, 一般用于访问某属性之前先做一下检查
- getattr() setattr(): 取得和赋值给对象的属性.
    - getattr(): 试图读取一个不存在的属性时, 引发 AttributeError 异常
    - setattr(): 要么加入一个新的属性, 要么取代一个已存在的属性.
- delattr(): 从一个对象中删除属性

### dir()

- 作用在**实例**上时, 显示**实例变量**, 还有在实例所在的类及所有它的基类中定义的**方法和类属性**
- 作用在**类**上时, 显示类以及它的所有基类的`__dict__`中的内容. 但不会显示定义在元类(metaclass)中的类属性.
- 作用在**模块**上时, 显示模块的`__dict__`的内容
- 不带参数时, 显示调用者的局部变量.

### super()

帮助程序员找出对应的父类, 然后方便调用相关的属性.

### vars()

与dir()类似, 只是给定的 对象参数必须有一个`__dict__`属性.
vars()返回一个字典, 包含了对象存储于其`__dict__`中的属性(key)和值.
如果没有这样的属性, 会引发TypeError异常. 
如果没有提供对象作为vars()的一个参数, 它将显示一个包含本地名字空间的属性(key)及其值的字典, 也就是: locals()

## 用特殊方法定制类

特殊方法可以:

- 模拟标准类型
- 重载操作符(+-*/, 下标, 映射)

以双下划线(__)开头和结尾.

### 基本定制型

- `__init__`  构造器
- `__new__` 构造器(通常用在设置不变数据类型的子类)
- `__del__` 解构器
- `C.__str__(self)` 可打印的字符输出: 内建str()及print语句
- `C.__repr__(self)` 运行时的字符串输出; 内建repr()和''操作符
- `C.__unicode__(self)` Unicode字符串输出; 内建unicode()
- `C.__call__(self, *args, **kwargs)` 可调用的实例
- `__nonzero__` 为object定义False值; 内建bool()
- `__len__` 长度(可用于类); 内建len()

### 对象(值)比较

- `__cmp__(self, obj)` 对象比较; 内建cmp()
- `__lt__` le eq ne gt ge < <= = != > >=

### 属性

- `__getattr__(self, attr)` 获取属性; 内建getattr(); 仅当属性没有找到时调用
- `__setattr__(self, attr, val)` 设置属性
- `__delattr__(self, attr)` 删除属性
- `__getattribute__(self, attr)` 获取属性; 内建 getattr(); 总是被调用
- `__get__(self, attr)` (描述符)获取属性
- `__set__(self, attr, val)` (描述符)获取属性
- `__delete__(self, attr)` (描述符)删除属性

### 模拟类型

#### 数值类型: 二元操作符

- `__add__(self, obj)` sub mul
- truediv /
- floordiv //
- mod %
- divmod divmod()
- pow pow() **
- lshift <<
- rshift >>
- and &
- or |
- xor ^

#### 数值类型: 增量赋值

- iadd isub imul imatmul itruediv ifloordiv imod ipow ilshift irshfit iand ixor ior += ...

#### 数值类型: 一元操作符

- neg 负
- pos 正
- abs 绝对值; 内建abs()
- invert按位求反; ~ 操作符

#### 数值类型: 数值转换

- complex 转为complex(复数); 内建complex()
- int
- float
- round

#### 数值类型: 数值压缩

- index

#### 序列/映射类型

- len 序列中项的数目
- getitem(self, key) 得到单个序列元素
- setitem(self, key, val) 设置单个序列元素
- delitem(self, key) 删除单个序列元素
- contains 测试序列成员; 内建in关键字
- reversed reversed()
- hash
- missing(self, key) 给定键如果不存在字典中, 则提供一个默认值

#### with

- `__enter__(self)`
- `__exit__(self, exc_type, exc_value, traceback)`

### 简单实现(RoundFloat2)

> 见*round_float2.py*

### 数值定制(Time60)

用来操作时间, 精确到小时和分.

> 具体见*time60.py*

### 迭代器

> 见*rand_seq.py*和*any_iter.py*

### 多类型定制

创建一个新类, NumStr, 由一个数字-字符对组成, 几位n和s, 数值为int.

> 具体见*numstr.py*

## 授权

### 包装

包装就是一个希望将某个对象（或类），进行重新打包，装换成另外一种更适合当前使用场合的对外接口。
相似娱乐界对明星的包装一样，其实本质没有什么改变，只是表面变得更容易受当下人欢迎而已。用到程序编程中，就是将程序包装成，当前环境跟适合的样子（主要是对外接口）。
一个例子，假如一个类中包含了许多的数据属性，同时也包含了许多的基本操作函数，
但是我们要求得这个类的对象的某个值（来自于对这个类对象中的各个数据属性和操作函数的多次操作），那么是不是每次都需要做一遍这样的事情呢？理论上是这样的，
有人会说，那为什么不在当初定义类的时候就定义一个这样的函数呢？对！但是，当初定义的时候或许想不到这些，而更为重要的是，如果将某个类定义的过分应用于某个情景，
那么这个类就并不好在其他地方使用，而如果把它实际到适合在许多情景中使用，那又会是类变得特别的负责，所以基本上，我们认为类应该设计的比较基本为好。

### 授权

#### 包装对象的简单例子

> 见*wrap_me.py*

#### 为对象添加时间戳

为对象加上创建时间(ctime), 修改时间(mtime), 访问时间(atime).

- 创建时间: 实例化的时间
- 修改时间: 核心数据升级的时间(通常会调用新的set()方法)
- 访问时间: 最后一次对象的数据值被获取或者属性被访问的时间戳.

> 见*twrapme.py*