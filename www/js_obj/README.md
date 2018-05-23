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

### 定义日期

Date 对象用于处理日期和时间。
可以通过 new 关键词来定义 Date 对象。以下代码定义了名为 myDate 的 Date 对象：
`var myDate=new Date() `

> 注释：Date 对象自动使用当前的日期和时间作为其初始值。

### 操作日期

```javascript
var myDate=new Date();
myDate.setFullYear(2008,7,9)
```

> 注意：表示月份的参数介于 0 到 11 之间。也就是说，如果希望把月设置为 8 月，则参数应该是 7。

在下面的例子中，我们将日期对象设置为 5 天后的日期：

```javascript
var myDate=new Date();
myDate.setDate(myDate.getDate()+5)
```

> 注意：如果增加天数会改变月份或者年份，那么日期对象会自动完成这种转换。

### 比较日期

日期对象也可用于比较两个日期。
下面的代码将当前日期与 2008 年 8 月 9 日做了比较：

```javascript
var myDate=new Date();
myDate.setFullYear(2008,8,9);

var today=new Date();

if (myDate>today)
    {
        alert("Today is before 2008/9/9");
    }
else {
    alert("Today is after 2008/9/9");
}
```

## JavaScript Array（数组）对象

**数组对象的作用是：使用单独的变量名来存储一系列的值。**

### 实例

> 创建数组: 12_js_array_create.html
> For...in声明: 13_js_array_forin.html
> 合并2个数组: 14_js_array_concat.html
> 用数组的元素组成字符串: 15_js_array_join.html
> 对数组进行字面上的排序: 16_js_array_sort.html
> 对数组进行数值上的排序: 17_js_array_sort.html

> ![Array对象参考手册](http://www.w3school.com.cn/jsref/jsref_obj_array.asp)

### 定义数组

`var myArray=new Array();`
有两种向数组赋值的方法（你可以添加任意多的值，就像你可以定义你需要的任意多的变量一样）。
```javascript
var mycars=new Array()
mycars[0]="Saab"
mycars[1]="Volvo"
mycars[2]="BMW"
//也可以使用一个整数自变量来控制数组的容量：
var mycars=new Array(3)
mycars[0]="Saab"
mycars[1]="Volvo"
mycars[2]="BMW"
//另一种赋值的方法
var mycars=new Array("Saab","Volvo","BMW")
```

> 注意：如果你需要在数组内指定数值或者逻辑值，那么变量类型应该是数值变量或者布尔变量，而不是字符变量

### 访问数组中的值

通过下标访问`myCar[0]`

### 修改已有数组中的值

通过下标修改`myCar[0]=""Opel"`

## JavaScript Boolean（逻辑）对象

Boolean（逻辑）对象用于将非逻辑值转换为逻辑值（true 或者 false）。

- 0 是逻辑的 false
- 1 是逻辑的 true
- 空字符串是逻辑的 false
- null 是逻辑的 false
- NaN 是逻辑的 false
- 字符串 'false' 是逻辑的 true

> ![Boolean对象](http://www.w3school.com.cn/jsref/jsref_obj_boolean.asp)

### 创建 Boolean 对象

`var myBoolean=new Boolean()`

> 注释：如果逻辑对象无初始值或者其值为 0、-0、null、""、false、undefined 或者 NaN，
> 那么对象的值为 false。否则，其值为 true（即使当自变量为字符串 "false" 时）！

下面的所有的代码行均会创建初始值为 false 的 Boolean 对象。

```javascript
var myBoolean=new Boolean();
var myBoolean=new Boolean(0);
var myBoolean=new Boolean(null);
var myBoolean=new Boolean("");
var myBoolean=new Boolean(false);
var myBoolean=new Boolean(NaN);
```

下面的所有的代码行均会创初始值为 true 的 Boolean 对象

```javascript
var myBoolean=new Boolean(1);
var myBoolean=new Boolean(true);
var myBoolean=new Boolean("true");
var myBoolean=new Boolean("false");
var myBoolean=new Boolean("Bill Gates");
```

## JavaScript Math（算数）对象

Math（算数）对象的作用是：执行常见的算数任务。

### 实例 

> round() : 18_js_math_round.html
> `random()`: 19_js_math_random.html
> `max()`: 20_js_math_max.html

> ![JavaScript Math 对象](http://www.w3school.com.cn/jsref/jsref_obj_math.asp)

### Math对象

Math 对象提供多种算数值类型和函数。无需在使用这个对象之前对它进行定义。

### 算数值

JavaScript 提供 8 种可被 Math 对象访问的算数值：

- 常数
- 圆周率
- 2 的平方根
- 1/2 的平方根
- 2 的自然对数
- 10 的自然对数
- 以 2 为底的 e 的对数
- 以 10 为底的 e 的对数

这是在 Javascript 中使用这些值的方法：（与上面的算数值一一对应）

- Math.E
- Math.PI
- Math.SQRT2
- Math.SQRT1_2
- Math.LN2
- Math.LN10
- Math.LOG2E
- Math.LOG10E

## JavaScript RegExp 对象

**RegExp 对象用于规定在文本中检索的内容。**

### 定义 RegExp

RegExp 对象用于存储检索模式。
通过 new 关键词来定义 RegExp 对象。
以下代码定义了名为 patt1 的 RegExp 对象，其模式是 "e"：
`var patt1=new RegExp("e");`
当您使用该 RegExp 对象在一个字符串中检索时，将寻找的是字符 "e"。

### RegExp 对象的方法
RegExp 对象有 3 个方法：test()、exec() 以及 compile()。

### test()
`test()` 方法检索字符串中的指定值。返回值是 true 或 false。

```javascript
var patt1=new RegExp("e");

document.write(patt1.test("The best things in life are free")); 
```

### exec()

exec() 方法检索字符串中的指定值。返回值是被找到的值。
如果没有发现匹配，则返回 null。

```javascript
var patt1=new RegExp("e");

document.write(patt1.exec("The best things in life are free")); 
//输出为e
```

您可以向 RegExp 对象添加第二个参数，以设定检索。
例如，如果需要找到所有某个字符的所有存在，则可以使用 "g" 参数 ("global")。
如需关于如何修改搜索模式的完整信息，请访问我们的 ![RegExp 对象参考手册](http://www.w3school.com.cn/jsref/jsref_obj_regexp.asp)。
在使用 "g" 参数时，exec() 的工作原理如下：

- 找到第一个 "e"，并存储其位置
- 如果再次运行 exec()，则从存储的位置开始检索，并找到下一个 "e"，并存储其位置

```javascript
var patt1=new RegExp("e","g");
do
{
result=patt1.exec("The best things in life are free");
document.write(result);
}
while (result!=null) 
```

### compile()

compile() 方法用于改变 RegExp。
compile() 既可以改变检索模式，也可以添加或删除第二个参数。

```javascript
var patt1=new RegExp("e");

document.write(patt1.test("The best things in life are free"));

patt1.compile("d");

document.write(patt1.test("The best things in life are free"));
```

