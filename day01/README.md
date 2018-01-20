# Day01

> 老师: 张志刚

## python3

- [官方站点](https://www.python.org)
- 截至目前: 
    - 3.6.4(教学使用3.6)
    - 2.7.14
- Python是c语言写的. 需要c语言的编译器
- 源码安装
    ```shell
    ./configure --prefix=/usr/local
    make && make install
    ```

### 安装

1. 下载老师提供的脚本, 解压缩
2. `bash setup.sh`

### IDE

[pycharm](https://www.jetbrains.com/pycharm/)
 
## 运行python程序

1. 运行解释器, 交互执行指令
2. 明确指定用python3执行文件
3. 为程序文件加执行权限
    ```python
    #!/usr/bin/env python
    #!/usr/local/bin/python3
    ```

## 基本输入输出

```python
print('hello world')
print('hello', 'world')
print('hello', 'world', sep='***')
print('hello' + 'world')
print('hello', 'world', sep='')
print('hello', 'world', end='')
```

### 输入

```python
name = input('prompt: ')
```

> 输入的全部都是**字符串**