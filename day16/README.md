# day16

## 练习

### 匹配身份证号

`\d{17}(\d|X|x)`

### 密码

以字母开头, 8-10位, 后跟数字字母下划线

`^[A-Za-z][0-9A-Za-z_]{7,9}$`


### 浮点数

`^-?\d+\.\d+$`

### 分析apache访问日志

1. 统计每个客户端访问apache服务器的次数
2. 将统计信息通过字典的方式显示出来
3. 分别统计客户端是Firefox还是MSIE
4. 使用函数式编程和OOP编程

> 使用 re collections 模块
> collections 模块中提供了许多有用的集合类
> 使用其中的 Counter 类
> Counter 是一个简单的计数器, 以字典的键值对形式储存, 其中搜索的元素作为key, 出现的次数作为值.

## forking 编程

fork 分岔, 一个进程在调用fork时, 产生另一个子进程.
父进程将自身资源拷贝一份, 命令在子进程中运行时, 就具有和父进程完全一样的运行环境.

`os.fork()` 可以实现forking功能.
对于父进程, 返回一个子进程的pid, 对于子进程, 返回0.

父进程通过 os.wait() 来得到子进程是否终止的信息
在子进程终止和父进程调用喔咕wait()之间的这段时间, 子进程被称为 zombie进程.

### forking 服务器

在网络服务器中, forking被广泛应用. 如果服务器需要响应多个请求, 那么就得用forking
父进程负责接受客户端的连接请求
子进程负责处理客户端的请求

## 多线程

- 本质上是异步的, 需要有多个并发任务
- 各个事务的运行顺序可以是不确定的, 随机的, 不可预测的.
- 这样的编程任务可以被分为多个执行流, 每个流都有一个要完成的目标
- 根据应用的不同, 这些子任务可能都要计算出一个中间结果, 用于合并得到最后的结果

# 网路编程

**服务器**: 是一个软件或硬件, 用于向一个或多个客户端(客户)提供所需要的"服务".
服务器不停地处理外来的请求, 而客户一次只能提出一个服务的请求, 等待结果.
先来先服务(first-come-first-served, FCFS)
无论如何, 服务器不会结束工作.

## 套接字

基于网络型的, 基于文件型的.
地址家族(AddressFamily, AF)

- AF_UNIX
- AF_INET  (AF_INET6)

### 面向连接与无连接

**面向连接**: 顺序的, 可靠的, 不会重复的数据传输, 而且不会被加上数据边界.
每个要发送的信息, 可能会被拆为多份, 每一份都会不多不少地正确到达目的地. 然后被重新拼接.
TCP协议 - SOCK_STREAM (流套接字)

**无连接**: 无需建立连接就可通讯. 数据到达的顺序/可靠性及不重复性无法保证. 保留数据边界.
数据是整个发送的. (如邮政) 能某些场合提供更好地性能.
UDP(用户数据报)协议 - SOCK_DGRAM (datagram, 数据报)

`s.accept()` 阻塞式的, 即程序在连接到来之前会处于挂起状态.
一旦接收到一个连接, `accept()`函数就会返回一个单独的**客户端套接字**用于后续的通信. 使用新的客户端套接字就像把
客户的电话转给一个客户服务人员. 当一个客户打电话进来的时候, 总机接了电话, 然后把电话转到合适的人那里来处理客户的请求.
这样就可以空出总机, 也就是最初的那个服务器套接字, 于是, 话务员就可以等待下一个电话(客户端请求), 与此同时, 前一个客户与对应的
客户服务人员在另一条线路上进行着他们之间的对话. 同样的, 当一个请求到来时, 要创建一个新的端口, 然后直接在那个端口上与客户对话,
这样就可以空出主端口来接受其他客户的连接.
创建一个新的**线程或进程**来完成与客户端通讯时一种非常常用的手段.
**SocketServer** 模块时一个基于*socket* 模块的高级别的套接字通讯模块, 它支持在新的线程或进程中处理客户端请求.

> **优雅的退出和调用服务器的 close() 函数**:
> 把服务器的 while 循环放在一个 try-except 语句的try子句当中, 并 except 中捕获 EOFError 和 KeyboardInterrupt异常. 在finally中调用
> close()函数关闭服务器的套接字.

## SocketServer 模块

1. 类: `BaseServer`  概述: 包含服务器的核心功能与混合(mix-in)类挂钩; 这个类只用于派生, 所以不会生成这个类的实例; 可以考虑使用TCPServer和UDPServer
2. `TCPServer/UDPServer` 基本的网络同步TCP/UDP服务器
3. `UnixStreamServer/UnixDatagramServer` 基本的基于文件同步的TCP/UDP服务器
4. `ForkingTCPServer/ForkingUDPServer` ForkingMixIn 和TCPServer/UDPServer的组合
5. `ThreadingTCPServer/ThreadingUDPServer` ThreadingMixIn和TCPServer/UDPServer的组合.
6. `BaseRequestHandler` 包含处理服务请求的核心功能. 这个类只用于派生, 所以不会生成这个类的实例.
7. `StreamRequestHandler/DatagramRequestHandler` 用于TCP/UDP服务器的服务处理工具.

### 创建 SocketServerTCP 服务器

> 见*ts_tserv_ss.py*

### 创建 SocketServerTCP 客户端

> 见*ts_tclnt_ss.py*