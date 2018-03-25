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
