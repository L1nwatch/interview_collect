```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 讨论关于单下划线和双下划线命名的问题

总结:
    __foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突.
    _foo:一种约定,用来指定变量私有.程序员用来指定私有变量的一种方式.
    __foo:这个有真正的意义:解析器用_className__foo来代替这个名字,以区别和其他类相同的命名.
"""

__author__ = '__L1n__w@tch'


class UnderlineTest:
    def __init__(self):
        self.__super_private = "超级私有"
        self._semi_private = "假私有"


if __name__ == "__main__":
    ut = UnderlineTest()
    try:
        print(ut.__super_private)
    except AttributeError as e:
        print("[!] 找不到超级私有")
        print(e)

    print("寻找假私有{}: {}", "ut._semi_private", ut._semi_private)
    print("打印 __dict__: {}".format(ut.__dict__))
```