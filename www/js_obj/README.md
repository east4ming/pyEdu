# JS 对象

## JS 对象 
JavaScript 中的所有事物都是对象：字符串、数值、数组、函数...
此外，JavaScript 允许自定义对象。

### JS对象

 JavaScript 提供多个内建对象，比如 String、Date、Array 等等。
对象只是带有**属性**和**方法**的特殊数据类型。

### 访问对象的属性

**属性是与对象相关的值。**访问对象属性的语法是：
`objectName.propertyName`

```javascript
var message="Hello World!";
var x=message.length;
```

### 访问对象的方法

**方法是能够在对象上执行的动作。**
`objectName.methodName()`

```javascript
var message="Hello world!";
var x=message.toUpperCase();
```

### 创建 JavaScript 对象

通过 JavaScript，您能够定义并创建自己的对象。

创建新对象有两种不同的方法：

1. 定义并创建对象的实例
2. 使用函数来定义对象，然后创建新的对象实例

### 创建直接的实例

这个例子创建了对象的一个新实例，并向其添加了四个属性：

```javascript
person=new Object();
person.firstname="Bill";
person.lastname="Gates";
person.age=56;
person.eyecolor="bule";
```
替代语法（使用对象 literals）：
`person={firstname:"John",lastname:"Doe",age:50,eyecolor:"blue"};`

### 使用对象构造器

本例使用函数来构造对象：

```javascript
function person(firstname,lastname,age,eyecolor)
{
this.firstname=firstname;
this.lastname=lastname;
this.age=age;
this.eyecolor=eyecolor;
}
```

### 创建 JavaScript 对象实例

一旦您有了对象构造器，就可以创建新的对象实例，就像这样：

```javascript
var myFather=new person("Bill","Gates",56,"blue");
var myMother=new person("Steve","Jobs",48,"green");
```

### 把属性添加到 JavaScript 对象

您可以通过为对象赋值，向已有对象添加新属性:
假设 personObj 已存在 - 您可以为其添加这些新属性：firstname、lastname、age 以及 eyecolor：

```javascript
person.firstname="Bill";
person.lastname="Gates";
person.age=56;
person.eyecolor="blue";

x=person.firstname;
```

### 把方法添加到 JavaScript 对象

方法只不过是附加在对象上的函数。在构造器函数内部定义对象的方法：

```javascript
function person(firstname,lastname,age,eyecolor)
{
this.firstname=firstname;
this.lastname=lastname;
this.age=age;
this.eyecolor=eyecolor;

this.changeName=changeName;
function changeName(name)
{
this.lastname=name;
}
}

myMother.changeName("Ballmer");
```

### JavaScript 类

JavaScript 是**面向对象**的语言，但 JavaScript **不使用类**。
在 JavaScript 中，**不会创建类**，也不会通过类来创建对象（就像在其他面向对象的语言中那样）。
JavaScript 基于 **prototype**，而不是基于类的。

### JavaScript for...in 循环

avaScript for...in 语句**循环遍历对象的属性**。

```javascript
for (对象中的变量)
  {
  要执行的代码
  }
  
var person={fname:"Bill",lname:"Gates",age:56};

for (x in person)
  {
  txt=txt + person[x];
  }
```

## JS Number对象

JavaScript 只有一种数字类型。
可以使用也可以不使用小数点来书写数字。

### JavaScript 数字

可以使用也可以不使用小数点来书写数字。

```javascript
var pi=3.14;    // 使用小数点
var x=34;       // 不使用小数点
//极大或极小可以通过科学计数法来写
var y=123e5;    // 12300000
var z=123e-5;   // 0.00123
```

### 所有 JavaScript 数字均为 64 位

JavaScript 不是类型语言。与许多其他编程语言不同，JavaScript 不定义不同类型的数字，比如整数、短、长、浮点等等。
JavaScript 中的所有数字都存储为**根为 10 的 64 位（8 比特），浮点数**。

### 精度

整数（不使用小数点或指数计数法）最多为 15 位。
小数的最大位数是 17，但是浮点运算并不总是 100% 准确：

### 八进制和十六进制

如果前缀为 0，则 JavaScript 会把数值常量解释为八进制数，如果前缀为 0 和 "x"，则解释为十六进制数。

```javascript
var y=0377;
var z=0xFF;
```

> 提示：绝不要在数字前面写零，除非您需要进行八进制转换。

### 数字属性和方法

**属性**:
- MAX VALUE             最大的数
- MIN VALUE             最小的数
- NEGATIVE INFINITIVE   负无穷大, 溢出时返回该值
- POSITIVE INFINITIVE   正无穷大, 溢出时返回该值
- NaN                   非数字值
- prototype             使您有能力向对象添加属性和方法
- constructor           返回对创建此对象的Number函数的引用

**方法:**:
- toExponential()       转换为指数计数法
- toFixed()             转换为字符串, 结果的小数点后有指定位数的数字
- toPrecision()         格式化为指定的长度
- toString()            转换为字符串, 使用指定的基数
- valueOf()             返回一个 Number 对象的基本数字值

## JS 字符串(String)对象

### JS String 对象 实例

> 1. 计算字符串长度 2_js_string_length.html
> 2. 为字符串添加样式 3_js_string_css.html

#### indexOf() 方法

用来定位字符串中某一个指定的字符首次出现的位置

> 4_js_string_indexof.html

#### 替换字符串中的字符 - replace()

> 5_js_string_replace.html

### String对象

![](http://www.w3school.com.cn/jsref/jsref_obj_string.asp)

## JS Date(日期)对象

日期对象用于处理日期和时间。

### JavaScript Date（日期）对象 实例

#### 返回当日的日期和时间

> 6_js_date_now.html

> getTime(): 7_js_date_gettime.html
> 使用`setFullYear()`设置具体的日期: 8_js_date_setfullyear.html
> 使用`toUTCString()`将当日的日期(根据UTC)转换为字符串. 9_js_date_toutcstring.html
> 使用`getDay()`和数组来显示星期, 而不仅仅是数字. 10_js_date_getday.html
> 在网页上显示一个钟表: 11_js_date_clock.html