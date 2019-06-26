#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python2.X
"""
题目描述
百马百担问题。有100匹马，驮100担货，大马驮3担，中马驮2担，两匹小马1担，编程计算所有可能的驮法？

输入
无

输出
输出所有可能的驮法。

每行输出一种驮法，每种驮法依次输出：

大马数，中马数，小马数

如2,30,68
表示大马数为2，中马数为30，小马数为68

样例输出
2,30,68
5,25,70
8,20,72
11,15,74
14,10,76
17,5,78
20,0,80
"""

__author__ = '__L1n__w@tch'


def solve():
    for x in range(100 / 3):
        for y in range(100):
            z = 100 - x - y
            if x * 3 + y * 2 + z / 2.0 == 100:
                print("{},{},{}".format(x, y, z))


if __name__ == "__main__":
    while True:
        try:
            solve()
            break
        except EOFError:
            break
