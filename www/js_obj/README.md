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

http://www.w3school.com.cn/js/js_obj_number.asp