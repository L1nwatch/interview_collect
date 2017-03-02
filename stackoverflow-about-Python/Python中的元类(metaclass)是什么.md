## Python中的元类(metaclass)是什么?

Python 中类的概念，借鉴于 Smalltalk

在大多数语言中，类就是一组用来描述如何生成一个对象的代码段。但是，在 Python 中，类也是对象。

每当你用到关键字 `class`，Python 就会执行它并且建立一个对象：

```python
>>> class ObjectCreator(object):
...       pass
```

上面代码在内存里创建了名叫 ObjectCreator 的对象

这个对象（类）有生成另一个对象（实例）的能力，而且由于它是对象，所以：

*   可以把它赋值给一个变量
*   可以赋值它
*   可以给它加属性
*   可以作为函数参数来传递它
*   ...

```python
>>> print(ObjectCreator) # 你可以打印一个类,因为它是一个对象
<class '__main__.ObjectCreator'>
>>> def echo(o):
...       print(o)
...
>>> echo(ObjectCreator) # 你可以把类作为参数传递
<class '__main__.ObjectCreator'>
>>> print(hasattr(ObjectCreator, 'new_attribute'))
False
>>> ObjectCreator.new_attribute = 'foo' # 可以给一个类添加属性
>>> print(hasattr(ObjectCreator, 'new_attribute'))
True
>>> print(ObjectCreator.new_attribute)
foo
>>> ObjectCreatorMirror = ObjectCreator # 可以把类赋值给一个变量
>>> print(ObjectCreatorMirror.new_attribute)
foo
>>> print(ObjectCreatorMirror())
<__main__.ObjectCreator object at 0x8997b4c>
```

### 动态创建类

因为类也是对象，所以可以在运行时动态创建它们。比如在函数中创建：

```python
>>> def choose_class(name):
...     if name == 'foo':
...         class Foo(object):
...             pass
...         return Foo # 返回一个类不是一个实例
...     else:
...         class Bar(object):
...             pass
...         return Bar
...
>>> MyClass = choose_class('foo')
>>> print(MyClass) # 返回一个类不是一个实例
<class '__main__.Foo'>
>>> print(MyClass()) # 你可以在类里创建一个对象
<__main__.Foo object at 0x89c6d4c>
```

但这还不够动态，因为仍然需要编写整个类的代码。

既然类是对象，那么肯定有什么东西来生成它，答案是 `type` 关键字。

`type` 可以接受一个类的描述作为参数，然后返回一个类。

```python
type(类名,
     父类名的元组 (针对继承情况,可以为空),
     包含属性的字典(名称和值))
```

比如，以下两种方式是等价的：

```python
>>> class MyShinyClass(object):
...       bar = True
# 以下与以上等价
>>> MyShinyClass = type('MyShinyClass', (), {"bar":True}) # 返回类对象
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # 创建一个类的实例
<__main__.MyShinyClass object at 0x8997cec>
```

 继承的方式：

```python
>>>   class FooChild(Foo):
...         pass
# 以上以下等价
>>> FooChild = type('FooChild', (Foo,), {})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar) # bar从Foo继承
True
```

要是在类中添加方法，要做的就是把函数名写入字典就可以了：

```python
>>> def echo_bar(self):
...       print(self.bar)
...
>>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
>>> hasattr(Foo, 'echo_bar')
False
>>> hasattr(FooChild, 'echo_bar')
True
```

### 元类

元类就是创建类的东西，既然类是对象，元类就是类的类，即：

```python
MyClass = MetaClass()
MyObject = MyClass()
```

而 `type` 就是一个元类，`type` 是 Python 中创建所有类的元类。

可以通过检查 `__class__` 属性看到：

```python
>>> age.__class__
<type 'int'>
>>> name.__class__
<type 'str'>
>>> foo.__class__
<type 'function'>
>>> b.__class__
<class '__main__.Bar'>
>>> age.__class__.__class__
<type 'type'>
>>> name.__class__.__class__
<type 'type'>
>>> foo.__class__.__class__
<type 'type'>
>>> b.__class__.__class__
<type 'type'>
```

