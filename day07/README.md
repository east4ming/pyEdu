# day07

## 作业

### 实现栈结构

可以通过在字典里保存**函数**, 然后根据key来执行对应的函数

```python
cmds = {'0': push_it, '1': pop_it, '2': view_it}
cmds['0']()
```

### unix2dos程序

1. windows文本文件行结束标志位  `\r\n`
2. 类nuix文本文件行结束标志 `\n`
3. 编写程序, 将unix文本文件格式转换为windows文本文件格式

**技巧**:
同时打开2个文件: 可以使用2个`with open() as ...:`嵌套;
读取文件4种方法:

- read(全部读取)
- readline(读一行)
- readlines(把文件每一行都作为list的一个元素)
- for循环

```python
with open(file1) as f1_obj:
    with open(file2) as f2_obj:
        for line in f1_obj:
            f2_obj.write(line)
```

读取linux的位置参数, 使用`sys.argv[1]` : `sys.argv`返回一个列表, 第0项为源文件名, 第一项为第一个参数.
使用`s.rstrip('\r\n')`来去除行尾的所有`\r` 和 `\n` 的组合. (如: `\n\r` `\r\n\n\n`...)

### 进度条动画

1. 屏幕上打印20个#
2. @从#中穿过去
3. 如此往复

