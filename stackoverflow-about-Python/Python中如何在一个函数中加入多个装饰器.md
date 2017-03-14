## Python中如何在一个函数中加入多个装饰器?

示例：

```python
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello() ## returns <b><i>hello world</i></b>
```

### 装饰器基础

*   Python 中的函数都是对象
*   你可以在一个函数里定义另一个函数

这意味着函数可以返回另一个函数

### 自己动手实现装饰器

`@decorator` 就是下面的简写：

```python
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```

### 装饰器高级用法

#### 在装饰器函数里传入参数

```python
# 这不是什么黑魔法,你只需要让包装器传递参数:

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print "I got args! Look:", arg1, arg2
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# 当你调用装饰器返回的函数时,也就调用了包装器,把参数传入包装器里,
# 它将把参数传递给被装饰的函数里.

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is", first_name, last_name

print_full_name("Peter", "Venkman")
# 输出:
#I got args! Look: Peter Venkman
#My name is Peter Venkman
```

#### 装饰方法

在 Python 里面方法和函数几乎一模一样，唯一的区别就是方法的第一个参数是一个当前对象的 self。

```python
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # 女性福音 :-)
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print "I am %s, what did you think?" % (self.age + lie)

l = Lucy()
l.sayYourAge(-3)
#输出: I am 26, what did you think?
```

如果想造一个更加通用的，可以同时满足方法和函数的装饰器，用 `*args,**kwargs` 即可

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # 包装器接受所有参数
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print "Do I have args?:"
        print args
        print kwargs
        # 现在把*args,**kwargs解包
        # 如果你不明白什么是解包的话,请查阅:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments
```

#### 把参数传递给装饰器

装饰器必须接收一个函数当做参数，所以不可以直接把被装饰函数的参数传递给装饰器

装饰器就是一个平常的函数，不用 `@` 也可以直接调用。当使用 `@my_decorator` 只是告诉 Python 去调用被变量 `my_decorator` 标记的函数

一个 DEMO

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print "I make decorators! And I accept arguments:", decorator_arg1, decorator_arg2

    def my_decorator(func):
        # 这里传递参数的能力是借鉴了 closures.
        # 如果对closures感到困惑可以看看下面这个:
        # http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print "I am the decorator. Somehow you passed me arguments:", decorator_arg1, decorator_arg2

        # 不要忘了装饰器参数和函数参数!
        def wrapped(function_arg1, function_arg2) :
            print ("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print ("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(function_arg1, function_arg2))
```

需要记住的是，装饰器只能被调用一次，当 Python 载入脚本后，不可以动态地设置参数了。即运行了 `import x` 之后，函数已经被装饰了

于是弄一个通用的装饰器，只要装饰了这个装饰器，自定义的装饰器就可以接收任意的参数了

```python
def decorator_with_args(decorator_to_enhance):
    """
    这个函数将被用来作为装饰器.
    它必须去装饰要成为装饰器的函数.
    休息一下.
    它将允许所有的装饰器可以接收任意数量的参数,所以以后你不必为每次都要做这个头疼了.
    saving you the headache to remember how to do that every time.
    """

    # 我们用传递参数的同样技巧.
    def decorator_maker(*args, **kwargs):

        # 我们动态的建立一个只接收一个函数的装饰器,
        # 但是他能接收来自maker的参数
        def decorator_wrapper(func):

            # 最后我们返回原始的装饰器,毕竟它只是'平常'的函数
            # 唯一的陷阱:装饰器必须有这个特殊的,否则将不会奏效.
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper
     return decorator_maker
```

删除多余注释：

```python
def decorator_with_args(decorator_to_enhance):
    """
    这个函数将被用来作为装饰器. 使得被它装饰的装饰器可以接收多个参数
    """

    def decorator_maker(*args, **kwargs):
        def decorator_wrapper(func):
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker
```

使用方法：

```python
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print "Decorated with", args, kwargs
        return func(function_arg1, function_arg2)
    return wrapper
```

之后调用这个自定义的装饰器，就可以传递任意参数了：

```python
@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print "Hello", function_arg1, function_arg2

decorated_function("Universe and", "everything")
#输出:
#Decorated with (42, 404, 1024) {}
#Hello Universe and everything
```

自己成功使用的示例：

```python
@decorator_with_args
def log_wrapper(func, *args, **kwargs):
    def wrapper(*func_args, **func_kwargs):
        print("[*] 测试装饰器")
        return func(*func_args, **func_kwargs)

    return wrapper
```

### 后续

*   装饰器是 Python2.4 里面引进的，所以确保 Python 解释器的版本 >= 2.4
*   装饰器使函数调用变慢了
*   装饰器不能被取消
*   用装饰器装饰函数，可能会导致 DEBUG 难度变高

### functools 模块

`functools.wraps()` 函数，可以复制装饰器的名字、模块和文档给它的包装器【PS：`functools.wraps()` 本身就是一个装饰器】

```python
#为了debug,堆栈跟踪将会返回函数的 __name__
def foo():
    print "foo"

print foo.__name__
#输出: foo

# 如果加上装饰器,将变得有点复杂
def bar(func):
    def wrapper():
        print "bar"
        return func()
    return wrapper

@bar
def foo():
    print "foo"

print foo.__name__
#输出: wrapper

# "functools" 将有所帮助

import functools

def bar(func):
    # 我们所说的"wrapper",正在包装 "func",
    # 好戏开始了
    @functools.wraps(func)
    def wrapper():
        print "bar"
        return func()
    return wrapper

@bar
def foo():
    print "foo"

print foo.__name__
#输出: foo
```

### 装饰器的用途

传统的用法就是用它来为外部的库函数（你不能修改的）做扩展或者 DEBUG（你不想修改的）

Python 自身提供了几个装饰器，像 `property`、`staticmethod`

*   Django 用装饰器管理缓存和视图的权限
*   Twisted 用来修改异步函数的调用

