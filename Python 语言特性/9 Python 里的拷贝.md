# about_copy.py
```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 关于 Python 的拷贝, 有引用/浅复制/深复制的区别, (引用和 copy(), deepcopy() 的区别)
"""

import copy

__author__ = '__L1n__w@tch'

if __name__ == "__main__":
    List = [1, 2, 3, 4, ["a", "b"]]

    one_list = List  # 赋值, 传对象的引用
    second_list = copy.copy(List)  # 对象拷贝, 浅拷贝
    third_list = copy.deepcopy(List)  # 对象拷贝，深拷贝

    List.append(5)  # 修改对象 List
    List[4].append("c")

    print("List: {}".format(List))
    print("one_list: {}".format(one_list))
    print("second_list: {}".format(second_list))
    print("third_list: {}".format(third_list))
```