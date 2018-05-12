# javascript

```javascript
var a=1;
a='abc';
b=1;

function print() {
  var a=1;
}
alert(a);
```

## html中js放在哪儿

- html种任何位置都可以写js
- 一般js放在`</body>`的前面(
    - 更好方便操作变量
    - js有时候会较大, 如果放在head里会导致页面加载缓慢
    
## 运行时机

- 立即运行
- 事件触发

## javascript-dom 树

- windows: 只有一个, 全局对象, 使用全局方法
- document: 可以有多个, 对应body元素, 是视窗区域
- form: 一个向服务器提供信息的单元
- $element: 任意元素. div tr button

## javascript的document对象

- close()
- getElementById()
- getElementByName()
- open()
- write()
- writeIn()

 