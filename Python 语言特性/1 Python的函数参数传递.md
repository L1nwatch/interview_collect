```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 参考网上资料, 关于 Python 的函数参数传递问题

总结:
    在 Python 中, strings, tuples, numbers 是不可更改的对象, 而 list, dict 等则是可以修改的对象
"""

__author__ = '__L1n__w@tch'


def modify_fun_fail(value):
    """
    当一个引用传递给函数的时候, 函数自动复制一份引用, 这个函数里的引用和外边的引用没有关系
    所以这里函数把引用指向了一个不可变对象, 当函数返回的时候, 外面的引用不会被改变
    :param value: int()
    :return: None
    """
    value += 50
    print("调用函数 {}, 修改值为 {}".format("modify_fun_fail", value))


def modify_fun_success(a_list):
    """
    函数内的引用指向的是可变对象, 对它的操作就和定位了指针地址一样, 在内存里进行修改
    :param a_list: list()
    :return: None
    """
    a_list.append(1)
    print("调用函数 {}, 修改值为 {}".format("modify_fun_success", a_list))


if __name__ == "__main__":
    number = 30
    print("接下来调用函数 {}, 当前 number 值为 {}".format("modify_fun_fail", number))
    modify_fun_fail(number)
    print("调用完成, number 值为 {}".format(number), end="\n\n")

    number_list = list()
    print("接下来调用函数 {}, 当前 number_list 值为 {}".format("modify_fun_success", number_list))
    modify_fun_success(number_list)
    print("调用完成, number_list 值为 {}".format(number_list))
```