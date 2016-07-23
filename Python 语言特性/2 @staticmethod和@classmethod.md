```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Python 有 4 个方法, 静态方法(staticmethod), 类方法(classmethod), 实例方法, 普通方法
"""

__author__ = '__L1n__w@tch'


def normal_function():
    print("I am just a 普通方法")


class FunctionTest:
    def method(self, value):
        """
        self 是对实例的绑定, 需要把实例自己传给函数, 调用的时候是这样的 ft.method(value), 其实是 method(ft, value)
        :param value: int()
        :return: None
        """
        print("I am just a 实例方法, {}; {}".format(self, value))

    @classmethod
    def class_method(cls, value):
        """
        # cls是对类的绑定
        :param value: int()
        :return: None
        """
        print("I am just a 类方法, {}; {}".format(cls, value))

    @staticmethod
    def static_method(value):
        print("I am just a 静态方法, 打印值 {}".format(value))


if __name__ == "__main__":
    ft = FunctionTest()

    normal_function()

    ft.method(3.4)
    ft.static_method(3.4)
    ft.class_method(3.4)

    FunctionTest.static_method(3.4)
    FunctionTest.class_method(3.4)
```