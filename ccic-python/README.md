# Python 企业开发

## 文件注释
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

## 数据类型与操作

- 整形
- 字符串
    - 字符串拼接： 通过“+”号
    - 字符串填充： 通过“%”或`fromat()`方法
    - 多行注释： 3个引号`""""""` `''''''`
- 布尔
    - True
    - False
- 列表： 有序集合
    - 长度： `len()`
    - 元素可以不是同一类型， 可以内嵌list
    - 切片
    - 列表元素追加：`append()`
    - 列表拓展： `extend(list)`
    - 删除： `pop(index)` `remove(value)`
    - 修改元素：索引赋值
- 元组： 不可变有序
    - 里边可以嵌套list， 但是不建议
- 字典： dict
    - 修改： 通过key-value修改
    - 添加元素： 直接添加key-value    
- 集合： set
    - 交集： `&`
    - 并集： `|`
    - 差集： `-`
    - 可以通过set去重
- None：
    - 空的列表/元组
    - 整数： 0
    - 空的字典/集合

## 循环和遍历

### for

### while

## 函数

### 内置函数

- `cmp()`
- `hash()`
- `len()`
- `list()`
- `max()`
- `sum()`
- `range()`
- `tuple()`