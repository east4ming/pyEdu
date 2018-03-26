# day14

## 类的特殊方法

### 类方法

使用 classmethod 方法装饰;
第一个参数为: cls

### 静态方法

staticmethod 装饰
没有self, 没有cls. 与类的关系不大.

- **需要实例化，就普通方法；**
- **不需要类实例化，但是会用到类，就用类方法；**
- **如果跟类完全没关系，就用静态方法。**

### 魔法方法

#### __init__ 构造器

#### __str__ 

#### __call__

### 私有性

## Socket

### TCP Server

1. 创建server的socket
2. 绑定该socket到server的IP+端口
3. 监听
4. 接受连接 `accept()`, 返回 connection和客户端地址
5. 收发数据 `connection.recv(1024)`  `connection.sendall()`
6. 关闭连接 `connection.close()`

> 示例:
> 我自己编写的OOP实现的tcp echo server: *tcp_echo_server.py*
> 文档示例: *socket_echo_server.py*

#### 选择监听地址

将服务器绑定到正确的地址非常重要，以便客户端可以与它进行通信。
前面的例子全部用作 'localhost'IP地址，这限制了与运行在同一台服务器上的客户端的连接。
使用服务器的公共地址，例如返回的值gethostname()，以允许其他主机连接。本示例修改回显服务器以侦听通过命令行参数指定的地址。

> 见*socket_echo_server_explicit.py*
> 客户端做对应修改, 见*socket_echo_client_explicit.py*

### TCP Client

1. 创建client的socket
2. 连接到server, `client_socket.connect(server_addr)`
3. 收发数据: `client_socket.recv(1024)` `client_socket.sendall()`
4. 关闭client的socket.

> 示例:
> 我自己编写的OOP实现的tcp echo client: *tcp_echo_client.py*
> 文档示例: *socket_echo_client.py*

#### 简易客户端连接

把前2步合为一步.
Connect to a **TCP** service listening on the Internet address (a 2-tuple (host, port)),
and return the socket object.
```python
# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))
```

### UDP服务端

用户数据报协议（UDP）与TCP/IP的工作方式不同。

- TCP是面向流的协议，确保所有数据以正确的顺序传输，
- UDP是面向消息的协议。UDP不需要长时间的连接，因此设置UDP套接字更简单一些。

另一方面，UDP消息只能处理单个数据报（对于IPv4，这意味着它们只能保存65,507字节，因为65,535字节的数据包中也包含标题信息），并且不保证与TCP一样的可靠性。
由于没有连接，服务器本身不需要监听(listen)和接受(accept)连接。它只需要使用bind()将其套接字与端口相关联，然后等待单个消息。
从套接字中使用`recvfrom()`读取消息，该消息返回**数据**以及发送它的**客户端的地址**。

> 示例:
> 自己编写: *udp_echo_server.py*
> 文档案例: *socket_echo_server_dgram.py*

### UDP客户端

UDP 回声客户端与服务器类似，但不用 `bind()`将其套接字附加到地址。它用 `sendto()`直接将消息传递给服务器，并用`recvfrom()`接收响应。

> 示例:
> 自己编写: *udp_echo_client.py*
> 文档案例: *socket_echo_client_dgram.py*

### Unix 域套接字

从程序员的角度来看，使用Unix域套接字和TCP/IP套接字有两个本质区别。

- 首先，套接字的地址是**文件系统上的路径**，而不是包含服务器名称和端口的元组。
- 其次，在套接字关闭之后，在文件系统中创建的代表套接字的节点仍然存在，并且每次启动服务器时都需要将其删除。

#### unix 服务器
以前的回声服务器示例可以通过在设置部分进行一些更改来更新以使用。
在socket地址族创建的 AF_UNIX。绑定套接字并管理传入连接的方式与TCP/IP套接字相同。

> 示例:
> 文档示例: *socket_echo_server_uds.py*

#### Unix 客户端

> 见*socket_echo_client_uds.py*

#### 权限

由于UDS套接字由文件系统上的节点表示，因此可以使用标准文件系统权限来控制对服务器的访问。

#### 父子进程之间的通信

`socketpair()`功能对于在Unix下设置用于进程间通信的UDS套接字非常有用。
它创建了一对连接的套接字，可以在fork子进程后用于在父进程和子进程之间进行通信。

> 见*socket_socketpair.py*
