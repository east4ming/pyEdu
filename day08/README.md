# day08

## 字典

- 映射类型, 没有下标

### 增加

- `dict()`
- `{}`
- `adict[key] = value`

### 删除

- `del`
- 内部方法`clear()`
- `pop()`

### 字典操作符

- `adict.copy()`
- `dict.get()`  - 查找不存在的key, 默认返回None
- `dict.setdefault()` - 字典的key, 如果有, 不修改; 如果没有, 设置对应key的value为该方法的第二个参数
- `dict.items()`  `dict.keys()` `dict.values()` 
- `adict.update(bdict)`

## 练习

### 使用字典模拟一个用户登陆信息系统

1. 支持新用户注册, 新用户名和密码注册到字典中
2. 支持老用户登陆, 用户名和密码正确提示登陆成功
3. 主程序通过循环询问什么操作, 根据用户的选择, 执行注册或是登陆操作

**技巧**:

- 可以使用`if password != dict.get(): ...`来同时判断用户名或密码是否有问题. 
    - 如果返回None, 表示用户名不存在
    - 如果返回的和password不相等, 表示密码错误
- 不希望密码出现在屏幕上, 使用`getpass`模块: `password = getpass.getpass(prompt)`
    - `getpass`模块在pycharm中运行不正常

## 集合

- 不同元素
- 可hash
- 无序排列
- 有可变和不可变2种集合

### 创建

- `set()` 可变集合
- `frozenset()` 不可变集合
- `{'a', 'b', 'c'}`

### 集合操作

- 交集 `&`  `aset.intersection()`
- 并集 `|`  `aset.union()`
- 补集 `^` `symmetric_difference(other)`
- 差补集  `aset - bset` `difference(*others)`

### 添加

`aset.add(element)`
`aset.update(bset)`

### 用途

- 从大量重复的选项中筛选出有效的(比如, 筛选出access.log中的url)
- 2个集合作运算, 找出差异项

## 时间方法 - time 模块

### 表示方式

- 时间戳timestamp: 从1970年1月1日0:00:00开始过了多少s
- UTC(世界协调时间). 中国为UTC+8   DST(Daylight Saving Time 夏令时)
- 元组(struct_time): 9个元素
    - 0: tm_year
    - 1: tm_mon
    - 2: tm_mday
    - 3: tm_hour
    - 4: tm_min
    - 5: tm_sec
    - 6: tm_wday (星期) **0-6: monday 是0**
    - 7: tm_yday(一年中的第几天)
    - 8: tm_isdst(是否为dst时间) 默认-1
    
### time模块方法

- `time.localtime()` - 返回当前时间的元组
- `time.gmtime()`
- `time.time()` - 时间戳
- `time.mktime()` 元组转换为时间戳
- `time.sleep(secs)`
- `time.asctime([t])`  把一个时间元组表示为可读的时间
- `time.ctime()` - 接受时间戳
- `time.strftime(format[,t])` 
- `time.strptime(string[, format])`

## datetime模块

- `datetime.today()`
- `datetime.now([tz])`
- `datetime.strptime(date_string, format)`
- `datetime.ctime()` 把datetime对象转换为时间格式
- `datetime.strftime()`

### 时间计算

- `timedalta()`

## 异常处理

- NameError
- IndexError
- SyntaxError
- KeyboardInterrupt
- EOFError (EndOfFile)
- IOError

```python
try:
    try_suite # 监控这里的异常
except Exception [as reason]:
    except_suite # 异常处理代码
except ValueError:
    print('xxx')
```

### 主动触发

- raise
- assert - 断言

## os 模块

- symlink()
- listdir()
- ...

## pickle模块

- dump
- load

## 练习

### 记账

1. 记账时, 有10000
2. 无论开销和收入都要记账
3. 内容包括:
    - 时间
    - 金额
    - 说明
4. 永久存储
