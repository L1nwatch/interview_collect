## 装饰器classmethod和staticmethod的区别

一个对象实体调用方法，隐藏了传递的第一个参数 `self`：

```python
a.foo(1)
```

如果方法是用 `classmethods` 装饰，那么被隐藏的第一个参数是对象的类而不是 `self`：

```python
a.class_foo(1)
```

也可以用类调用，一般被装饰为 `classmethod` 是希望用类来调用，而不是实例来调用

用 `staticmethods` 装饰，不管传递给第一个参数是 `self` 还是 `cls`，表现都一样，静态方法被用来组织类之间有逻辑关系的函数

静态方法就是一个普通方法，一个不带参数绑定的方法

