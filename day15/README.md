# day15

> 石博文 shibw@tedu.cn

## re 模块

正则表达式

### findall 函数

查找正则表达式匹配的所有的出现, 返回字符串的列表.

`re.findall(pattern, text)`

### compile 函数

将正则表达式进行编译, 返回一个正则表达式对象
**在大量匹配的情况下, 提升效率**

```python
#re_search_substring.py 
import re

text = 'This is some text -- with punctuation.'
pattern = re.compile(r'\b\w*is\w*\b')

print('Text:', text)
print()

pos = 0
while True:
    match = pattern.search(text, pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print('  {:>2d} : {:>2d} = "{}"'.format(
        s, e - 1, text[s:e]))
    # Move forward in text for the next search
    pos = e
```

### split 方法

根据正则表达式的分隔符, 将其分割为一个列表, 返回匹配的列表

### match 函数

用正则表达式从字符串的**开头**匹配, 如果匹配成功, 则返回一个匹配对象.

### search 函数

匹配正则表达式中**第一次出现**的结果. 匹配到返回一个match object. 匹配不到返回None

### finditer 函数

findall 返回列表; finditer返回迭代器, 每个元素是match object.

### group 方法

使用match或search匹配成功, 返回的匹配对象可以通过group方法获得匹配内容

可以通过`groups()`函数来获取**子组**, 返回一个元组.

`group`  与 `groups` 完全不同

### split 方法

将字符串按照正则表达式进行分割, 分割后的内容放在列表里.

```python
import re
s = 'hello-world.data'
print(re.split('\.|-', s))
```

### sub 方法

把字符串中所有匹配正则表达式的地方替换成新的字符串.

`re.sub(regex, new, string)`

### 正则表达式语法

#### 匹配单个字符

- `.`  任意单个字符
- `[x-y]` 匹配字符组里的任意字符  `[0-9A-Za-z]`
- `[^x-y]` 匹配不在组里的任意字符
- `\d` 任意数字
- `\w` 任意数字字母字符
- `\s` 匹配空白字符

#### 匹配一组字符

- 'foo' 字符串的值
- `re1|re2` 匹配re1或re2
- `*` 匹配前边的表达式0次或多次
- `+` 1次或多次
- `?` 0次或1次
- `{M, N}` m次到n次

#### 其他元字符

- `^` 开始位置
- `$` 字符串的结尾
- `\b` 匹配单词的边界
- `()` 对正则表达式分组
- `\nn` 匹配

#### 贪婪匹配

`*+?` 默认都是贪婪匹配操作符, 再在其后加上`?`取消贪婪匹配. (贪婪: 尽可能多的向后匹配内容)