`type` 是 Python 的內建元类，然后你也可以创建自己的元类

### `__metaclass__` 属性

可以添加 `__metaclass__` 属性，如果你这么做了，Python 就会用元类来创建类 Foo：

```python
class Foo(object):
  __metaclass__ = something...
  [...]
```

这里写下 `class Foo(object)`，但是类对象 Foo 还没有在内存中创建。Python 将会在类定义中寻找 `__metaclass__`，如果找到了就用它来创建类对象 Foo，找不到（会往父类接着找、然后到模块层次去找），都找不到则用默认的 `type`

那么可以在 `__metaclass__` 中放置什么东西？答案是，可以创建一个类的东西。比如 `type`，或者任何使用到 `type` 或者子类化 `type` 等都可以

### 自定义元类

元类的主要目的就是为了当创建类时能够自动地改变类，通常会为 API 做这样的事情，因为希望可以创建符合当前上下文的类。

比如说希望你的模块里所有的类的属性都应该是大写形式，其中一种实现方法就是在模块级别设定 `__metaclass__`

另外，`__metaclass__` 实际上可以被任意调用，并不需要是一个正式的类

```python
# 元类会自动将你通常传给'type'的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    返回一个将属性列表变为大写字母的类对象
  """

  # 选取所有不以'__'开头的属性,并把它们编程大写
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # 用'type'创建类
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # 将会影响整个模块

class Foo(): # global __metaclass__ won't work with "object" though
  # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
  bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出: True

f = Foo()
print(f.BAR)
# 输出: 'bip'
```

以下重新实现一遍，用类的方法来弄：

```python
# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
class UpperAttrMetaclass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回它的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)
```

这不是真正的面向对象（OOP），因为我们直接调用了 type，没有改写父类的 `__new__` 方法。

正确的方式应该这样处理：

```python
class UpperAttrMetaclass(type):

    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # 重用 type.__new__ 方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, uppercase_attr)
```

注意到有个额外的参数 `upperattr_metaclass`，类方法的第一个参数总是表示当前的实例，类似于 self，这里的名字应该改为 `cls` 比较符合标准一些

另外，如果使用 `super` 方法的话，会更清晰一些而且还会缓解继承：

```python
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)
```

就元类本身而言，其实是很简单的：

*   拦截类的创建
*   修改一个类
*   返回修改之后的类

### 为什么要使用 metaclass 类而不是函数？

由于 `__metaclass__` 可以接受任何可调用的对象，为何还要使用类？

*   意图可以更加清晰
*   可以使用 OOP 编程，元类可以从元类中继承而来，改写父类的方法。元类甚至还可以使用元类
*   可以把代码组织得更好，将多个方法归总到一个类中会很有帮助
*   可以使用 `__new__`、`__init__`、`__call__` 等特殊方法

### 为什么要使用元类？

一般来说，根本就用不上它。

元类的主要用途是创建 API，比如 Django ORM，比如

```python
class Person(models.Model):
  name = models.CharField(max_length=30)
  age = models.IntegerField()
```

但是如果你这样做：

```python
guy = Person(name='bob', age='35')
print(guy.age)
```

这并不会返回一个 `InterField` 对象，而是会返回一个 int，甚至可以直接从数据库中取出数据。

这是有可能的，因为 `models.Model` 定义了一个 `__metaclass__`，使用了一些魔法方法能够将你刚刚定义的简单类转变成对数据库的一个复杂 hook

### 结语

Python 中的一切都是对象，要么是类的实例，要么是元类的实例。

除了 `type`，它实际上是自己的元类，在纯 Python 环境中难以实现，需要在实现层面中用一些特殊手段做到。

对于非常简单的类，可以通过其他技术来修改，比如：

*   monkey patching
*   装饰器

当你需要动态修改类时，最好使用上面这两种技术