# JS HTML DOM

**通过 HTML DOM，可访问 JavaScript HTML 文档的所有元素。**

## 简介

### HTML DOM (文档对象模型)

当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）
HTML DOM 模型被构造为对象的树。

### HTML DOM 树

![](http://www.w3school.com.cn/i/ct_htmltree.gif)

通过可编程的对象模型，JavaScript 获得了足够的能力来创建动态的 HTML。

- JavaScript 能够改变页面中的所有 HTML **元素**
- JavaScript 能够改变页面中的所有 HTML **属性**
- JavaScript 能够改变页面中的所有 **CSS** 样式
- JavaScript 能够对页面中的所有**事件**做出反应

### 查找HTML元素

通常，通过 JavaScript，您需要操作 HTML 元素。
为了做到这件事情，您必须首先找到该元素。有三种方法来做这件事：

- 通过 id 找到 HTML 元素
- 通过标签名找到 HTML 元素
- 通过类名找到 HTML 元素

### 通过 id 查找 HTML 元素

在 DOM 中查找 HTML 元素的最简单的方法，是通过使用元素的 id。

> 实例*1_get_by_id.html*

如果找到该元素，则该方法将以**对象**（在 x 中）的形式返回该元素。
如果未找到该元素，则 x 将包含 null。

### 通过标签名查找 HTML 元素

> *2_get_by_tagname.html*

> 提示：通过类名查找 HTML 元素在 IE 5,6,7,8 中无效。

## JavaScript HTML DOM - 改变 HTML

HTML DOM 允许 JavaScript 改变 HTML 元素的内容。

### 改变 HTML 输出流

JavaScript 能够创建动态的 HTML 内容：
今天的日期是： *Tue May 15 2018 21:48:27 GMT+0800 (CST)*
在 JavaScript 中，`document.write()` 可用于直接向 HTML 输出流写内容。

> 见*3_date.html*

> 提示：绝不要使用在文档加载之后使用 document.write()。这会覆盖该文档。

### 改变 HTML 内容

修改 HTML 内容的最简单的方法时使用 innerHTML 属性。
如需改变 HTML 元素的内容，请使用这个语法：`document.getElementById(id).innerHTML=new HTML`

> *4_innerHTML.html*

### 改变 HTML 属性

如需改变 HTML 元素的属性，请使用这个语法：
`document.getElementById(id).attribute=new value`

> *5_change_attr.html*

## JavaScript HTML DOM - 改变 CSS

HTML DOM 允许 JavaScript 改变 HTML 元素的样式。

### 改变 HTML 样式

如需改变 HTML 元素的样式，请使用这个语法：
`document.getElementById(id).style.property=new style`

> *6_change_css_color.html*
> *7_change_onclick.html*
> *8_hide_text.html*

**[HTML DOM Style 对象参考手册](http://www.w3school.com.cn/jsref/dom_obj_style.asp)**

## JavaScript HTML DOM 事件

HTML DOM 使 JavaScript 有能力对 HTML 事件做出反应。

### 对事件做出反应

我们可以在事件发生时执行 JavaScript，比如当用户在 HTML 元素上点击时。
如需在用户点击某个元素时执行代码，请向一个 HTML 事件属性添加 JavaScript 代码：
`onclick=JavaScript`

HTML 事件的例子：

- 当用户点击鼠标时
- 当网页已加载时
- 当图像已加载时
- 当鼠标移动到元素上时
- 当输入字段被改变时
- 当提交 HTML 表单时
- 当用户触发按键时

> *9_onclick.html*
> *10_onclick_func.html*

### HTML 事件属性

如需向 HTML 元素分配 事件，您可以使用事件属性。

> *11_button_onclick.html*

### 使用 HTML DOM 来分配事件

HTML DOM 允许您通过使用 JavaScript 来向 HTML 元素分配事件：

> *12_button_onclick.html*

### onload 和 onunload 事件

onload 和 onunload 事件会在用户进入或离开页面时被触发。
onload 事件可用于检测访问者的**浏览器类型**和**浏览器版本**，并基于这些信息来加载网页的正确版本。
onload 和 onunload 事件可用于处理 **cookie**。

> *13_checkCookie.html*

### onchange 事件

onchange 事件常结合对输入字段的验证来使用。
下面是一个如何使用 onchange 的例子。
当用户改变输入字段的内容时，会调用 `upperCase()` 函数。

> *14_upperCase_onchange.html*

### onmouseover 和 onmouseout 事件

onmouseover 和 onmouseout 事件可用于在用户的鼠标移至 HTML 元素上方或移出元素时触发函数。

> 15_onmouseover.html

### onmousedown、onmouseup 以及 onclick 事件

onmousedown, onmouseup 以及 onclick 构成了鼠标点击事件的所有部分。
首先当点击鼠标按钮时，会触发 onmousedown 事件，当释放鼠标按钮时，会触发 onmouseup 事件，
最后，当完成鼠标点击时，会触发 onclick 事件。

> 16_onmousedown.html
> 17_lighton.html
> 18_onload.html
> 19_onfocus.html
> 20_change_color_onmouseover.html

## JavaScript HTML DOM 元素（节点）

添加和删除节点（HTML 元素）。

### 创建新的 HTML 元素

如需向 HTML DOM 添加新元素，您必须首先创建该元素（元素节点），然后向一个已存在的元素追加该元素。

> 21_appendChild.html

### 删除已有的 HTML 元素

如需删除 HTML 元素，您必须首先获得该元素的父元素：

> 22_removeChild.html
> 提示：如果能够在不引用父元素的情况下删除某个元素，就太好了。
>   不过很遗憾。DOM 需要清楚您需要删除的元素，以及它的父元素。
>   这是常用的解决方案：找到您希望删除的子元素，然后使用其 parentNode 属性来找到父元素：
> ```javascript
>  var child=document.getElementById("p1");
>  child.parentNode.removeChild(child);
>  ```
