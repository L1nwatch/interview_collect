```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 练习一下自己怎么写一个装饰器

完整资料参考: https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/3/README.html
"""

__author__ = '__L1n__w@tch'


def no_argument_decorator(function):
    # 注意这是在脚本被解释期间(还没进入 main 代码就在跑的了)
    print("I am a 无参数修饰器")

    def wrapper():
        print("{} 装饰开始 {}".format("*" * 30, "*" * 30))
        function()
        print("{} 装饰结束 {}".format("*" * 30, "*" * 30))

    return wrapper


def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("创建装饰器, 同时接收参数: {}, {}".format(decorator_arg1, decorator_arg2))

    def my_decorator(func):
        print("装饰器, 得到参数: {}, {}".format(decorator_arg1, decorator_arg2))

        # 不要忘了装饰器参数和函数参数!
        def wrapped(*args, **kwargs):
            print("装饰函数得到的参数: {}, {}, {}, {}".format(decorator_arg1, decorator_arg2,
                                                     args, kwargs))
            return func(*args, **kwargs)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments("a", "b")
# @no_argument_decorator
def no_argument_function():
    print("I am a 普通的无参数函数")


@decorator_maker_with_arguments("a", "b")
# @no_argument_decorator
def argument_function(*args):
    print("I am a 带多个参数的函数")


@decorator_maker_with_arguments("a", "b")
# @no_argument_decorator
def args_kwargs_function(*args, **kwargs):
    print("I am a 带 args & kwargs 参数的函数")


if __name__ == "__main__":
    no_argument_function()
    argument_function("c", "d")
    args_kwargs_function("c", "d")
```