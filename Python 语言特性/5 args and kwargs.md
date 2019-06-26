```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 讨论关于 args 和 kwargs 的相关知识点

总结:
    当你不确定你的函数里将要传递多少参数时你可以用 *args
    **kwargs 允许你使用没有事先定义的参数名
    可以混着用, 命名参数首先获得参数值然后所有的其他参数都传递给 *args 和 **kwargs

"""

__author__ = '__L1n__w@tch'


def test_args(*args):
    # 当你不确定你的函数里将要传递多少参数时你可以用 *args
    for count, value in enumerate(args):
        print("{}: {}".format(count, value))


def test_kwargs(**kwargs):
    # **kwargs 允许你使用没有事先定义的参数名
    for key, value in kwargs.items():
        print("Key:Value, {}:{}".format(key, value))


# 当调用函数时你也可以用 * 和 ** 语法
def star_operation(name, value, count):
    print("Name: {}, Value: {}, Count: {}".format(name, value, count))


if __name__ == "__main__":
    test_args("a", "1", "c", "b", "3", "2")
    test_kwargs(test1=1, test2=2, test3=3)

    # 它可以传递列表(或者元组)的每一项并把它们解包. 注意必须与它们在函数里的参数相吻合
    a_list = ["名字", "值", "计数器"]
    star_operation(*a_list)
```