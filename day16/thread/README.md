# 多线程编程

适合多线程编程的特点:
本质上是异步的, 需要有多个并发任务, 各个事务的运行顺序可以是不确定的/随机的/不可预测的.
这样的编程任务可以被分成多个执行流, 每个流都有一个要完成的目标.
根据应用的不同, 这些子任务可能都要计算出一个中间结果, 用于合并得到最后的结果.

举例:

- UserRequestThread: 负责读取客户的输入, 可能是一个I/O信道. 程序可能创建多个线程, 每个客户一个, 请求会被放入到队列中
- RequestProcessor: 一个负责从队列中获取并处理请求的线程, 它为下面的线程提供输出
- ReplyThread: 负责把用户的输出取出来并发送出去.

I/O密集型的Python程序比计算密集型的程序更能充分利用多线程的好处.
即:

- **多线程** : **I/O密集型**
- **多进程** : **计算密集型**

## 线程和全局解释器锁

### 退出线程

- `thread.exit()`
- `sys.exit()` 或 抛出`SystemExit`异常

### 一个线程的情况

> 见*one_thread.py*

## python的threading模块

python提供了几个用于多线程编程的模块, 包括thread/threading/Queue等.

- _thread 模块提供了基本的线程和锁的支持;
- threading提供了更高级别, 功能更强的线程管理功能
- Queue模块允许用户创建一个可以用于多个线程之间共享数据的队列数据结构

> 关于**并发执行**的模块, 包括:
> 17.1. threading — Thread-based parallelism
> 17.2. multiprocessing - 基于进程的并行性
> 17.3. concurrent
> 17.4. concurrent.futures - 启动并行任务
> 17.5. subprocess —— 子进程管理
> 17.6. sched - 事件调度程序
> 17.7. queue - 同步队列类
> 17.8. dummy_threading - threading模块的插入替换
> 17.9. _thread - 低级线程API
> 17.10. _dummy_thread - 替换_thread模块

## _thread 模块

功能:

- 产生线程
- 基本的同步数据结构对象(lock project, 也叫原语锁, 简单锁, 互斥锁, 二值信号量)

函数:

- `start_new_thread(func, args, kwargs)`  产生一个新线程
- `allocate_lock()` 分配一个LockType类型的锁对象
- `exit()` 让线程退出

LockType 类型锁对象方法:

- `acquire(wait=None)` 尝试获取锁对象
- `locked()` 如果获取了锁对象返回True, 否则返回False
- `release()` 释放锁

> 见*mt_sleep1.py*

用sleep()来做线程的同步操作并不可靠. 而且如果循环的执行时间不能事先确定的话, 那该怎么办? 这可能会造成主线程过早或过晚退出.
这就是锁的用武之地了. 下面, 我们引入锁的概念.

> 见*mt_sleep2.py*

## threading模块

threading不仅提供了Thread类, 还提供了各种非常好用的同步机制.

**threading模块对象**:

- Thread: 表示一个线程的执行的对象
- Lock: 锁原语对象(跟 _thread 模块里的锁对象相同)
- RLock: 可重入锁对象. 使单线程可以再次获得已经获得的锁(递归锁定)
- Condition: 条件变量对象. 能让一个线程停下来, 等待其他线程满足了某个"条件". 如, 状态的改变或值的改变
- Event: 通用的条件变量. 多个线程可以等待某个事件的发生, 在事件发生后, 所有的线程都会被激活.
- Semaphore: 为等待锁的线程提供一个类似"等候室"的结构
- BoundedSemaphore: 与Semaphore类似, 只是它不允许超过初始值
- Timer: 与Thread相似, 只是它要等待一段时间后才开始运行.

> 另一个避免使用 thread 模块的原因是, 它不支持守护线程.
> 当主线程退出时, 所有的子线程不论它们是否还在工作, 都会被强制退出. 为了避免这种情况引入了守护线程的概念.
> Threading模块支持守护线程. 工作模式如下:
> 守护线程一般时一个等待客户请求服务器, 如果没有客户提出请求, 它就在那等着.
> 如果你设定一个线程为守护线程, 就表示你在说这个线程**不重要**, 在进程退出的时候, 不用等待这个线程退出.
> 如果主线程要退出, 不用等待那些子线程完成, 那就设定这些线程的deamon属性. 即, 在线程开始(调用 thread.start())之前,
> 调用 `setDaemon()`函数设定线程的 daemon标志(thread.setDaemon(True)). 就表示这个线程"不重要"
> 如果要等待子线程完成再退出, 那就什么都不用做.
> 可以调用 thread.isDaemon()函数来判断其daemon标志的值. 新的子线程会继承其父线程的daemon标志.
> 整个Python会在所有的非守护线程退出后才会结束, 即进程中没有非守护线程存在的时候才结束.

### Thread 类

Thread类时主要的运行对象. 用Thread类可以有多种方法来创建线程. 如下: (一般使用最后一个):

- 创建一个Thread实例, 传给它一个**函数**
- 创建一个Thread实例, 传给它一个**可调用的类对象**
- 从Thread派生出一个子类, 创建一个这个子类的实例

Thread的函数:

- start(): 开始线程的执行
- run(): 定义线程的功能的函数(一般会被子类重写)
- join(timeout=None): 程序挂起, 直到线程结束; 如果给了timeout, 则最多阻塞timeout秒
- getName(): 返回线程的名字
- setName(name): 设置线程的名字
- isAlive(): 布尔标志, 表示这个线程是否还在运行中
- isDeamon(): 返回线程的 daemon标志
- setDaemon(daemonic): 把线程的 daemon标志设为 daemonic(一定要在调用start()函数前调用)

传入函数的实例见: *mt_sleep3.py*

传入可调用的类对象的示例见: *mt_sleep4.py*

从Thread派生一个子类, 创建一个这个子类的实例. 示例: *mt_sleep5.py*

### 斐波那契 阶乘和累加和

*mt_facfib.py* 比较了递归求斐波那契/阶乘和累加和函数的运行. 脚本现在**单线程**中运行这三个函数, 然后在多线程中做同样的事情, 以说明多线程的好处.

> 会调用*my_thread.py*

### threading 模块中的其他函数

- activeCount(): 当前活动的线程对象的数量
- currentThread(): 返回当前线程对象
- enumerate(): 返回当前活动线程的列表
- settrace(func): 为所有线程设置一个跟踪函数
- setprofile(func): 为所有线程设置一个profile函数

### 生产者 - 消费者问题和Queue模块

Queue模块可以用来进行线程间通讯, 让各个线程之间共享数据.
现在, 创建一个队列, 让生产者(线程)把新生产的货物放进去供消费者(线程)使用.

**queue模块函数**:

- queue(size): 创建一个大小为size的Queue对象

**queue对象函数**:

- qsize(): 返回队列的大小(由于在返回的时候, 队列可能会被其他线程修改, 所以这个值时近似值)
- empty(): 如果队列为空返回True, 否则返回False
- full(): 如果队列满返回True, 否则返回False
- put(item, block=0): 把item放到队列中, 如果给了block(不为0), 函数会一直阻塞到队列中有空间为止.
- get(block=0): 从队列中取一个对象, 如果给了block(不为0), 函数会一直阻塞到队列中有对象为止.

> 见*prod_cons.py*
