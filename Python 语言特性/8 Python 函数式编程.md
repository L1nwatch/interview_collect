# func_code
```Python
#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 函数式编程相关知识

完整版参考资料:
    http://coolshell.cn/articles/10822.html

Python 中函数式编程支持:
    filter 函数的功能相当于过滤器, 调用一个布尔函数 bool_func 来迭代遍历每个 seq 中的元素;
    返回一个使 bool_seq 返回值为 true 的元素的序列

    map 函数是对一个序列的每个项依次执行函数

    reduce 函数是对一个序列的每个项迭代调用函数
"""
import functools

__author__ = '__L1n__w@tch'


def test_filter():
    """
    测试 filter 函数的功能
    :return:
    """
    wait_to_filter = [i for i in range(10)]
    after_filter = filter(lambda x: x > 5, wait_to_filter)
    print("测试 filter: {}".format(list(after_filter)))


def test_map():
    """
    测试 map 函数的功能
    :return:
    """
    wait_to_map = [i for i in range(10)]
    after_map = map(lambda x: x * 2, wait_to_map)
    print("测试 map: {}".format(list(after_map)))


def test_reduce():
    """
    测试 reduce 函数的功能, 看 doc 说 3.4 版本的 reduce 好像有所不同
    :return:
    """
    wait_to_reduce = [i for i in range(1, 4)]
    after_reduce = functools.reduce(lambda x, y: x * y, wait_to_reduce)
    print("测试 reduce: {}".format(after_reduce))


if __name__ == "__main__":
    test_filter()  # 过滤得到大于 5 的值
    test_map()  # 对一个序列每个项都乘以 2
    test_reduce()  # 求 3 的阶乘

```