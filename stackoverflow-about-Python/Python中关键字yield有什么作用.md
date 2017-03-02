## Python中关键字yield有什么作用?

为了理解 yield 有什么用，首先得理解 generators，再之前还要理解 iterables

### Iterables

可迭代的，比如创建了一个列表，可以一个一个读取它的每一项，这就叫迭代（iteration）：

```python
>>> mylist = [1, 2, 3]
>>> for i in mylist:
...    print(i)
1
2
3
```

可以用在 `for...in...` 语句中的都是可迭代的，但是必须把它们的值放到内存里，当它们有很多值时就会消耗太多的内存

### Generators

生成器，也是迭代器的一种，但是只能迭代一次，因为它们不是全部存在内存里，只在要调用的时候在内存里生成：

```python
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```

生成器和迭代器的区别就是用 `()` 代替 `[]`，还有不能用 `for i in mygenerator` 第二次调用生成器，因为每计算完一个值就会丢弃一个值

### Yield

`yield` 用法和 `return` 差不多，下面的函数将会返回一个生成器：

```python
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # 创建生成器
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

如果函数要返回一个非常大的集合，而你只需要读取一次的话，用这个就很合适了。

这里当你调用函数时，函数里的代码并没有运行，仅仅返回生成器对象。每当 for 语句迭代生成器的时候代码才会运转。

当 `for` 语句第一次调用函数里的生成器对象，函数里的代码就开始运作，直到碰到 `yield`，然后会返回本次循环的第一个返回值。所以下一次调用也将运行一次循环然后返回下一个值，直到没有值可以返回。一旦函数运行没有喷到 yield 语句就认为生成器已经为空了

### 生成器的高级用法：控制迭代器的穷尽

生成器对于一些不断变化的值很有用，比如控制资源的访问：

```python
>>> class Bank(): # 让我们建个银行,生产许多ATM
...    crisis = False
...    def create_atm(self):
...        while not self.crisis:
...            yield "$100"
>>> hsbc = Bank() # 当一切就绪了你想要多少ATM就给你多少
>>> corner_street_atm = hsbc.create_atm()
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # 经济危机来了没有钱了!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # 对于其他ATM,它还是True
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # 麻烦的是,尽管危机过去了,ATM还是空的
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # 只能重新新建一个bank了
>>> for cash in brand_new_atm:
...    print cash
$100
$100
```

### Itertools 模块

该模块包含了一些特殊的函数可以操作可迭代对象，比如复制生成器，链接两个生成器等

```python
>>> horses = [1, 2, 3, 4]
>>> races = itertools.permutations(horses)
>>> print(races)
>>> print(list(itertools.permutations(horses)))
[(1, 2, 3, 4),
 (1, 2, 4, 3),
 (1, 3, 2, 4),
 (1, 3, 4, 2),
 (1, 4, 2, 3),
 ....
]
```

### 理解迭代的内部机制

迭代是可迭代对象（对应 `__iter__()` 方法）和迭代器（对应 `__next__()` 方法）的一个过程。