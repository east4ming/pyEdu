# AJAX

## AJAX

AJAX = Asynchronous JavaScript and XML（异步的 JavaScript 和 XML）。

AJAX 不是新的编程语言，而是一种使用现有标准的新方法。

AJAX 是与服务器交换数据并更新部分网页的艺术，在不重新加载整个页面的情况下。

## AJAX 简介

**AJAX 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。**

### 什么是 AJAX ？

AJAX = 异步 JavaScript 和 XML。

AJAX 是一种用于创建快速动态网页的技术。

通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

传统的网页（不使用 AJAX）如果需要更新内容，必需重载整个网页面。

有很多使用 AJAX 的应用程序案例：新浪微博、Google 地图、开心网等等。

## AJAX - 创建 XMLHttpRequest 对象

**XMLHttpRequest 是 AJAX 的基础。**

### XMLHttpRequest 对象

所有现代浏览器均支持 XMLHttpRequest 对象（IE5 和 IE6 使用 ActiveXObject）。
XMLHttpRequest 用于在后台与服务器交换数据。
这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

### 创建 XMLHttpRequest 对象

所有现代浏览器（IE7+、Firefox、Chrome、Safari 以及 Opera）均内建 XMLHttpRequest 对象。

#### 创建 XMLHttpRequest 对象的语法：

`variable=new XMLHttpRequest();`

#### 老版本的 Internet Explorer （IE5 和 IE6）使用 ActiveX 对象：

`variable=new ActiveXObject("Microsoft.XMLHTTP");`

为了应对所有的现代浏览器，包括 IE5 和 IE6，请检查浏览器是否支持 XMLHttpRequest 对象。
如果支持，则创建 XMLHttpRequest 对象。如果不支持，则创建 ActiveXObject ：
```javascript
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
```

## AJAX - 向服务器发送请求

XMLHttpRequest 对象用于和服务器交换数据。

**向服务器发送请求**
如需将请求发送到服务器，我们使用 XMLHttpRequest 对象的 open() 和 send() 方法：

```javascript
//open(method,url,async)
xmlhttp.open("GET","test1.txt",true);
xmlhttp.send();
```

### GET 还是 POST？

与 POST 相比，GET 更简单也更快，并且在大部分情况下都能用。

然而，在以下情况中，请使用 POST 请求：

- 无法使用缓存文件（更新服务器上的文件或数据库）
- 向服务器发送大量数据（POST 没有数据量限制）
- 发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠

### GET 请求

```javascript
xmlhttp.open("GET","demo_get.asp",true);
xmlhttp.send();
```

> 1_ajax_get.html