# JavaScript

## JavaScript简介

**JavaScript 是世界上最流行的编程语言。**
**这门语言可用于 HTML 和 web，更可广泛用于服务器、PC、笔记本电脑、平板电脑和智能手机等设备。**

**JavaScript 是脚本语言**
- JavaScript 是一种轻量级的编程语言。
- JavaScript 是可插入 HTML 页面的编程代码。
- JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。
- JavaScript 很容易学习。

### 写入HTML输出

`document.write()` 只能在HTML输出中使用该方法. 如果您在文档加载后使用该方法, 会覆盖整个文档.

### 对事件作出反映

> 见*1_onclick.html*

`alert()`函数在JavaScript 中并不常用, 但它对于代码测试非常方便.
`onclick` 事件是众多事件之一.

### 改变HTML内容

> 见*2_getElementById.html*

`document.getElementByID("some id")` 这个方法是HTML DOM中定义的.
DOM(文档对象模型) 是用以访问HTML元素的W3C 标准.

### 改变HTML图像

> 本例子会动态改变HTML `<image>` 的来源(src)
> *3_light_bulb.html*

### 改变HTML样式

> *4_change_style.html*

### 验证输入

javascript常用于验证用户的输入.

> *5_check_input.html*

> **你知道吗?**
> 提示: JavaScript 与 Java 是两种完全不同的语言, 无论是概念上还是设计上.
> Java(由Sun发明)是更复杂的编程语言
> ECMA-262 是JavaScript 标准的官方名称.
> JavaScript 由 Brendan Eich 发明. 它于1995年出现在Netscape中, 并于1997年被ECMA(一个标准协会)采纳

## JavaScript 使用

**HTML 中的脚本必须位于`<script>`和`</script>`标签之间.**
**脚本可被放置在HTML页面的`<body>`和`<head>`部分中. 但推荐放在`</body>`之前**
把 JavaScript 放到了页面代码的底部，这样就可以确保在 `<p>` 元素创建之后再执行脚本。

> 那些老旧的实例可能会在 <script> 标签中使用 type="text/javascript"。现在已经不必这样做了。JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言。

### 外部的JavaScript

也可以把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码。
外部 JavaScript 文件的文件扩展名是 .js。
如需使用外部文件，请在 <script> 标签的 "src" 属性中设置该 .js 文件：

```html
<!DOCTYPE html>
<html>
<body>
<script src="myScript.js"></script>
</body>
</html>
```

> 提示：外部脚本不能包含 <script> 标签。

## JavaScript 输出

**JavaScript通常用于操作HTML元素**

## JavaScript 语句

### 分号

分号用于分隔 JavaScript 语句。
通常我们在每条可执行的语句结尾添加分号。
使用分号的另一用处是在一行中编写多条语句。
提示：您也可能看到不带有分号的案例。
在 JavaScript 中，用分号来结束语句是可选的(**但建议都加上**)

### JavaScript对大小写敏感

### 对代码行进行折行

在文本字符串中使用反斜杠对代码行进行换行。

```javascript
document.write("Hello \
World!");
```

> **你知道吗?**
> 提示：JavaScript 是脚本语言。浏览器会在读取代码时，逐行地执行脚本代码。

### JavaScript 变量

```javascript
var x=2;
var y=3;
var z=x+y;
var pi=3.14;
var name="Bill Gates";
var answer='Yes I am!';
```

### 声明(创建)JavaScript变量

在 JavaScript 中创建变量通常称为“声明”变量。
我们使用 var 关键词来声明变量：`var carname;`
变量声明之后，该变量是空的（它没有值）。
如需向变量赋值，请使用等号：`carname="Volvo";`
不过，您也可以在声明变量时对其赋值：`var carname="Volvo";`

### 一条语句，多个变量

可以在一条语句中声明很多变量。该语句以 var 开头，并使用**逗号**分隔变量即可：
`var name="Gates", age=56, job="CEO";`

也可以跨多行:
```javascript
var name="Gates",
age=56,
job="CEO";
```

### Value = undefined

在计算机程序中，经常会声明无值的变量。未使用值来声明的变量，其值实际上是 undefined。

### 重新声明 JavaScript 变量

如果重新声明 JavaScript 变量，该变量的值不会丢失

## JavaScript 数据类型

- 字符串
- 数字
- 布尔
- 数组(对应Python的列表list)
- 对象(对应Python的字典dict)
- Null(对应Python的None)
- Undefined

### JavaScript 拥有动态类型

JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型：

```javascript
var x                // x 为 undefined
var x = 6;           // x 为数字
var x = "Bill";      // x 为字符串
```

### JavaScript 数字

JavaScript 只有一种数字类型。数字可以带小数点，也可以不带：

```javascript
var x1=34.00;      //使用小数点来写
var x2=34;         //不使用小数点来写
```

极大或极小的数字可以通过科学（指数）计数法来书写：
```javascript
var y=123e5;      // 12300000
var z=123e-5;     // 0.00123
```

### JavaScript 布尔

布尔（逻辑）只能有两个值：true 或 false。

### JavaScript 数组

```javascript
//方法1
var cars=new Array();
cars[0]="Audi";
cars[1]="BMW";
cars[2]="Volvo";
//方法2
var cars=new Array("Audi","BMW","Volvo");
//方法3: 推荐
var cars=["Audi","BMW","Volvo"];
```

数组下标是基于零的

### JavaScript 对象

对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：

```javascript
var person={firstname:"Bill", lastname:"Gates", id:5566};
var person={
firstname : "Bill",
lastname  : "Gates",
id        :  5566
};
//对象属性有两种寻址方式：
name=person.lastname;
name=person["lastname"];
```

### Undefined 和 Null

Undefined 这个值表示变量不含有值。

可以通过将变量的值设置为 null 来清空变量。

**这两个基本没啥太大区别, 一般就用Null**

### 声明变量类型

当您声明新变量时，可以使用关键词 "new" 来声明其类型：

```javascript
var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```

## JavaScript 对象

**JavaScript 中的所有事物都是对象：字符串、数字、数组、日期，等等。**
在 JavaScript 中，对象是拥有**属性**和**方法**的数据。

### 属性和方法

属性是与对象相关的值。
方法是能够在对象上执行的动作。
举例：汽车就是现实生活中的对象。
汽车的属性：

```javascript
car.name=Fiat
car.model=500
car.weight=850kg
car.color=white 
```

汽车的方法:
```javascript
car.start()
car.drive()
car.brake()
```

### JavaScript 中的对象

```javascript
var txt = "Hello";
/*
实际上已经创建了一个 JavaScript 字符串对象。字符串对象拥有内建的属性 length。
对于上面的字符串来说，length 的值是 5。字符串对象同时拥有若干个内建的方法。
 */
txt.length=5
txt.indexOf()
txt.replace()
txt.search()
```

### 创建JavaScript对象

JavaScript 中的几乎所有事务都是对象：字符串、数字、数组、日期、函数，等等。
你也可以创建自己的对象。
本例创建名为 "person" 的对象，并为其添加了四个属性：

```javascript
person=new Object();
person.firstname="Bill";
person.lastname="Gates";
person.age=56;
person.eyecolor="blue";
```

### 访问对象的属性

访问对象属性的语法是：`objectName.propertyName`

### 访问对象的方法

您可以通过下面的语法调用方法：`objectName.methodName()`

> 使用 camel-case 标记法的函数是很常见的。您会经常看到 someMethod() 这样的函数名

# TODO: 函数

http://www.w3school.com.cn/js/js_functions.asp